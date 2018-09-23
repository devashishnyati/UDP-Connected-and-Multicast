from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class ConnectedUDPServer(DatagramProtocol):

    def startProtocol(self):
        host = '127.0.0.1'
        port = 8001
        self.transport.connect(host, port)
        print('Server connected')
        
    def datagramReceived(self, data, addr):
        print('Received data: {} from {}'.format(data.decode('utf-8'),addr))
        self.transport.write(data)

reactor.listenUDP(8000, ConnectedUDPServer())
reactor.run()