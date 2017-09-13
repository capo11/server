from tcpstream import *
import SimpleHTTPServer
import SocketServer


def build():
    print("PROVA DI ACCESSO ALLA CONFIGURAZIONE LOCALE")
    print("===========================================")
    print("LOCAL NAME: " + getLocalName())
    print("LOCAL DOMAIN: " + getLocalDomain())
    print("LOCAL IP: " + getLocalAddress())

    HOST = ""
    PORT = 8000

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()


build()
