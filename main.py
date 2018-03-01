from random import *
import json,time

from RTSPClient import main


def plus(a, b):
    return a + b


def save_file(name, pwd, age, flag):
    data = {
        'url': 'rtsp://192.168.2.100:8554/vlc',
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
    # print("load "+str(data))
    return data['url']


if __name__ == '__main__':

    save_file("lala", "admin12345", 25, True)
    url = load_file()
    print(url)
    main(url)
    while True:
        print("sleep")
        time.sleep(1)

