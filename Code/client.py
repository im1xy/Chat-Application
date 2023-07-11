import os
import sys
from time import sleep

import socket as sk
import threading

from PySide6.QtWidgets import QApplication
from chat_GUI import Chat_GUI

import ctypes

lib = ctypes.CDLL('./CLogin.dll') # In the same directory or provide full path to the file (in C++ Login Form)

HOST = "192.168.0.42"
PORT = 9100


class Client_App(Chat_GUI):
    def __init__(self, host, port):
        self.server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.server_connection(host, port)
        self.username = self.login()  # C++ Login

        super().__init__(self.username, self.server)  # Initialize GUI

        self.server.send(self.username.encode('utf-8'))

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def server_connection(self, host, port):
        try:
            self.server.connect((host, port))
        except TimeoutError:  # If error is that client cannot connect to the server
            ctypes.windll.user32.MessageBoxW\
                (0, "Could not connect to the server. Try again Later.", "Connection Error", 16)
            sys.exit()
        except:  # Unknown Error
            ctypes.windll.user32.MessageBoxW\
                (0, "Something went wrong. Try again Later.", "Error", 16)
            sys.exit()

    def receive(self):
        while True:
            if self.ready:
                try:
                    self.handle_messages()
                except UnicodeDecodeError:  # When garbage or too much data received, it cannot be decoded
                    continue
                except:
                    self.ui.chat_viewer.append(
                        "SERVER: *** Something went wrong. You're disconnected from the server ***")
                    self.server.close()
                    break
            else:
                sleep(1)  # To make less comparisons, less loading

    def handle_messages(self):
        stream = self.server.recv(1024).decode('utf-8').split("$%$")  # decoding
        for item in stream:  # One stream can have multiple data
            msg_status = item[:4]
            message = item[4:]

            if msg_status == "CHAT":
                self.ui.chat_viewer.append(message)

            elif msg_status == "FILE":
                full_file_info = message.split("/")  # Information about file: client_who_sent/name/size

                send_user = full_file_info[0]
                file_name = full_file_info[1]
                file_size = full_file_info[2]
                file_size = self.file_sizes(file_size)

                self.ui.download_file_area.show()
                self.ui.file_info.setText(f"From User: {send_user}\nFile name: {file_name}\nSize: {file_size}")

                self.to_pass = full_file_info
                self.ready = False  # Stop receiving regular data and receive file data
                self.disable_all()  # Disable GUI

            elif msg_status == "LIST":
                self.ui.online_clients_list.clear()  # Clear Old Online Clients List
                for client in message[1:-1].split(", "):
                    self.ui.online_clients_list.addItem(client[1:-1])

    # C++ Login
    def login(self):
        file_path = os.path.expanduser('~')  # Getting USER folder
        file_path += "\\login_data.txt"

        try:
            lib.login()  # C++ function that creates file with username inside USER folder
            file = open(file_path, "r")
            username = file.read()
            file.close()

            os.remove(file_path)  # Deleting file
        except:
            sys.exit()  # If Login was Canceled
        return username

    # OTHER
    def file_sizes(self, file_size):  # Create string with right File Size
        if int(file_size) <= 1000:
            file_size += " B"
        elif 1000 <= int(file_size) <= 1000000:
            file_size = str(int(file_size) / 1000)
            file_size += " KB"
        else:
            file_size = str(int(file_size) / 1000000)
            file_size += " MB"

        return file_size


# MAIN
app = QApplication(sys.argv)
client = Client_App(HOST, PORT)
client.show()
app.exec()
