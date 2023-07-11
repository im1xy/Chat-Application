import threading
import socket as sk

HOST = sk.gethostbyname(sk.gethostname())
PORT = 9100

server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []


def broadcast_to_all(message):
    for client in clients:
        client.send(message)


def broadcast_with_exception(file_data, exception):
    for client in clients:
        if client != exception:
            client.send(file_data)


def close_connection(client):
    index = clients.index(client)
    nickname = nicknames[index]

    print(f"Server: {nickname} left the server")

    clients.remove(client)
    client.close()
    nicknames.remove(nickname)

    broadcast_to_all(("$%$CHAT" + f"{nickname} left the chat!").encode('utf-8'))
    broadcast_to_all(("$%$LIST" + str(nicknames)).encode('utf-8'))


def handle(client):
    while True:
        try:
            handle_messages(client)
        except:
            close_connection(client)
            break


def handle_messages(client):
    stream = client.recv(1024).decode('utf-8')
    client_msg_status = stream[:5]
    message = stream[5:]

    if client_msg_status == "CHAT:":
        broadcast_to_all(("$%$CHAT" + message).encode('utf-8'))

    elif client_msg_status == "FILE:":
        full_file = message.split("/")  # Information about file: name/size
        file_name = full_file[0]
        file_size = full_file[1]

        file_data = client.recv(int(file_size))  # Receiving file
        index = clients.index(client)

        broadcast_with_exception(f"$%$FILE{nicknames[index]}/{file_name}/{file_size}".encode('utf-8'), client)
        broadcast_with_exception(file_data, client)


def receive():
    while True:
        client, address = server.accept()
        print(f"Server: Connected with {str(address)}")

        nickname = client.recv(1024).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        print(f"Server: Nickname of the client is {nickname}")

        broadcast_to_all(("$%$CHAT" + f"{nickname} joined the chat!").encode('utf-8'))
        broadcast_to_all(("$%$LIST" + str(nicknames)).encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))  # Thread that will take care of client
        thread.start()


# MAIN
print("Server is ready")
receive()
