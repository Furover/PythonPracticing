import socket

ports = [21, 22, 80, 8080, 443, 445, 3300, 25]

for port in ports:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    client.connect(("bancocn.com", port))
    client.send(b"hello world")
    response = client.recv(1024)
    print(response.decode())