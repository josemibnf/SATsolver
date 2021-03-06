from threading import get_ident, Thread, Lock, Event
import requests, json
from start import DIR, TRAIN_SOLVERS_TIMEOUT, LOGGER, CONNECTION_ERRORS, START_AVR_TIMEOUT
from start import SAVE_TRAIN_DATA as REFRESH
from singleton import Singleton
import _solve


class Session(metaclass=Singleton):

    def __init__(self):
        self.thread = None
        self.random_service_instance = None
        self.solvers = json.load(open(DIR + 'solvers.json', 'r'))
        self.solvers_lock = Lock()
        self.exit_event = None
        self._solver = _solve.Session()

    def stop(self):
        if self.exit_event and self.thread:
            self.exit_event.set()
            self.thread.join()
            self.random_service_instance.stop()
            self.exit_event = None
            self.thread = None

    def load_solver(self, solver):
        self.solvers_lock.acquire()
        self.solvers.update({solver: {}})
        self.solvers_lock.release()

    def init_random_cnf_service(self):
        self.random_service_instance = _solve.get_image_uri(
            '07a9852b10c5bbc9c55180d43d70561854f6a8f5fc8a28483bf893cac0871e0b')

    def random_cnf(self):
        def new_instance():
            LOGGER('VAMOS A CAMBIAR EL SERVICIO DE OBTENCION DE CNFs RANDOM')
            self.random_service_instance.stop()
            self.init_random_cnf_service()
            LOGGER('listo. ahora vamos a probar otra vez.')
        connection_errors = 0
        while True:
            try:
                LOGGER('OBTENIENDO RANDON CNF')
                response = requests.get(
                    'http://' + self.random_service_instance.uri + '/',
                    timeout = START_AVR_TIMEOUT
                )
                LOGGER('RESPUESTA DEL CNF --> ' + str(response) + str(response.text))
            except requests.exceptions.ConnectionError as e:
                if connection_errors < CONNECTION_ERRORS:
                    connection_errors = connection_errors +1
                    continue
                else:
                    connection_errors = 0
                    LOGGER('  ERROR OCCURS OBTAINING THE CNF --> '+ str(e))
                    new_instance()
                    continue
            except (TimeoutError, requests.exceptions.ReadTimeout, requests.HTTPError) as e:
                LOGGER('  ERROR OCCURS OBTAINING THE CNF --> '+ str(e))
                new_instance()
                continue
            if response and response.status_code == 200 and 'cnf' in response.json():
                    return response.json().get('cnf')

    @staticmethod
    def isGood(cnf, interpretation):
        def goodClause(clause, interpretation):
            for var in clause:
                for i in interpretation:
                    if var == i:
                        return True
            return False

        for clause in cnf:
            if not goodClause(clause, interpretation):
                return False
        return True

    def updateScore(self, cnf, solver, score):
        num_clauses, num_literals = (
            len(cnf),
            0,
        )
        for clause in cnf:
            for literal in clause:
                if abs(literal) > num_literals:
                    num_literals = abs(literal)
        type_of_cnf = str(num_clauses) + ':' + str(num_literals)
        if type_of_cnf in self.solvers[solver]:
            solver_cnf = self.solvers[solver][type_of_cnf]
        else:
            solver_cnf = {
                'index': 1,
                'score': 0
            }
        self.solvers[solver].update({
            str(num_clauses) + ':' + str(num_literals): {
                'index': solver_cnf['index'] + 1,
                'score': (solver_cnf['score'] * solver_cnf['index'] + score) / (solver_cnf['index'] + 1)
            }
        })

    def start(self):
        if self.exit_event and self.thread: return None
        try:
            self.exit_event = Event()
            self.thread = Thread(target=self.init, name='Trainer')
            self.thread.start()
        except RuntimeError:
            LOGGER('Error: train thread was started and have an error.')

    def init(self):
        LOGGER('TRAINER THREAD IS ' + str(get_ident()))
        refresh = 0
        timeout = TRAIN_SOLVERS_TIMEOUT
        LOGGER('INICIANDO SERVICIO DE RANDOM CNF')
        self.init_random_cnf_service()
        LOGGER('hecho.')
        while True:
            if self.exit_event.is_set(): break
            if refresh < REFRESH:
                LOGGER('REFRESH ES MENOR')
                refresh = refresh + 1
                cnf = self.random_cnf()
                is_insat = True  # En caso en que se demuestre lo contrario.
                insats = {}  # Solvers que afirman la insatisfactibilidad junto con su respectivo tiempo.
                LOGGER('VAMOS A PROBAR LOS SOLVERS')
                self.solvers_lock.acquire()
                for solver in self.solvers:
                    LOGGER('SOVLER --> ' + str(solver))
                    try:
                        interpretation, time = self._solver.cnf(cnf=cnf, solver=solver, timeout=timeout)
                        if interpretation == [] or interpretation is None:
                            insats.update({solver: time})
                        else:
                            if self.isGood(cnf, interpretation):
                                is_insat = False
                            else:
                                pass
                            if time == 0:
                                score = +1
                            else:
                                score = float(-1 / time)
                            self.updateScore(
                                cnf=cnf,
                                solver=solver,
                                score=score
                            )
                    except (TimeoutError, requests.exceptions.ReadTimeout):
                        LOGGER('TIME OUT NO SUPERADO.')
                        if timeout == 0:
                            score = -1
                        else:
                            score = float(-1 / timeout)
                        self.updateScore(
                            cnf=cnf,
                            solver=solver,
                            score=score
                        )
                self.solvers_lock.release()
                # Registra los solvers que afirmaron la insatisfactibilidad en caso en que ninguno
                #  haya demostrado lo contrario.
                if is_insat:
                    for solver in insats:
                        self.updateScore(
                            cnf=cnf,
                            solver=solver,
                            score=float(+1 / insats.get(solver)) if insats.get(solver) != 0 else 1
                        )
                else:
                    for solver in insats:
                        self.updateScore(
                            cnf=cnf,
                            solver=solver,
                            score=float(-1 / insats.get(solver)) if insats.get(solver) != 0 else -1
                        )
            else:
                LOGGER('ACTUALIZA EL JSON')
                refresh = 0
                with open(DIR + 'solvers.json', 'w') as file:
                    json.dump(self.solvers, file)
