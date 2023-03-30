from cypher_v2 import Parameter, Sign, unSign
import tqdm
import time
import sys

class main():
    def __init__(self) -> None:
        self.param = Parameter(bit=160)
        self.sign = Sign()
        self.unSign = unSign()
    
    def run(self):
        # self.per.bit(160)
        self.param.write_P()
        self.param.read_P()
        print("P = ", self.param.P)
        print("Q = ", self.param.Q)
        print("R = ", self.param.R)
        for percent in self.param.generate_matching_pair():
            print(f"Progress: {percent:.2f}%", end="\r")
        print("tạo PR thành công")
        self.param.select_g()
        self.param.select_a()
        self.param.sender_XA()
        self.param.sender_XB()
        self.param.random_chain()

        self.sign.run("#", "#")
        self.unSign.run("#", "#")
            
if __name__ == "__main__":
    app = main()
    runtime = time.time()
    app.run()
    print('Tạo tham số thành công')
    print("Time elapsed: {:.2f} seconds".format(time.time() - runtime)) 