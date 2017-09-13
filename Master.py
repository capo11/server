import os.path
import shutil
import urllib2
from datetime import *
import socket
import SimpleHTTPServer
import SocketServer


HOST = "prova.it"
PORT = 8000

allowed_hosts = (('185.20.66.26', 8000),)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print(hostname)
print(IP)

'''
ipMio = getLocalAddress()
ipHost = dirsolve(name)
print ipHost
print ipMio'''

httpd.serve_forever()

net = tcpStream()
net.open(HOST, PORT)

ipHost = dirsolve(name)
ipMio = getLocalAddress()

print ipHost
print ipMio

if(ipMio != ipHost):
    print 'sono diversi'
else:
    print 'sono uguali'

response = urllib2.urlopen()
print response

header = response.info()
print 'Data: ', header['date']
print 'Header: ', header

data = response.read()
print 'Dati: '

print 'Url: ', pathname2url(path)
print 'Percorso: ', url2pathname('/d/e/f')
