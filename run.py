from cypher_v2 import Parameter, Sign, unSign
import tqdm
import time
import sys


class main:
    def __init__(self) -> None:
        self.param = Parameter(bit=160)
        self.sign = Sign()
        self.unSign = unSign()

    def run_param(self):
        # self.per.bit(160)
        self.param.write_P()
        self.param.read_P()
        print("P = ", self.param.P)
        print("Q = ", self.param.Q)
        print("R = ", self.param.R)
        for percent in self.param.generate_matching_pair():
            print(f"Đang tạo (P, R) {percent:.2f}%", end="\r")
        print("Tạo (P,R) thành công")
        self.param.select_g()
        self.param.select_a()
        self.param.sender_XA()
        self.param.sender_XB()
        self.param.random_chain()
        print("Tạp tham số thành công, yey :33")

    def run_sign(self, inp):
        self.sign.create_keys()
        print("Tạo khóa k1, k2 thành công!")
        self.sign.encrypt(inp=inp)
        print("Mã hóa thành công!")
        self.sign.calculate_signature_r(input_file=inp)
        print("Tính chữ kí r thành công!")
        self.sign.calculate_s()
        print("Tính s thành công!")


if __name__ == "__main__":
    app = main()
    runtime = time.time()
    app.run_param()
    app.run_sign(f"./input/input.txt")
    print("Thời gian thực hiện: {:.2f} seconds".format(time.time() - runtime))
