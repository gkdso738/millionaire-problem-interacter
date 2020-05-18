import gmpy2
import random
from millionaire_general import *

def create_table(x,bit_ln):
    t = [[],[]]
    for _ in range(bit_ln):
        b = x%2
        t[b].append(enc(1,g,h,p,q))
        t[b^1].append(enc(random.randint(3,p-3),g,h,p,q))
        x //= 2
    # Previous range check may have floating point error
    if x: raise Exception("Number too large")
    t[0].reverse()
    t[1].reverse()
    return t

def print_key(p,alpha):
    with open("key.txt", "w") as f:
        f.write(str(p) + "\n")
        f.write(str(alpha) + "\n")

def print_table(t):
    with open("enc_A.txt", "w") as f:
        f.write(str(p) + "\n")
        for i in range(bit_ln):
            if i: f.write(",")
            f.write(str(int(t[0][i][0])) + ",")
            f.write(str(int(t[0][i][1])))
        f.write('\n')
        for i in range(bit_ln):
            if i: f.write(",")
            f.write(str(int(t[1][i][0])) + ",")
            f.write(str(int(t[1][i][1])))
        f.write('\n')

print("Generating key...")
p,q,g,h,alpha = gen_key()
mode = get_int("Please enter your mode (1 or 2): ", 1, 2)

if mode == 1:
    bit_ln = get_int("Please enter maximum bit length (max 2000): ", 1, 2000)
    x = get_int("Please enter your number: ", 0, (2**bit_ln)-1)
    t = create_table(x,bit_ln)
    print_key(p,alpha)
    print_table(t)

if mode == 2:
    str_ln = get_int("Please enter maximum string length (max 1000): ", 1, 1000)
    bit_ln = str_ln * 8
    while True:
        st = input("Please enter your string: ")
        if len(st) > str_ln:
            print("Invalid input. Try again.")
        else: break
    st = pad(st, str_ln)
    x = 0
    for i in range(len(st)):
        x = x * 256 + ord(st[i])
    t = create_table(x,bit_ln)
    print_key(p,alpha)
    print_table(t)
