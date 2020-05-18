from millionaire_general import *

with open("enc_B.txt", "r") as f:
    line = f.readlines()
    ln = line[0].split(",")
    data = []
    for i in range(len(ln)//2):
        data.append([int(ln[i*2]),int(ln[i*2+1])])

with open("key.txt", "r") as f:
    line = f.readlines()
    p = int(line[0])
    alpha = int(line[1])

mode = get_int("Please enter your mode (1 or 2): ", 1, 2)

if mode == 1:
    for i in range(len(data)):
        if dec(data[i], p, alpha) == 1:
            print("Side A is greater than side B.")
            exit(0)
    print("Side B is greater than or equal to side A.")

if mode == 2:
    if dec(data[0], p, alpha) == 1: print("Two strings are identical.")
    else: print("Two strings are different.")
