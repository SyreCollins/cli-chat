import sys
import socket
import threading

clients = []

def handle_client(clt):
    global clients
    clients.append(clt)
    print(f"Connected to {clt.getpeername()} successfully")
    clt.send(bytes("Built by @syrecollins, IG: _heiscollins", "utf-8"))
    while True:
        msg = clt.recv(1024)
        if not msg:
            break
        print("Received: " + msg.decode("utf-8"))

        for client in clients:
            if client != clt:
                client.send(msg)
    clt.close()
    clients.remove(clt)
    print("Connection closed")


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    while True:
        clt, adr = s.accept()
        thread = threading.Thread(target=handle_client, args=(clt,))
        thread.start()


def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    def receive_messages():
        while True:
            msg = s.recv(1024)
            if msg:
                print("Receive: " + msg.decode("utf-8"))

    def send_messages():
        while True:
            user_req = input("Send Text? y/n: ")
            if user_req == "y":
                client_message = input("Enter message: ")
                s.send(bytes(client_message, "utf-8"))
                print(f"Message sent.")
            else:
                print("checking new messages..")

    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cli-chat.py [server|client]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "server":
        start_server()
    elif command == "client":
        start_client()
    else:
        print("Invalid command. Use either 'server' or 'client'")
