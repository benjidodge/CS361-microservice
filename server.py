import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    message = clientSocket.recv(4096).decode()
    print(f"Inputs received: {message}")
    inputs = message.split(';')
    income, time, rate = float(inputs[0]), float(inputs[1]), float(inputs[2])
    total = str(round(income * (((pow((1 + rate / 100), time / 12)) - 1) / (rate / 100)), 2))
    print(f"Sending total: {total}")
    clientSocket.send(total.encode())
    clientSocket.close()
