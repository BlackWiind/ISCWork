import copy
import random
from rsa_alg import RSAAlg
from common_algorithms import module_degree
from person import Person

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


# def izomorf(rule: int) -> list:
#     """
#     Находит изоморфный граф.
#     Возвращает матрицу смежности.
#     :param rule: int
#     :return: List[][]
#     """
#     rules_of_nature: list = []
#     for row in range(len(BASE_MATRIX)):
#         # ((a+Z)mod 8), изменино с 9 на 8 т.к. индексация с нуля
#         rules_of_nature.append(module_degree((row + rule), 1, 8))
#
#     new_matrix = [[0] * len(BASE_MATRIX) for _ in range(len(BASE_MATRIX))]
#     for row_index, row in enumerate(BASE_MATRIX):
#         for item_index, item in enumerate(row):
#             new_matrix[row_index][item_index] = BASE_MATRIX[rules_of_nature[item_index]][rules_of_nature[row_index]]
#
#     return new_matrix
#
#
# def tilda_matrix(matrix: list) -> list:
#     """
#     Приписывает к значениям в матрице случайные числа слева.
#     Технически плюсует десятки.
#     :param matrix: List[][]
#     :return: List[][]
#     """
#     tuple_for_random: tuple = (10, 20, 30, 40, 50)
#     for row_index, row in enumerate(matrix):
#         for item_index, item in enumerate(row):
#             matrix[row_index][item_index] += random.choice(tuple_for_random)
#     return matrix
#
#
# def crypted_matrix(matrix: list) -> list:
#     rsa = RSAAlg(CONSTANT_P, CONSTANT_Q)
#     for row_index, row in enumerate(matrix):
#         for item_index, item in enumerate(row):
#             matrix[row_index][item_index] = rsa.encrypt_message(rsa.open_key, matrix[row_index][item_index])
#     return matrix


def question_one(f_matrix: list, tilda_matrix: list, numbers: list, key: tuple) -> bool:
    for row_index, row in enumerate(tilda_matrix):
        for item_index, item in enumerate(row):
            tilda_matrix[row_index][item_index] = module_degree(tilda_matrix[row_index][item_index], key[0], key[1])
    if f_matrix != tilda_matrix:
        raise ValueError("фвфывфы")
    return True


def question_two() -> bool:
    return True


def chek_b(f_matrix: list, open_key: tuple) -> bool:
    if random.randint(0, 1) > 0:
        print("Выбран первый вопрос")
        return question_one()
    else:
        print("Выбран второй вопрос")
        return question_two()

def main():
    for _ in range(random.randint(1, 20)):
        person_A = Person(CONSTANT_P, CONSTANT_Q, VARIANT)
        person_A.create_matrixs(BASE_MATRIX)
        if random.randint(0, 1) > 0:
            print("Выбран первый вопрос")
            question_one(person_A.get_f_matrix(), person_A.get_tilda_h_matrix(), person_A.rules, person_A.open_key)
        else:
            print("Выбран второй вопрос")
            question_two()
        # if not chek_b(person_A.get_f_matrix(), person_A.open_key):
        #     raise ValueError("Верификация не пройдена")

    print("Верификация пройдена")




if __name__ == '__main__':
    main()
