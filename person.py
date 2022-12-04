import copy
import random
from common_algorithms import module_degree, RSAAlg

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


class Person:

    def __init__(self, p: int = CONSTANT_P, q: int = CONSTANT_Q, variant: int = VARIANT):
        self.p = p
        self.q = q
        self.rules = self.rule(variant)
        self.gelmintov_cicle: list = []
        self.open_key: tuple = None
        self.h_matrix: list = self.izomorf(self.rules, BASE_MATRIX)
        self.tilda_h_matrix: list = self.tilda_matrix(copy.deepcopy(self.h_matrix))
        self.f_matrix: list = self.crypted_matrix(copy.deepcopy(self.tilda_h_matrix), self.p, self.q)

    def rule(self, rule: int) -> list:
        rules_of_nature: list = []
        for row in range(8):
            # ((a+Z)mod 8), изменино с 9 на 8 т.к. индексация с нуля
            rules_of_nature.append(module_degree((row + rule), 1, 8))
        return rules_of_nature

    def izomorf(self, rules: list, matrix: list) -> list:
        """
        Находит изоморфный граф.
        Возвращает матрицу смежности.
        :param rules: list
        :return: List[][]
        """
        new_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
        for row_index, row in enumerate(matrix):
            for item_index, item in enumerate(row):
                new_matrix[row_index][item_index] = matrix[rules[item_index]][rules[row_index]]

        return new_matrix

    def tilda_matrix(self, matrix: list) -> list:
        """
        Приписывает к значениям в матрице случайные числа слева.
        Технически плюсует десятки.
        :param matrix: List[][]
        :return: List[][]
        """
        tuple_for_random: tuple = (10, 20, 30, 40, 50)
        for row_index, row in enumerate(matrix):
            for item_index, item in enumerate(row):
                matrix[row_index][item_index] += random.choice(tuple_for_random)
                # if matrix[row_index][item_index] % 2 != 0:
                #     self.gelmintov_cicle.append((row_index, item_index, matrix[row_index, item_index]))

        return matrix

    def crypted_matrix(self, matrix: list, p: int, q: int) -> list:
        rsa = RSAAlg(p, q)
        self.open_key = rsa.open_key
        for row_index, row in enumerate(matrix):
            for item_index, item in enumerate(row):
                matrix[row_index][item_index] = rsa.encrypt_message(rsa.open_key, matrix[row_index][item_index])
        return matrix

    def create_matrixs(self, base_matrix: list):
        self.h_matrix = self.izomorf(self.rules, base_matrix)
        self.tilda_h_matrix = self.tilda_matrix(copy.deepcopy(self.h_matrix))
        self.f_matrix = self.crypted_matrix(copy.deepcopy(self.tilda_h_matrix), self.p, self.q)

    def get_h_matrix(self) -> list:
        if not self.h_matrix:
            raise ValueError("Не сгенерирована матрица H")
        return self.h_matrix

    def get_tilda_h_matrix(self) -> list:
        if not self.tilda_h_matrix:
            raise ValueError("Не сгенерирована матрица ~H")
        return self.tilda_h_matrix

    def get_f_matrix(self) -> list:
        if not self.f_matrix:
            raise ValueError("Не сгенерирована матрица ~F")
        return self.f_matrix


def question_one(f_matrix: list, tilda_matrix: list, numbers: list, key: tuple) -> bool:
    tilda_one = copy.deepcopy(tilda_matrix)
    tilda_two = copy.deepcopy(tilda_matrix)
    new_matrix = [[0] * len(tilda_matrix) for _ in range(len(tilda_matrix))]
    for row_index, row in enumerate(tilda_one):
        for item_index, item in enumerate(row):
            tilda_one[row_index][item_index] = module_degree(tilda_one[row_index][item_index], key[0], key[1])
    if f_matrix != tilda_one:
        return False

    for row_index, row in enumerate(tilda_two):
        for item_index, item in enumerate(row):
            tilda_two[row_index][item_index] = tilda_two[row_index][item_index] % 2
            new_matrix[numbers[item_index]][numbers[row_index]] = tilda_two[row_index][item_index]
    if BASE_MATRIX != new_matrix:
        return False
    return True


def question_two() -> bool:
    return True


def verification(persona: object) -> str:
    answer: str = f"Выполнена верификация:\n"
    for _ in range(random.randint(1, 20)):
        #person_A = Person(CONSTANT_P, CONSTANT_Q, VARIANT)
        persona.create_matrixs(BASE_MATRIX)
        if random.randint(0, 1) > 0:
            answer += "Выбран первый вопрос, "
            answer += "ответ верный\n" if question_one(persona.get_f_matrix(), persona.get_tilda_h_matrix(), persona.rules, persona.open_key) else "ответ неверный\n"
        else:
            answer += "Выбран второй вопрос, "
            answer += "ответ верный\n" if question_two() else "ответ неверный\n"
    return answer
