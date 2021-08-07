from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-like object for writing
            self.wfile.write(line)


# 创建一个预先分配大小的工作线程池或进程池(多线程最佳实践是使用线程池)
if __name__ == '__main__':
    from threading import Thread

    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    print('Multithreaded server running on port 20000')
    serv.serve_forever()
