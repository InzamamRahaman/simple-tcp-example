import TcpServer
import threading
import BlockList

# We inherit from our previously defined server
class ThreadedTcpServer(TcpServer.TcpServer):

    def __init__(self, port, host='', block_list=BlockList.BlockList()):
        """
        This is the constructor for the ThreadedTcpServer object
        :param host: the hostname for this server as a string. Default is empty string ('') to automatically set to localhost
        :param port: the port number for the server to receive connections
        :param block_list: the BlockList to be used to decide whether to process a client or not
        """
        # call the super-constructor
        super(ThreadedTcpServer, self).__init__(port, host, block_list)

    def process_client_socket(self, client_socket, client_addr):
        fun = self.handle_client
        if not self.block_list.block_client(client_addr):
            fun = self.reject_client
        # handles client on separate thread
        thread = threading.Thread(fun, (client_socket, client_addr))
        thread.start()
