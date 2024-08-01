import socket

def send(soc, ix):
    if ix == 'exit':
        exit()
    soc.sendall(ix.encode())
    data = " "
    data = soc.recv(1024)
    print(data.decode("utf-8"))

def run(soc):
    while True:
        ix = input()
        send(soc,ix)


def main():
    host = '127.0.0.1'
    port = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        send(s, "load solved/easy.bin")
        run(s)

if __name__ == "__main__":
    main()
