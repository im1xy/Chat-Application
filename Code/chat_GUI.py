import os
from emoji import emojize

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent

from app import Ui_MainWindow


class Chat_GUI(QMainWindow):
    def __init__(self, username, server):
        super(Chat_GUI, self).__init__()
        self.setFixedSize(550, 440)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Main Components
        self.set_ui()  # Additional Settings

        self.username = username
        self.server = server
        self.to_pass = None  # Useful variable to pass data to From Client to GUI
        self.ready = True  # Variable to stop receiving when needed

    # GUI METHODS
    def send_message(self):
        message = f"CHAT:{self.username}: {self.ui.chat_input.toPlainText()}"
        self.server.send(message.encode('utf-8'))
        self.ui.chat_input.clear()

    def send_file(self):
        full_path = QFileDialog.getOpenFileName(self, "Select File", os.getcwd())

        # If user decided to cancel
        try:
            p_file = open(full_path[0], "rb")
        except:
            return

        file_size = os.path.getsize(full_path[0])
        file_path, file_name = os.path.split(full_path[0])

        self.server.send(f"FILE:{file_name}/{file_size}".encode('utf-8'))

        data = p_file.read()
        self.server.sendall(data)

        p_file.close()

    def accept_download_file(self):
        file_name = self.to_pass[1]
        file_size = self.to_pass[2]

        full_path = QFileDialog.getSaveFileName(self, "Save File", os.getcwd() + f"/{file_name}")  # Where to save file

        file_data = self.server.recv(int(file_size))

        file = open(full_path[0], "wb")
        file.write(file_data)
        file.close()

        self.ready_to_recv()  # Ready to receive new regular data

    def add_emoji(self, emoji_text):
        self.ui.chat_input.insertPlainText(emojize(emoji_text))

    def close_menu(self):
        self.ui.online_clients_area.hide()
        self.ui.menu_area.hide()

    def scroll_to_bottom(self):  # Chat Viewer Always at the bottom, to see new messages
        self.ui.chat_viewer.verticalScrollBar().setValue(self.ui.chat_viewer.verticalScrollBar().maximum())

    def closeEvent(self, event: QCloseEvent):  # GUI closed
        self.server.close()

    def set_ui(self):
        # AREAS
        self.ui.menu_area.hide()
        self.ui.emoji_area.hide()
        self.ui.online_clients_area.hide()
        self.ui.download_file_area.hide()

        # SCROLLBAR
        self.ui.chat_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.chat_viewer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.chat_viewer.verticalScrollBar().rangeChanged.connect(self.scroll_to_bottom)

        # BUTTONS
        # MENU
        self.ui.menu_open_button.clicked.connect(self.ui.menu_area.show)
        self.ui.menu_close_button.clicked.connect(self.close_menu)

        # HISTORY
        self.ui.online_clients_open_button.clicked.connect(self.ui.online_clients_area.show)
        self.ui.online_clients_close_button.clicked.connect(self.ui.online_clients_area.hide)

        # FILE
        self.ui.download_button.clicked.connect(self.accept_download_file)
        self.ui.cancel_download_button.clicked.connect(self.ready_to_recv)

        # SEND
        self.ui.file_send_button.clicked.connect(self.send_file)
        self.ui.send_button.clicked.connect(self.send_message)

        # EMOJIS
        self.ui.emoji_open_button.clicked.connect(self.ui.emoji_area.show)
        self.ui.emoji_close_button.clicked.connect(self.ui.emoji_area.hide)

        emoji_buttons = \
            [self.ui.emoji_1, self.ui.emoji_2, self.ui.emoji_3, self.ui.emoji_4, self.ui.emoji_5, self.ui.emoji_6,
             self.ui.emoji_7, self.ui.emoji_8, self.ui.emoji_9,
             self.ui.emoji_10, self.ui.emoji_11, self.ui.emoji_12, self.ui.emoji_13, self.ui.emoji_14, self.ui.emoji_15,
             self.ui.emoji_16, self.ui.emoji_17, self.ui.emoji_18,
             self.ui.emoji_19, self.ui.emoji_20, self.ui.emoji_21, self.ui.emoji_22, self.ui.emoji_23, self.ui.emoji_24,
             self.ui.emoji_25, self.ui.emoji_26, self.ui.emoji_27,
             self.ui.emoji_28, self.ui.emoji_29, self.ui.emoji_30, self.ui.emoji_31, self.ui.emoji_32, self.ui.emoji_33,
             self.ui.emoji_34, self.ui.emoji_35, self.ui.emoji_36,
             self.ui.emoji_37, self.ui.emoji_38, self.ui.emoji_39, self.ui.emoji_40, self.ui.emoji_41, self.ui.emoji_42,
             self.ui.emoji_43, self.ui.emoji_44, self.ui.emoji_45]

        for emoji_button in emoji_buttons:
            emoji_button.clicked.connect(lambda x=None, text=emoji_button.text(): self.add_emoji(text))

        for emoji_button in emoji_buttons:
            emoji_button.setText(emojize(emoji_button.text()))

    # OTHER
    def ready_to_recv(self):
        self.ui.download_file_area.hide()
        self.ready = True
        self.enable_all()

    def disable_all(self):
        self.ui.chat_viewer.setEnabled(False)
        self.ui.chat_input.setEnabled(False)
        self.ui.send_button.setEnabled(False)
        self.ui.file_send_button.setEnabled(False)
        self.ui.emoji_open_button.setEnabled(False)

    def enable_all(self):
        self.ui.chat_viewer.setEnabled(True)
        self.ui.chat_input.setEnabled(True)
        self.ui.send_button.setEnabled(True)
        self.ui.file_send_button.setEnabled(True)
        self.ui.emoji_open_button.setEnabled(True)
