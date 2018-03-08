from socketserver import BaseRequestHandler,TCPServer,ThreadingTCPServer
import socket,struct,threading
from HwBean import *
from Log import *


class HwProtocolHandler(BaseRequestHandler):

    def _send(self, head, body, body_len):
        head.proVersion = 1
        head.dataLen = body_len
        head.err = 0
        self.request.sendall(struct.pack(ProtocolHead,head))
        self.request.sendall(body)

    def _do_login(self, head, body):
        print( "we login len={}   body len={}".format(head.dataLen, TLogin.get_size()))
        log_info = TLogin.from_buf(body)
        name = ''
        for x in log_info.logName:
            name += bytes.decode(x)
        print(name)
        self._send(head, struct.pack("i", 0), struct.calcsize("i"))



    def _protocol_handler(self, head, body):
        print("protocol type={}   len={}".format(hex(head.proType), head.dataLen))
        return {
            HW_PROTOCOL_LOGIN: self._do_login(head, body)
        }.get(head.proType)

    def handle(self):
        while True:
            print('Got connection from', self.client_address)
            print("thread id={}".format(threading.current_thread()))
            try:
                head_buf = self.request.recv(ProtocolHead.get_size())
            except Exception as e:
                print(e)
                break
            rx_head = ProtocolHead.from_buf(head_buf)
            rx_buf = self.request.recv(rx_head.dataLen)
            self._protocol_handler(rx_head, rx_buf)







def protocol_server_main():
    print("thread id={}".format(threading.current_thread()))
    serv = ThreadingTCPServer(("", 5198), HwProtocolHandler, bind_and_activate=False)
    # serv = ThreadingTCPServer(("", 5198), HwProtocolHandler)
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 256*1024)
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, struct.pack("ll", 5, 0))
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, struct.pack("ll", 5, 0))
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    serv.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    serv.server_bind()
    serv.server_activate()
    serv.serve_forever()
