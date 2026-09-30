import socket
from cipher import encrypt, decrypt

HOST = "127.0.0.1"
PORT = 5001
KEY = "rahasiya"

def sendmsg(sock, data):
    sock.sendall(len(data).to_bytes(4, "big") + data)

def recvmsg(sock):
    header = sock.recv(4)
    if not header:
        return None

    size = int.from_bytes(header, "big")
    data = b""
    while len(data) < size:
        data += sock.recv(size - len(data))
    return data

def main():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    print(f"connected to {HOST}:{PORT}")

    while True:
        msg = input("send: ")
        if msg.lower() == "quit":
            break

        ct = encrypt(msg, KEY)
        sendmsg(sock, ct)
        print(f"ciphertext sent: {ct.hex()}")

        reply = recvmsg(sock)
        if not reply:
            print("connection closed")
            break

        print(f"ciphertext received: {reply.hex()}")
        print(f"plaintext: {decrypt(reply, KEY)}")

    sock.close()

if __name__ == "__main__":
    main()
