import os,struct,time

from threading import Thread
from ctypes import *
from HwBean import *
import types
MAX_HANDLE_LEN = 6







class FileUtil:
    def __init__(self, file_path):
        self._running = False
        self._filePath = file_path
        self._handles = []

    def init_play(self):
        self._running = True
        for i in range(MAX_HANDLE_LEN):
            self._handles.append(-1)
            # print("handle = "+str(self._handles[i]))

    def run(self):
        f = open(self._filePath, "rb")
        info = f.read(40)
        media_info = HwMediaInfo.from_buf(info)
        print("{}  {}".format(hex(media_info.media_fourcc),HwMediaInfo.get_size()))
        # print("{} {} {} {} {} {} {} {}".format(hex(media_info.), dv, vc, ac, ab, a_s, ac, res))
        # mf,dv,vc,ac,ab,a_s,ac,res,r1,r2,r3,r4,r5 = struct.unpack("IlllBBBB5I", info)
        # eof = os.fstat(f.fileno()).st_size
        # print("{} {} {} {} {} {} {} {}".format(hex(mf),dv,vc,ac,ab,a_s,ac,res))
        while self._running:
            try:
                stream_head = f.read(StreamHead.get_size())
                sh = StreamHead.from_buf(stream_head)
                # stream_head = f.read(struct.calcsize("2lQ2l"))
                # sh_len, sh_type, sh_time_stamp, sh_tag, sh_sys_time = struct.unpack("2lQ2l", stream_head)
                # buf_len = sh_len - struct.calcsize("2lQ2l")
                buf_len = sh.len - StreamHead.get_size()
                buf = f.read(buf_len)
                time.sleep(0.04)
            except Exception:
                f.seek(40)
                continue
        f.close()


def file_util_main():
    fu = FileUtil("D:/work/file/tmp.mp4")
    fu.init_play()
    t = Thread(target=fu.run())

