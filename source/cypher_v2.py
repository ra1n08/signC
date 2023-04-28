# for parameters creator
import random
from _math import is_prime
import secrets
import ast
# fpr signcrypt and unsigncrypt
from _math import modPrimePow, fast_exponentiation
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import hashlib


def generate_prime(bit):
    Q = random.getrandbits(bit)
    while not is_prime(Q):
        Q = random.getrandbits(bit)
    return Q


def hash_to_128(value):
    sha256 = hashlib.sha256(value.encode())
    hex_dig = sha256.hexdigest()
    k1 = hex_dig[:32]
    k2 = hex_dig[32:]
    return k1, k2

def encrypt_text(plaintext, key, iv):
    backend = default_backend()
    padder = PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(ciphertext)

def hash_function(key, plantext):
    sha256 = hashlib.sha256()
    sha256.update(key + plantext.encode('utf-8'))
    return sha256.hexdigest()


def calculate_hash(x, yb, p):
    value = modPrimePow(yb, x, p)
    k1, k2 = hash_to_128(str(value))
    return k1, k2


class Parameter:
    def __init__(self, bit) -> None:

        self.param_path = f"./thamso"
        self.Q = generate_prime(bit)
        self.R = random.getrandbits(20)
        self.P = self.cal_P()
        self.P_path = f"{self.param_path}/P.txt"
        self.percent = 0
        # self.g = None
        # self.a = None
        # self.p = None
        # self.x = None
        self.g, self.a, self.p, self.x = None, None, None, None

    def cal_P(self):
        while True:
            P = self.Q * self.R + 1
            if is_prime(P):
                # print("P = ", P)
                return P
            else:
                self.Q = generate_prime(160)
                self.R = random.getrandbits(20)
                # pass

    def write_P(self):
        self.P = int(self.P)
        with open(self.P_path, "w") as f:
            f.write(str(self.P))

    def read_P(self):
        with open(self.P_path, "r") as f:
            self.p = int(f.read().strip())

    def generate_matching_pair(self):
        Q = generate_prime(160)
        PR_path = f"{self.param_path}/PR.txt"
        with open(PR_path, "w") as f:
            for R in range(1, 100000):
                self.percent = R / 100000 * 100
                # print(f"Progress: {self.percent:.2f}%", end="\r")
                # calculate the value of P
                P = Q * R + 1
                # check if P is prime
                if is_prime(P):
                    # write the matching pair to file
                    f.write(f"({P}, {R})\n")
                yield self.percent

    def select_g(self):
        input_path = f"./{self.param_path}/PR.txt"
        out_path = f"./{self.param_path}/tapG.txt"
        with open(input_path, "r") as f:
            # pairs = [eval(line.strip()) for line in f]
            pairs = [ast.literal_eval(line.strip()) for line in f]

        valid_g = False
        while not valid_g:
            P, R = random.choice(pairs)

            h = random.randint(1, P - 1)

            self.g = pow(h, R, P)

            if pow(self.g, R, P) != 1:
                valid_g = True

        with open(out_path, "w") as f:
            f.write(f"{self.g}\n")
        x = self.g
        with open(f"./{self.param_path}/giatrix.txt", "w") as f:
            f.write(f"{x}\n")
        print("x = ", x)
        print("x saved successfully")

    def select_a(self):
        self.a = random.randint(2, 200)
        print("a = ", self.a)
        with open(f"./{self.param_path}/a.txt", "w") as f:
            f.write(str(self.a))

    def sender_XA(self):
        input_file_path = f"./{self.param_path}/PR.txt"
        output_file_path = f"./{self.param_path}/xa.txt"

        with open(input_file_path, "r") as f:
            pairs = [ast.literal_eval(line.strip()) for line in f]

        valid_xa = False
        while not valid_xa:
            P, R = random.choice(pairs)
            h = random.randint(1, P - 1)
            xa = pow(h, R, P)
            if pow(xa, R, P) != 1 and xa < self.g:
                valid_xa = True

        with open(output_file_path, "w") as f:
            f.write(f"{xa}\n")

        with open(output_file_path, "w") as f:
            f.write(str(xa))

        ya = pow(self.a, xa, self.p)
        with open(f"./{self.param_path}/ya.txt", "w") as f:
            f.write(str(ya))
        print("Cặp khóa người gửi là (xa = {}; y_a = {})".format(xa, ya))

    def sender_XB(self):
        input_path = f"./{self.param_path}/PR.txt"
        output_path_xb = f"./{self.param_path}/xb.txt"
        output_path_yb = f"./{self.param_path}/yb.txt"

        with open(input_path, "r") as f:
            pairs = [ast.literal_eval(line.strip()) for line in f]

        valid_xb = False
        while not valid_xb:
            P, R = random.choice(pairs)
            h = random.randint(1, P - 1)
            xb = pow(h, R, P)

            if pow(xb, R, P) != 1 and xb != self.g and xb != self.x:
                valid_xb = True

        with open(output_path_xb, "w") as f:
            f.write(f"{xb}\n")
        yb = pow(self.a, xb, self.p)
        with open(output_path_yb, "w") as f:
            f.write(str(yb))
        print("Cặp khóa người gửi là (xb = {}; y_b = {})".format(xb, yb))

    def random_chain(self):
        iv = secrets.token_bytes(16)
        with open(f"./{self.param_path}/IV.txt", "wb") as f:
            f.write(iv)


