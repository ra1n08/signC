import secrets
from _math import is_prime
# from sympy import isprime
import random
import time
import tqdm
# import math
# import os
start_time = time.time()
#  hàm kiếm tra số nguyên tố Miller-Rabin primality test.

def generate_prime():
    Q = random.getrandbits(160)
    while not is_prime(Q):
        Q = random.getrandbits(160)
    return Q

# tạo Q
Q = generate_prime()

#TẠO R
R = random.getrandbits(20)

while True:
    # calculate P
    P = Q * R + 1

    # kiếm tra tính nguyên tố
    if is_prime(P):
        print("P =", P)
        break
    else:
        # tạo lai Q r
        Q = generate_prime()
        R = random.getrandbits(20)
        
print("Q =", Q)       
print("R =", R)
with open(r"./thamso/P.txt", "w") as f: # mở p.txt và ghi chuỗi p vào tệp
    f.write(str(P))
   
with open(".//thamso//P.txt", "r") as file:
    p = int(file.read().strip()) # lấy giá trị P để tính g
 
# Define the values of Q
Q = generate_prime()

# Define the file path to write the matching pairs
file_path = r"./thamso/PR.txt"

# Open the file in write mode
with open(file_path, "w") as f:
    # Iterate over values of R from 1 to 100
    for R in range(1, 100000):
        # Calculate the value of P
        P = Q * R + 1
        # Check if P is prime
        if is_prime(P):
            # Write the matching pair (P, R) to the file
            f.write(f"({P}, {R})\n")
print('tao pr thành công')

input_file_path = r"./thamso/PR.txt"
output_file_path = r"./thamso/tapG.txt"

# Read the pairs (P, R) from the input file
with open(input_file_path, "r") as f:
    pairs = [eval(line.strip()) for line in f]

valid_g = False
while not valid_g:
    # Select a random pair (P, R)
    P, R = random.choice(pairs)

    # Choose a random value h from [1, P)
    h = random.randint(1, P-1)

    # Compute g = h^R mod P
    g = pow(h, R, P)

    # Check that g^R != 1 mod P
    if pow(g, R, P) != 1:
        valid_g = True

# Write the computed value of g to the output file
with open(output_file_path, "w") as f:
    f.write(f"{g}\n")

x = g
with open(r"./thamso/giatrix.txt", "w") as f:
    f.write(f"{x}\n")
print('x =', x)
print("x saved successfully")

# chọn ngẫu nhiên a sau đó in ra màn hình và lưu vào file a.txt
a = random.randint(2, 200) 
print("a =", a)
with open(r"./thamso/a.txt", "w") as f:
    f.write(str(a))
    
input_file_path = r"./thamso/PR.txt"
output_file_pathxa = r"./thamso/xa.txt"

# Read the pairs (P, R) from the input file
with open(input_file_path, "r") as f:
    pairs = [eval(line.strip()) for line in f]

valid_xa = False
while not valid_xa:
    # Select a random pair (P, R)
    P, R = random.choice(pairs)

    # Choose a random value h from [1, P)
    h = random.randint(1, P-1)

    # Compute g = h^R mod P
    xa = pow(h, R, P)

    # Check that g^R != 1 mod P
    if pow(xa, R, P) != 1 and xa <g:
        valid_xa = True

# Write the computed value of g to the output file
with open(output_file_pathxa, "w") as f:
    f.write(f"{xa}\n")

with open(r"./thamso/xa.txt", "w") as f:
    f.write(str(xa))
#tính khóa công khai của người gửi sau đó ghi vào ya.txt
y_a = pow(a, xa, p)
with open(r"./thamso/ya.txt", "w") as f:
    f.write(str(y_a))
print("Cặp khóa người gửi là (xa = {}; y_a = {})".format(xa, y_a))


input_file_path = r"./thamso/PR.txt"
output_file_pathxb = r"./thamso/xb.txt"

# Read the pairs (P, R) from the input file
with open(input_file_path, "r") as f:
    pairs = [eval(line.strip()) for line in f]

valid_xb = False
while not valid_xb:
    # Select a random pair (P, R)
    P, R = random.choice(pairs)

    # Choose a random value h from [1, P)
    h = random.randint(1, P-1)

    # Compute g = h^R mod P
    xb = pow(h, R, P)

    # Check that g^R != 1 mod P
    if pow(xb, R, P) != 1 and xb != g and xb != x:
        valid_xb = True

# Write the computed value of g to the output file
with open(output_file_pathxb, "w") as f:
    f.write(f"{xb}\n")

with open(r"./thamso/xb.txt", "w") as f:
    f.write(str(xb))
#tính khóa công khai của người gửi sau đó ghi vào ya.txt
y_b = pow(a, xb, p)
with open(r"./thamso/yb.txt", "w") as f:
    f.write(str(y_b))
print("Cặp khóa người gửi là (xb = {}; y_b = {})".format(xb, y_b))

#tạo ra một chuỗi ngẫu nhiên gồm 16 byte ( 128 bit) sử dụng làm vectơ khởi tạo (IV) trong AES-CBC
iv = secrets.token_bytes(16)
with open(r"./thamso/IV.txt", "wb") as f:
    f.write(iv)

print('Tạo tham số thành công')
print("Time elapsed: {:.2f} seconds".format(time.time() - start_time)) 


