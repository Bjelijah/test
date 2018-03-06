import os,struct,time

from threading import Thread
from ctypes import *
import types
MAX_HANDLE_LEN = 6


class HwMediaInfo(Structure):
    _fields_ = [
        ("media_fourcc", c_uint),
        ("dvr_version", c_long),
        ("vdec_code", c_long),
        ("adec_code", c_long),
        ("au_bits", c_ubyte),
        ("au_sample", c_ubyte),
        ("au_channel", c_ubyte),
        ("reserve", c_ubyte),
        ("reserved", 5*c_ubyte)
    ]


class StreamHead(Structure):

    _fields = [
        ("len", c_long),
        ("type", c_long),
        ("time_stamp", c_ulonglong),
        ("tag", c_long),
        ("sys_time", c_long)
    ]


class FileUtil:
    def __init__(self, file_path):
        self._running = False
        self._filePath = file_path
        self._handles = []

    def init_play(self):
        self._running = True
        for i in range(MAX_HANDLE_LEN):
            self._handles.append(-1)
            print("handle = "+str(self._handles[i]))

    def run(self):
        f = open(self._filePath, "rb")
        info = f.read(40)
        mf,dv,vc,ac,ab,a_s,ac,res,r1,r2,r3,r4,r5 = struct.unpack("IlllBBBB5I", info)
        eof = os.fstat(f.fileno()).st_size

        print("{} {} {} {} {} {} {} {}".format(hex(mf),dv,vc,ac,ab,a_s,ac,res))
        while self._running:
            stream_head = f.read(struct.calcsize("2lQ2l"))
            if(f.tell() == eof | f.tell()+struct.calcsize("2lQ2l")>eof):
                f.seek(40)
            # print("len="+str(stream_head))
            sh_len, sh_type, sh_time_stamp, sh_tag, sh_sys_time = struct.unpack("2lQ2l", stream_head)
            print("{} {} {} {} {}  ".format(sh_len,sh_type,sh_time_stamp,hex(sh_tag),sh_sys_time))
            buf_len = sh_len - struct.calcsize("2lQ2l")
            buf = f.read(buf_len)

            # time.sleep(0.04)
        f.close()


def file_util_main():
    fu = FileUtil("D:/work/file/tmp.mp4")
    fu.init_play()
    t = Thread(target=fu.run())

