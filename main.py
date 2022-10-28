import random
import rsa_alg
from common_algorithms import module_degree

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


def izomorf(rule: int) -> list:
    """
    Находит изоморфный граф.
    Возвращает матрицу смежности.
    :param rule: int
    :return: List[][]
    """
    rules_of_nature: list = []
    for row in range(len(BASE_MATRIX)):
        # ((a+Z)mod 8), изменино с 9 на 8 т.к. индексация с нуля
        rules_of_nature.append(module_degree((row + rule), 1, 8))

    new_matrix = [[0] * len(BASE_MATRIX) for _ in range(len(BASE_MATRIX))]
    for row_index, row in enumerate(BASE_MATRIX):
        for item_index, item in enumerate(row):
            new_matrix[row_index][item_index] = BASE_MATRIX[rules_of_nature[item_index]][rules_of_nature[row_index]]

    return new_matrix


def tilda_matrix(matrix: list) -> list:
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
    return matrix


def main():
    h_matrix = izomorf(VARIANT)
    h_matrix = tilda_matrix(h_matrix)

    for matrix_row in h_matrix:
        print(f"{matrix_row}")


if __name__ == '__main__':
    main()
