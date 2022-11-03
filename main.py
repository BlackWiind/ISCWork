import copy
import random
from common_algorithms import module_degree
from person import Person
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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


def question_one(f_matrix: list, tilda_matrix: list, numbers: list, key: tuple) -> bool:
    tilda_one = copy.deepcopy(tilda_matrix)
    tilda_two = copy.deepcopy(tilda_matrix)
    new_matrix = [[0] * len(tilda_matrix) for _ in range(len(tilda_matrix))]
    for row_index, row in enumerate(tilda_one):
        for item_index, item in enumerate(row):
            tilda_one[row_index][item_index] = module_degree(tilda_one[row_index][item_index], key[0], key[1])
    if f_matrix != tilda_one:
        raise ValueError("Графы не изоморфны")

    for row_index, row in enumerate(tilda_two):
        for item_index, item in enumerate(row):
            tilda_two[row_index][item_index] = tilda_two[row_index][item_index] % 2
            new_matrix[numbers[item_index]][numbers[row_index]] = tilda_two[row_index][item_index]
    if BASE_MATRIX != new_matrix:
        raise ValueError("Графы не изоморфны")
    return True


def question_two() -> bool:
    return True


def main():
    G = nx.DiGraph(np.matrix(BASE_MATRIX))
    nx.draw(G, with_labels=True, node_size=300, arrows=False)
    plt.show()
    for _ in range(random.randint(1, 20)):
        person_A = Person(CONSTANT_P, CONSTANT_Q, VARIANT)
        person_A.create_matrixs(BASE_MATRIX)
        if random.randint(0, 1) > 0:
            print("Выбран первый вопрос")
            question_one(person_A.get_f_matrix(), person_A.get_tilda_h_matrix(), person_A.rules, person_A.open_key)
        else:
            print("Выбран второй вопрос")
            question_two()
    print("Верификация пройдена")


if __name__ == '__main__':
    main()
