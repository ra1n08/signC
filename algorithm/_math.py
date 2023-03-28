import random

def modPrimePow(a=int, b=int, p=int):
    ret = 1
    a %= p
    b %= p - 1
    while b > 0:
        if b % 2 > 0:
            ret = (ret * a) % p
        a = (a * a) % p
        b //= 2
    return ret

def is_prime(n, k=10):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    # tìm d và s thỏa d * 2^s = n - 1
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        t = random.randint(2, n - 2)
        x = pow(t, d, n)
        if x == 1 or x == n - 1:
            continue

        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
        
        return True
    
