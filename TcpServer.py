from socket import *
import threading

#serverName = 'localhost'
serverPort = 6969
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print('The server is ready to receive')


def handleClient(connectionSocket, address):
 sentence = connectionSocket.recv(1024).decode()
 print(sentence)
 capitalizedSentence = sentence.upper()
 connectionSocket.send(capitalizedSentence.encode())
 connectionSocket.close()

while 1:
 connectionSocket, addr = serverSocket.accept()
 threading.Thread(target=handleClient, args = (connectionSocket, addr)).start()