class Sign:
    def __init__(self) -> None:
        self.x = None
        self.yb = None
        self.p = None
        # self.inp = ""

    def create_keys(self):
        x_file = f"./thamso/giatrix.txt"
        yb_file = f"./thamso/yb.txt"
        p_file = f"./thamso/P.txt"

        with open(x_file, "r") as f:
            self.x = int(f.read().strip())
        with open(yb_file, "r") as f:
            self.yb = int(f.read().strip())
        with open(p_file, "r") as f:
            # self.p = str(f.read().strip())
            self.p = int(f.read().strip())

        k1, k2 = calculate_hash(self.x, self.yb, self.p)

        with open(f"./thamso/k1.txt", "w") as f:
            f.write(k1)
        with open(f"./thamso/k2.txt", "w") as f:
            f.write(k2)

        # print("Tạo khóa k1, k2 thành công!")

    def encrypt(self, inp):
        with open(f"./thamso/k1.txt", "rb") as f:
            key = f.read()
        with open(f"./thamso/IV.txt", "rb") as f:
            iv = f.read()

        with open(inp, "r", encoding="UTF-8") as f:
            plaintext = f.read()

        cipher_text = encrypt_text(plaintext, key, iv)

        with open(f"./c.r.s/c.txt", "wb") as f:
            f.write(cipher_text)

        # print("Mã hóa thành công!")

    def calculate_signature_r(self, input_file):
        with open(f"./thamso/k2.txt", "r", encoding="utf-8") as f:
            value = f.read().strip()
            k2 = bytes.fromhex(value)

        with open(input_file, "r", encoding="utf-8") as f:
            plaintext = f.read().strip()

        r = hash_function(k2, plaintext)

        with open(f"./c.r.s/r.txt", "w", encoding="utf-8") as f:
            f.write(r)

        # print("Tính chữ kí r thành công!")

    def calculate_s(self):
        with open(f"./thamso/P.txt", "r") as f:
            P = int(f.read().strip())
        with open(f"./thamso/giatrix.txt", "r") as f:
            x = int(f.read().strip())
        with open("./thamso/xa.txt", "r") as f:
            x_a = int(f.read().strip())
            s = (x - x_a + P) % P
        with open(f"./c.r.s/s.txt", "w") as f:
            f.write(str(s))


class unSign:
    def __init__(self) -> None:
        pass

    # read values from files
    def read_values(self):
        with open(f"", "r") as f:
            a = int(f.read().strip())

# if __name__ == "__main__":
#     app = Parameter()
#     app.write_P()
#     print("P = ", app.P)
#     print("Q = ", app.Q)
#     print("R = ", app.R)
#     app.generate_matching_pair()
#     app.select_g()
#     app.select_a()
