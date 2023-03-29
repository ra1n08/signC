import random
from _math import is_prime
import secrets
import ast

class Parameter():
    def __init__(self, bit) -> None:

        self.Q = self.generate_prime(bit)
        self.R = random.getrandbits(20)
        self.P = self.cal_P()
        self.P_path = f"./thamso/P.txt"
        self.percent = 0
        self.g = None
        self.a = None
        self.p = None
        self.x = None
    
    def generate_prime(self, bit):
        Q = random.getrandbits(bit)
        while not is_prime(Q):
            Q = random.getrandbits(bit)
        return Q
    
    def cal_P(self):
        while True:
            P = self.Q * self.R + 1
            if is_prime(P):
                # print("P = ", P)
                return P
            else:
                self.Q = self.generate_prime(160)
                self.R = random.getrandbits(20)
                # pass
    
    def write_P(self):
        with open(self.P_path, "w") as f:
            f.write(str(self.P))
            
    def read_P(self):
        with open(self.P_path, "r") as f:
            self.p = int(f.read().strip())
        
    
    def generate_matching_pair(self):
        Q = self.generate_prime(160)
        with open(self.P_path, "w") as f:
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
        input_path = f"./thamso/PR.txt"
        out_path = f"./thamso/tapG.txt"
        with open(input_path, "r") as f:
            # pairs = [eval(line.strip()) for line in f]
            pairs = [ast.literal_eval(line.strip()) for line in f]
            
        valid_g = False
        while not valid_g:
            P, R = random.choice(pairs)
            
            h = random.randint(1, P-1)
            
            self.g = pow(h, R, P)
            
            if pow(self.g, R ,P) != 1:
                valid_g = True
                
        with open(out_path, "w") as f:
            f.write(f"{self.g}\n")
        x = self.g
        with open(f"./thamso/giatrix.txt", "w") as f:
            f.write(f"{x}\n")
        print("x = ", x)
        print("x saved successfully")
        
    def select_a(self):
        self.a = random.randint(2, 200)
        print("a = ", self.a)
        with open(f"./thamso/a.txt", "w") as f:
            f.write(str(self.a))
            
    def sender_XA(self):
        input_file_path = f"./thamso/PR.txt"
        output_file_path = f"./thamso/xa.txt"
        
        with open(input_file_path, "r") as f:
            pairs = [ast.literal_eval(line.strip()) for line in f]
            
        valid_xa = False
        while not valid_xa:
            P, R = random.choice(pairs)
            h = random.randint(1, P-1)
            xa = pow(h, R, P)
            if pow(xa, R, P) != 1 and xa < self.g:
                valid_xa = True
        
        with open(output_file_path, "w") as f:
            f.write(f"{xa}\n")
            
        with open(output_file_path, "w") as f:
            f.write(str(xa))
            
        ya = pow(self.a, xa, self.p)
        with open(f"./thamso/ya.txt", "w") as f:
            f.write(str(ya))
        print("Cặp khóa người gửi là (xa = {}; y_a = {})".format(xa, ya))
        
    def sender_XB(self):
        input_path = f"./thamso/PR.txt"
        output_path_xb = f"./thamso/xb.txt"
        output_path_yb = f"./thamso/yb.txt"
        
        with open(input_path, "r") as f:
            pairs = [ast.literal_eval(line.strip()) for line in f]
            
        valid_xb = False
        while not valid_xb:
            P, R = random.choice(pairs)
            h = random.randint(1, P-1)
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
        with open(f"./thamso/IV.txt", "wb") as f:
            f.write(iv)
              
                
# if __name__ == "__main__":
#     app = Parameter()
#     app.write_P()
#     print("P = ", app.P)
#     print("Q = ", app.Q)
#     print("R = ", app.R)
#     app.generate_matching_pair()
#     app.select_g()
#     app.select_a()
                
        
        