import random
import copy


def module_degree(basis: int, grade: int, module: int, optional=1) -> int:
    # Возведение в степень по модулю
    return (optional * basis ** grade) % module


def module_inversion(a: int, c: int) -> int:
    # Обратная инверсия по модулю
    for i in range(c):
        if (a * i) % c == 1:
            answer = i
    if answer:
        return answer


def evclid_extended(num1: int, num2: int) -> int:
    # Обобщенный алгоритм Евклида
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = evclid_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)


def rule(rule: int) -> list:
    rules: list = [7, 4, 5, 3, 1, 2, 8, 6]
    for row in range(len(rules)):
        rules[row] = module_degree((rules[row] + rule), 1, 8)  # 8 т.к индексация начинается с нуля
    return rules


def izomorf(rules: list, matrix: list) -> list:
    """
    Находит изоморфный граф.
    Возвращает матрицу смежности.
    :param rules: list
    :return: list
    """
    new_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
    for row_index, row in enumerate(matrix):
        for item_index, item in enumerate(row):
            new_matrix[row_index][item_index] = matrix[rules[item_index]][rules[row_index]]

    return new_matrix


def tilda_matrix(matrix: list) -> list:
    """
    Приписывает к значениям в матрице случайные числа слева.
    Технически плюсует десятки.
    :param matrix: list
    :return: list
    """
    tuple_for_random: tuple = (10, 20, 30, 40, 50)
    for row_index, row in enumerate(matrix):
        for item_index, item in enumerate(row):
            matrix[row_index][item_index] += random.choice(tuple_for_random)

    return matrix


def crypted_matrix(matrix: list, open_key: tuple) -> list:
    for row_index, row in enumerate(matrix):
        for item_index, item in enumerate(row):
            matrix[row_index][item_index] = rsa_encrypt_message(open_key, matrix[row_index][item_index])
    return matrix


def question_one(matrixs: dict, numbers: list, key: tuple) -> bool:
    tilda_one = copy.deepcopy(matrixs["tilda_matrix"])
    tilda_two = copy.deepcopy(matrixs["tilda_matrix"])
    new_matrix = [[0] * len(matrixs["tilda_matrix"]) for _ in range(len(matrixs["tilda_matrix"]))]
    for row_index, row in enumerate(tilda_one):
        for item_index, item in enumerate(row):
            tilda_one[row_index][item_index] = module_degree(tilda_one[row_index][item_index], key[0], key[1])
    if matrixs["f_matrix"] != tilda_one:
        return False

    for row_index, row in enumerate(tilda_two):
        for item_index, item in enumerate(row):
            tilda_two[row_index][item_index] = tilda_two[row_index][item_index] % 2
            new_matrix[numbers[item_index]][numbers[row_index]] = tilda_two[row_index][item_index]
    if matrixs["b_matrix"] != new_matrix:
        return False
    return True


def question_two(cycle: list, f_matrix: list, key: tuple) -> bool:
    is_verified = True
    for point in cycle:
        if module_degree(point[2], key[0], key[1]) != f_matrix[point[0]][point[1]]:
            is_verified = False

    return is_verified


def rsa_open_key(p: int, q: int) -> tuple:
    n = p * q
    d = find_d((p - 1) * (q - 1))
    return (d, n)


def rsa_private_key(p: int, q: int) -> int:
    fi = (p - 1) * (q - 1)
    private_key = evclid_extended(fi, find_d(fi))[2]
    return private_key if private_key > 0 else private_key + fi


def rsa_encrypt_message(open_key: tuple, message: int) -> int:
    return module_degree(message, open_key[0], open_key[1])


def rsa_decrypt_message(private_key: int, encrypted_message: int, p: int, q: int) -> int:
    return module_degree(encrypted_message, private_key, p * q)


def find_d(fi: int) -> int:
    # Находит d взаимно простое с fi такое, что d<fi
    d: int = random.randint(0, fi - 1)
    return d if evclid_extended(d, fi)[0] == 1 else find_d(fi)


def get_cycle(matrix: list) -> list:
    cycle: list = [[0, 5], [1, 2], [2, 3], [3, 4], [4, 1], [5, 6], [6, 7], [7, 0]]
    for indexs in cycle:
        indexs.append(matrix[indexs[0]][indexs[1]])
    return cycle
