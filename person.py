import copy
import random
from rsa_alg import RSAAlg
from common_algorithms import module_degree

class Person:

    def __init__(self, p: int, q: int, variant: int):
        self.p = p
        self.q = q
        self.rules = self.rule(variant)
        self.gelmintov_cicle: list = []
        self.open_key: tuple = None
        self.h_matrix: list = None
        self.tilda_h_matrix: list = None
        self.f_matrix: list = None

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
        :param rule: int
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
                if matrix[row_index][item_index] % 2 != 0:
                    self.gelmintov_cicle.append((row_index, item_index, matrix[row_index, item_index]))
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


