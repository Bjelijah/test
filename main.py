from random import *
import json,time

from RTSPClient import main
from FileUtil import file_util_main
from ProtocolServer import protocol_server_main
import array
def plus(a, b):
    return a + b


def save_file(name, pwd, age, flag):
    data = {
        'url': 'rtsp://184.72.239.149/vod/mp4://BigBuckBunny_175k.mov:554',
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


def file_test():
    file_util_main()


def server_test():
    protocol_server_main()


if __name__ == '__main__':

    save_file("lala", "admin12345", 25, True)
    url = load_file()
    print(url)
    # file_test()
    # main(url)
    # while True:
    #     print("sleep")
    #     time.sleep(1)
    server_test()


    # tmp = (b'a', b'd', b'm', b'i', b'n')
    #
    # for x in tmp:
    #     y = bytes.decode(x)
    #     print("{} {}".format(x, y))
    # print("{}".format(tmp[0]))
    # # str(tmp, 'utf-8')
    # test = b'a', b'b'
    # print("{}".format(test))