from socketserver import BaseRequestHandler,TCPServer,ThreadingTCPServer
import socket,struct,threading


class HwProtocolHandler(BaseRequestHandler):

    def _protocol_handler(self, rx_buf, buf_len):
        print(rx_buf+str(buf_len))



    def handle(self):
        while True:
            print('Got connection from', self.client_address)
            print("thread id={}".format(threading.current_thread()))
            rx_head = self.request.recv(struct.calcsize("35I"))
            p_type,p_ver,data_len,p_min_ver,p_err,seq_num, = struct.unpack("35I",rx_head)
            print("{} {} {} {} {} {}".format(p_type,p_ver,data_len,p_min_ver,p_err,seq_num))

            # self._protocol_handler(rx_buf, len(rx_buf))



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
