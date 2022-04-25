from copyreg import pickle
from numpy import random
import numpy as np
import pickle as p


def write_to_b():
    with open("task1.bin", "wb") as f:
            x = random.randint(100, size = 20)
            p.dump(" ".join(str(a) for a in x), f)
            f.close()
    print(x)
    print("Vector is ready")


def read_b():
    try:
        with open("task1.bin", "rb") as f:
            x = p.load(f).split(" ")
        print(x)
    except:
        print("No byte file")


def add_value(value):
    try:
        with open("task1.bin", "rb") as f:
            x = p.load(f).split(" ")
            x.append(value)
        
        with open("task1.bin", "wb") as f:
            p.dump(" ".join(str(a) for a in x), f)
            f.close()
        print(x)
        print("Value added")
    except:
        print("No byte file")


def remove_value(value):
    try:
        print(str(value))
        with open("task1.bin", "rb") as f:
            x = p.load(f).split(" ")
            vector = list(filter(lambda x: (x != str(value)), x))
        
        with open("task1.bin", "wb") as f:
            p.dump(" ".join(str(a) for a in vector), f)
            f.close()
        print(vector)
        print("Value removed")
    except:
        print("No byte file")

def replace_values(value, replace):
    try:
        with open("task1.bin", "rb") as f:
            x = p.load(f).split(" ")
            vector = list(map(lambda x: (replace if x == str(value) else x), x))
        
        with open("task1.bin", "wb") as f:
            p.dump(" ".join(str(a) for a in vector), f)
            f.close()
        print(vector)
        print("Value replaced")
    except:
        print("No byte file")



#__main__
dtype = np.dtype('B')
with open("task1.txt", "wt") as f:
    x = random.randint(100, size = 20)
    f.write(" ".join(str(a) for a in x))
    f.close()
print("Vector in the text file:", x)
while True: 
    print("""Choose option:\n
        1. write new vector to binary file\n
        2. view vector from binary file\n
        3. add value to the vector(binary)\n
        4. remove value from vector(binary)\n
        5. replace values in binary file\n
        0. exit""")
    mode = int(input("Type here: "))
    match mode:
        case 0:
            break
        case 1:
            write_to_b()
        case 2:
            read_b()
        case 3:
            n = int(input("Enter value to insert: "))
            add_value(n)
        case 4:
            n = int(input("Enter value to remove: "))
            remove_value(n)
        case 5:
            n = int(input("Enter value to replace: "))
            k = int(input("Enter new value: "))
            replace_values(n, k)
        case default:
            print("Wrong option")
    
