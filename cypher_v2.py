import random
from _math import is_prime
import secrets
import time
import tqdm
import os
import sys

class Parameter():
    def __init__(self) -> None:
        self.Q = self.generate_prime(160)
        self.R = random.getrandbits(20)
        self.P = self.cal_P()
        self.P_path = f"./thamso/P.txt"
    
    def generate_prime(self, bit):
        Q = random.getrandbits(bit)
        while not is_prime(Q):
            Q = random.getrandbits(bit)
        return Q
    
    def cal_P(self):
        while True:
            P = self.Q * self.R + 1
            if is_prime(P):
                print("P = ", P)
                return P
            else:
                self.Q = self.generate_prime(160)
                self.R = random.getrandbits(20)
                pass
    
    def write_P(self):
        with open(self.P_path, "w") as f:
            f.write(str(self.P))
    
    def generate_mathching_pair(self):
        Q = self.generate_prime(160)
        with open(self.P_path, "w") as f:
            for R in range(1, 100000):
                # calculate the value of P
                P =Q * R + 1
                # check if P is prime
                if is_prime(P):
                    # write the matching pair to file
                    f.write(f"({P}, {R})\n")
                    
    def select_g(self):
        input_path = f"./thamso/PR.txt"
        out_path = f"./thamso/tapG.txt"
        with open(input_path, "r") as f:
            pairs = [eval(line.strip()) for line in f]
            
        valid_g = False
        while not valid_g:
            P, R = random.choice(pairs)
            
            h = random.randint(1, P-1)
            
            g = pow(h, R, P)
            
            if pow(g, R ,P) != 1:
                valid_g = True
                
        with open(out_path, "w") as f:
            f.write(f"{g}\n")
        x = g
        with open(f"./thamso/giatrix.txt", "w") as f:
            f.write(f"{x}\n")
        print("x = ", x)
        print("x saved successfully")
        
    def select_a(self):
        a = random.randint(2, 200)
        print("a = ", a)
        with open(f"./thamso/a.txt", "w") as f:
            f.write(str(a))
                
                
if __name__ == "__main__":
    app = Parameter()
    app.write_P()
    print("Q = ", app.Q)
    print("R = ", app.R)
    app.generate_mathching_pair()
    app.select_g()
    app.select_a()
                
        
        