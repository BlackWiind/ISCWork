# RSA шифр, в качестве сообщения только целые числа
from common_algorithms import module_degree, evclid_extended


class RSAAlg:

    def __init__(self, p: int, q: int, d: int):
        self.n = p * q
        self.d = d
        self.fi = (p - 1) * (q - 1)
        self.open_key = (d, self.n)
        private_key = evclid_extended(self.fi, self.d)[2]
        self.private_key = private_key if private_key > 0 else private_key + self.fi

    def encrypt_message(self, open_key: tuple, message: int) -> int:
        # Шифровка сообщения, open key от адресата сообщения
        return module_degree(message, open_key[0], open_key[1])

    def decrypt_message(self, encrypted_message: int) -> int:
        # Расшифровка сообщения
        return module_degree(encrypted_message, self.private_key, self.n)


def demonstration(p: int, q: int, d: int, message: int):
    user = RSAAlg(p, q, d)
    encrypted_message = user.encrypt_message(user.open_key, message)
    decrypted_message = user.decrypt_message(encrypted_message)

    print(f"Алгоритм RSA:\n"
          f"Входные данные P= {p},Q= {q}, d= {d}\n"
          f"Сообщение: {message}\n"
          f"Зашифровонне сообщение: {encrypted_message}\n"
          f"Расшифрованное сообщение: {decrypted_message}\n")