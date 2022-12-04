import random


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


class RSAAlg:

    def __init__(self, p: int, q: int, d: int = None):
        self.n = p * q
        self.fi = (p - 1) * (q - 1)
        self.d = d if d else find_d(self.fi)
        self.open_key = (self.d, self.n)
        private_key = evclid_extended(self.fi, self.d)[2]
        self.private_key = private_key if private_key > 0 else private_key + self.fi

    def find_d(self):
        pass

    def encrypt_message(self, open_key: tuple, message: int) -> int:
        # Шифровка сообщения, open key от адресата сообщения
        return module_degree(message, open_key[0], open_key[1])

    def decrypt_message(self, encrypted_message: int) -> int:
        # Расшифровка сообщения
        return module_degree(encrypted_message, self.private_key, self.n)


def find_d(fi: int) -> int:
    # Находит d взаимно простое с fi такое, что d<fi
    d: int = random.randint(0, fi-1)
    return d if evclid_extended(d, fi)[0] == 1 else find_d(fi)
