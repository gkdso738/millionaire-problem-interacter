import gmpy2
import random
from millionaire_general import *

def compute_result(x,p,bit_ln,mode):
    bit_arr = []
    for _ in range(bit_ln):
        bit_arr.append(x%2)
        x //= 2
    if x: raise Exception("Number too large")
    bit_arr.reverse()
    res = []
    if mode == 1:
        for i in range(bit_ln):
            if bit_arr[i] != 0:
                u = random.randint(3,p-3)
                v = random.randint(3,p-3)
                res.append([u * u % p, v * v % p])
            else:
                val = [1,1]
                for j in range(i):
                    val = mul(val, t[bit_arr[j]][j],p)
                val = mul(val, t[1][i], p)
                val = scal(val, p)
                res.append(val)
        return res
    if mode == 2:
        val = [1,1]
        for i in range(bit_ln):
            val = mul(val, t[bit_arr[i]][i],p)
        val = scal(val, p)
        res.append(val)
        return res

def print_result(res):
    with open("enc_B.txt", "w") as f:
        for i in range(len(res)):
            if i: f.write(",")
            f.write(str(int(res[i][0])) + ",")
            f.write(str(int(res[i][1])))
        f.write('\n')

t = [[],[]]
mode = get_int("Please enter your mode (1 or 2): ", 1, 2)
with open("enc_A.txt","r") as f:
    line = f.readlines()
    p = int(line[0])
    ln = line[1].split(',')
    for i in range(len(ln)//2):
        t[0].append([int(ln[i*2]),int(ln[i*2+1])])
    ln = line[2].split(',')
    for i in range(len(ln)//2):
        t[1].append([int(ln[i*2]),int(ln[i*2+1])])

if mode == 1:
    bit_ln = get_int("Please enter maximum bit length (max 2000): ", 1, 2000)
    x = get_int("Please enter your number: ", 0, (2**bit_ln)-1)
    res = compute_result(x,p,bit_ln,1)
    random.shuffle(res)
    print_result(res)

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
    res = compute_result(x,p,bit_ln,2)
    random.shuffle(res)
    print_result(res)
