import socket

# server settings
HOST = '192.168.3.131'  # server ip address
PORT = 8080  # server port

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()
print("Server is listening on {}:{}".format(HOST, PORT))

while True:
    # establish a connection
    client_socket, addr = server_socket.accept()
    print("Connection from: {}".format(addr))

    # receive temperature in Fahrenheit
    temp_fahrenheit = client_socket.recv(1024).decode()
    print("Temperature in Fahrenheit: {}".format(temp_fahrenheit))

    # convert to Celsius
    temp_celsius = (float(temp_fahrenheit) - 32) * 5/9
    temp_celsius = round(temp_celsius, 2)
    print("Temperature in Celsius: {}".format(temp_celsius))

    # send temperature in Celsius back to client
    client_socket.sendall(str(temp_celsius).encode())

    # close the connection
    client_socket.close()
