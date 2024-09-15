import socket
import RPi.GPIO as GPIO
import time

etat = False
HOST, PORT = '', 8888
verif_var = 0

relay_pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, False)


def relay():
    global etat
    if etat:
        GPIO.output(relay_pin, False)
        etat = False
    else:
        GPIO.output(relay_pin, True)
        etat = True


def verif():
    global verif_var
    verif_var += 1
    if verif_var % 2 == 0:
        relay()


listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    verif()

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
