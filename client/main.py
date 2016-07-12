import socket
import TcpClient
import ClientConfig
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'client_config.json')

if __name__ == '__main__':
    client_configuration = ClientConfig.ClientConfig(CONFIG_FILE)
    port = client_configuration.port
    host = client_configuration.host
    client = TcpClient.TcpClient(port, host)
    print 'Client connected.....'
    client.connect()