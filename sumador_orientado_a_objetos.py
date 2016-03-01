#!/usr/bin/python

#Saray Moratino Sousa

import socket

class webApp:
	def parse(self, request):
		"""Parse the received request, extracting the relevant information."""
		
		return None
        
	def process(self, parsedRequest):
		"""Process the relevant elements of the request.
		Returns the HTTP code for the reply, and an HTML page."""
		
		return ("200 OK", "<html><body><h1>It works!</h1></body></html>")
			
	def recortar(self, request):
		numero = int(request.split()[1][1:])
		return numero
		
	def suma(self, numero1, numero2):
		 suma = numero1 + numero2
		 return suma
          
	def __init__ (self, hostname, port):
		"""Initialize the web application."""
		#Create a TCP objet socket and bind it to a port
		mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		mySocket.bind((hostname, port))
		# Queue a maximum of 5 TCP connection requests
		mySocket.listen(5)

		# Accept connections, read incoming data, and call
		# parse and process methods (in a loop)
		num1 = None	
		num2 = None
		while True:
			print 'Waiting for connections'
			(recvSocket, address) = mySocket.accept()
			print 'HTTP request received (going to parse and process):'
			request = recvSocket.recv(2048)
			print request
			parsedRequest = self.parse(request)
			(returnCode, htmlAnswer) = self.process(parsedRequest)
			if (num1 == None):
				try:
					num1 = self.recortar(request)
				except ValueError:
					recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + 
									"<html><body>"+'Fallo'+"</html></body>" + "\r\n")
					recvSocket.close()
					continue
				recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body><h1>Primer numero introducido: " 
							+ str(num1) + '<p><h4>''otro numero mas..''</h4><p>' + "</h1></body></html>" + "\r\n")
				recvSocket.close()
			else:
				try:
					num2 = self.recortar(request)
				except ValueError:
					recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + 
									"<html><body>"+'Fallo'+"</html></body>" + "\r\n")
					recvSocket.close()
					continue
				resultadoSuma = self.suma(num1, num2)
				print 'Suma:', resultadoSuma
				print 'Answering back...'
				recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body><h3>Segundo numero introducido: " 
							+ str(num2) + 
							"<p>"'la suma es: ' 
							+ str(num1) + "+" + str(num2) + "="
							+ str(resultadoSuma) + "<p>""</h1></body></html>" + "\r\n")
				recvSocket.close()	
				num1 = None
				num2 = None				

if __name__ == "__main__":
	testWebApp = webApp("localhost", 1234) 	
