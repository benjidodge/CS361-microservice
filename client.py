import socket

print("Hello, Please enter the below information:")
income = input("Monthly net income: ")
time = input("Time period (number of months): ")
rate = input("Projected interest rate: ")
send = input("click 1 to send to microservice, or 2 to close: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 6060))
if send == "1":
    data = income + ";" + time + ";" + rate
    s.send(data.encode())
    total = s.recv(4096)
    print(f"total: {total.decode()}")
elif send == "2":
    pass
else:
    print("You entered an invalid option! oh well... closing anyways.")
