
import socket
import TcpServer
import ThreadedTcpServer

use_multithreaded = False

if __name__ == '__main__':
    port = 12345
    host = socket.gethostname()
    server = None # None is the Python equivalent to null from Java
    if use_multithreaded:
        server = ThreadedTcpServer.ThreadedTcpServer(port, host)
    else:
        server = TcpServer.TcpServer(port, host)
    server.listen()