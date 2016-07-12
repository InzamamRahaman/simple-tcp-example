
import TcpServer
import ThreadedTcpServer
import ServerConfig
import os

# os.path.dirname(__file__) gets the current directory of this file
# os.path.join is a function that joins the strings to form a correct file path
CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'server_config.json')

if __name__ == '__main__':
    config = ServerConfig.ServerConfig(CONFIG_FILE)
    server = None # None is the Python equivalent to null
    if config.use_multithreaded:
        server = ThreadedTcpServer.ThreadedTcpServer(config.port, config.host, config.block_list)
    else:
        server = TcpServer.TcpServer(config.port, config.host, config.block_list)
    server.listen()