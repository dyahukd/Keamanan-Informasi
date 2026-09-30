import socket
from cipher import encrypt, decrypt

HOST = "0.0.0.0"
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
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"waiting for sender on port {PORT}...")
    conn, addr = server.accept()
    print(f"connected with {addr}")

    while True:
        ct = recvmsg(conn)
        if not ct:
            print("sender disconnected")
            break

        print(f"ciphertext received: {ct.hex()}")
        print(f"plaintext: {decrypt(ct, KEY)}")

        msg = input("reply: ")
        if msg.lower() == "quit":
            break

        out = encrypt(msg, KEY)
        sendmsg(conn, out)
        print(f"ciphertext sent: {out.hex()}")

    conn.close()
    server.close()

if __name__ == "__main__":
    main()
