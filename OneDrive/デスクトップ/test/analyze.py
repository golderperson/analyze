import hashlib
import itertools
import sys


x = input()
e= len(x)
md5 = hashlib.md5(x.encode()).hexdigest()


int_list = [chr(t) for t in range(32,127)] 
print(int_list)
if e== 32:
    for y in range(0,127):
        for pair in itertools.product(int_list, repeat=y):
            pair = "".join(pair)
            md51 = hashlib.md5(pair.encode()).hexdigest()
            print(pair)
            if x == md51:
                print(pair)
                sys.exit()
if e == 40:
    for y in range(0,127):
        for pair in itertools.product(int_list, repeat=y):
            pair = "".join(pair)
            sha12 = hashlib.sha1(pair.encode()).hexdigest()
            print(pair)
            if x == sha12:
                print(pair)
                sys.exit()
if e == 56:
    for y in range(0,127):
        for pair in itertools.product(int_list, repeat=y):
            pair = "".join(pair)
            sha2245 = hashlib.sha224(pair.encode()).hexdigest()
            print(pair)
            if x == sha2245:
                print(pair)
                sys.exit()
if e == 96:
    for y in range(0,127):
        for pair in itertools.product(int_list, repeat=y):
            pair = "".join(pair)
            sha3845 = hashlib.sha384(pair.encode()).hexdigest()
            print(pair)
            if x == sha3845:
                print(pair)
                sys.exit()
if e == 128:
    for y in range(0,127):
        for pair in itertools.product(int_list, repeat=y):
            pair = "".join(pair)
            sha5129= hashlib.sha512(pair.encode()).hexdigest()
            print(pair)
            if x == sha5129:
                print(pair)
                sys.exit()