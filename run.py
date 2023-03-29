from cypher_v2 import Parameter
import tqdm
import time
import sys

class main():
    def __init__(self) -> None:
        self.per = Parameter(bit=160)
    
    def run(self):
        # self.per.bit(160)
        self.per.write_P()
        self.per.read_P()
        print("P = ", self.per.P)
        print("Q = ", self.per.Q)
        print("R = ", self.per.R)
        for percent in self.per.generate_matching_pair():
            print(f"Progress: {percent:.2f}%", end="\r")
        print("tạo PR thành công")
        self.per.select_g()
        self.per.select_a()
        self.per.sender_XA()
        self.per.sender_XB()
        self.per.random_chain()
            
if __name__ == "__main__":
    app = main()
    runtime = time.time()
    app.run()
    print('Tạo tham số thành công')
    print("Time elapsed: {:.2f} seconds".format(time.time() - runtime)) 