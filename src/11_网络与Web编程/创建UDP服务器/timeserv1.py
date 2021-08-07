from socketserver import BaseRequestHandler, UDPServer
import time

# 对于数据报的传送， 你应该使用socket的 sendto() 和 recvfrom() 方法。
# 尽管传统的 send() 和 recv() 也可以达到同样的效果， 但是前面的两个方法对于UDP连接而言更普遍。
# UDP天生是不可靠的（因为通信没有建立连接，消息可能丢失）。 因此需要由你自己来决定该怎样处理丢失消息的情况。
class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()
