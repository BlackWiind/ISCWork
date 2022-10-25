import rsa_alg

CONSTANT_P: int = 19
CONSTANT_Q: int = 41
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


def main():
    indexs = [6, 3, 4, 2, 0, 1, 7, 5]
    new_matrix = BASE_MATRIX
    for i in range(8):
        for j in range(8):
            print(i,j)
            new_matrix[i][j] = BASE_MATRIX[indexs[i]][indexs[j]]
            print(indexs[i], indexs[j])
            print(BASE_MATRIX[indexs[i]][indexs[j]])
        print(new_matrix[i])
    for matrix in new_matrix:
        print(f"{matrix}\n")


if __name__ == '__main__':
    main()
