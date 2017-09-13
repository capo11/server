import os.path
import shutil
import urllib2
from datetime import *
import socket
import SimpleHTTPServer
import SocketServer


HOST = "prova.it"
PORT = 8000

allowed_hosts = '192.168.1.182'

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print(hostname)
print(IP)
print(allowed_hosts)

if(IP != allowed_hosts):
    print 'non puoi accedere a questo sito'
else:
    print 'puoi accedere'
    httpd.serve_forever()
