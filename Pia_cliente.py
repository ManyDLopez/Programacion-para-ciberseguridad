import socket
import sys
servidor = ('192.168.1.91', 49669)
bufferSize = 2000
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while(True):
    pregunta = "Espere......."
    if pregunta == "bye":
        UDPClientSocket.close()
        sys.exit()
    UDPClientSocket.sendto(str.encode(pregunta), servidor)
    mensaje = UDPClientSocket.recvfrom(bufferSize)
    respuesta = "Respuesta: " + mensaje[0].decode()
    print(respuesta)
