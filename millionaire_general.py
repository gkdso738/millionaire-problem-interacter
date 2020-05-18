import gmpy2
import random

def mul(a,b,p):
    res = []
    res.append(a[0] * b[0] % p)
    res.append(a[1] * b[1] % p)
    return res

def enc(x,g,h,p,q):
    r = random.randint(3,q-3)
    data = []
    val = gmpy2.powmod(g, r, p)
    data.append(val)
    val = x * gmpy2.powmod(h, r, p) % p
    data.append(val)
    return data

def dec(a,p,alpha):
    return gmpy2.powmod(a[0], alpha, p) * a[1] % p

def scal(a,p):
    r = random.randint(3,p//2-3)
    base = a
    res = [1,1]
    while r:
        if r%2: res = mul(res,base,p)
        base = mul(base,base,p)
        r //= 2
    return res

def gen_key():
    while True:
        q = int(random.getrandbits(1024))
        # optimize
        if q % 2 == 0 or q % 3 != 2 or q % 5 == 0 or q % 7 == 0:
            continue
        p = 2 * q + 1
        if gmpy2.is_prime(p) and gmpy2.is_prime(q):
            break
    g = random.randint(3,p-3)
    g = g * g % p
    alpha = random.randint(3,q-3)
    h = gmpy2.powmod(g, q-alpha, p)
    return p,q,g,h,alpha

def get_int(msg, l_bound, r_bound):
    while True:
        value = input(msg)
        try:
            value = int(value)
            if value < l_bound or value > r_bound:
                print("Invalid input. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    return value

def pad(st, target_length):
    while len(st) != target_length:
        st = st + "a"
    return st
