from random import *
import json


def plus(a, b):
    return a + b


def save_file(name, pwd, age, flag):
    data = {
        'name': name,
        'pwd': pwd,
        'age': age,
        'flag': flag
    }
    json_str = json.dumps(data)
    print(json_str)
    f = open("config.json", "w")
    json.dump(data, f)
    f.close()


def load_file():
    f = open("config.json", "r")
    data = json.load(f)
    f.close()
    print("load "+str(data))


if __name__ == '__main__':
    num = 10
    while num > 0:
        num -= 1
        print("hello world2 {} ".format(randint(1, 10))+str(plus(2, 4)))
    myList = []
    myList.append(2)
    myList.append(0)
    myList.append(3)
    myList.append(0)
    myList.append("tmp")
    myList.append(True)
    try:
        myList.remove(0)
    except:
        print("error")
    finally:
        print("ok")
    print(myList)
    save_file("lala", "admin12345", 25, True)
    load_file()


