import socket

# client settings
HOST = '192.168.3.131'  # server IP address
PORT = 8080  # server port

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))

# get temperature in Fahrenheit from user input
temp_fahrenheit = input("Enter temperature in Fahrenheit: ")

# send temperature to server
client_socket.sendall(temp_fahrenheit.encode())

# receive temperature in Celsius from server
temp_celsius = client_socket.recv(1024).decode()

# print temperature in Celsius
print("Temperature in Celsius: {}".format(temp_celsius))

# close the connection
client_socket.close()
