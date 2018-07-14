
from socket import *

def main():
	
	serverSocket = socket(AF_INET, SOCK_STREAM)

	localAddr = ("",8080)

	serverSocket.bind(localAddr)

	serverSocket.listen(100)

	#将serverSocket设置成非堵塞
	serverSocket.setblocking(False)

	clients = []

	while True:
		
		try:
			clientSocket,clientAddr = sererSocket.accept()

		except:
			pass

		else:
			clientSocket.setblocking(False)
			clients.append((clientSocket,clientAddr))
	
		finally:
			pass

		for clientSocket, clientAddr in clients:
			content = clientSocket.recv(1024)
			if len(content) > 0:
				print("[%s]:%s"%(clientAddr, content.decode('utf-8')))
			else:
				cilentSocket.close()
				clients.remove((clientSocket,clientAddr))

if __name__ == "__main__":
	main()
