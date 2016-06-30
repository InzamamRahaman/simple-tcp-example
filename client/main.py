import socket
import TcpClient

if __name__ == '__main__':
    port = 12345
    host = socket.gethostname()
    client = TcpClient.TcpClient(port, host)
    print 'Client connected.....'
    client.connect()