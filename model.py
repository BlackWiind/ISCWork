import copy
import utils

CONSTANT_P: int = 19
CONSTANT_Q: int = 41
VARIANT: int = 3

BASE_MATRIX: list = [
    [0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0],
]


class Model:

    def __init__(self, p: int = CONSTANT_P, q: int = CONSTANT_Q, variant: int = VARIANT):
        self._p = p
        self._q = q
        self._rules = utils.rule(variant)
        self._open_key: tuple = utils.rsa_open_key(self._p, self._q)
        self._private_key: int = utils.rsa_private_key(self._p, self._q)
        self._h_matrix: list = utils.izomorf(self._rules, BASE_MATRIX)
        self._tilda_h_matrix: list = utils.tilda_matrix(copy.deepcopy(self._h_matrix))
        self._f_matrix: list = utils.crypted_matrix(copy.deepcopy(self._tilda_h_matrix), self._open_key)
        self._gemiltonov_cycle: list = utils.get_cycle(self._tilda_h_matrix)

    @property
    def rules(self):
        return self._rules

    @property
    def h_matrix(self):
        return self._h_matrix

    @property
    def tilda_matrix(self):
        return self._tilda_h_matrix

    @property
    def f_matrix(self):
        return self._f_matrix

    @property
    def open_key(self):
        return self._open_key

    @property
    def cycle(self):
        return self._gemiltonov_cycle

    def all_matrixs(self) -> dict:
        matrixs = {
            "h_matrix": self._h_matrix,
            "f_matrix": self._f_matrix,
            "tilda_matrix": self._tilda_h_matrix,
            "cycle": self._gemiltonov_cycle,
            "b_matrix": BASE_MATRIX,
        }
        return matrixs


def b_matrix() -> list:
    return BASE_MATRIX
