import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from ui_main import Ui_MainWindow
from core import create_rpc, start_rpc, update_rpc, close_rpc
import json


class CustomDiscordStatusWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config = {}
        
        with open("res\stylesheet\Hookmark.qss", "r") as styleFile:
            self.setStyleSheet(styleFile.read())
        
        self.setWindowIcon(QIcon("res\icons\discord.ico"))
        self.rpc = None
        
        self.load_config()
        self.InitUI()
    
    def InitUI(self):
        self.btn_disconnect.setEnabled(0)
        
        self.btn_connect.clicked.connect(self.connect_rpc)
        self.btn_disconnect.clicked.connect(self.disconnect_rpc)
        self.btn_set_status.clicked.connect(self.set_status)
    
    def connect_rpc(self):
        try:
            if not self.config.get("app_id"):
                self.label_error.setText("Id приложения не указан")
                return
            self.rpc = create_rpc(self.config["app_id"])
            start_rpc(self.rpc)
            update_rpc(self.rpc, *list(self.config.values())[1:])
            self.btn_connect.setEnabled(0)
            self.btn_disconnect.setEnabled(1)
        except Exception as ex:
            self.label_error.setText("Id приложения указан не верно")
    
    def disconnect_rpc(self):
        if self.rpc:
            close_rpc(self.rpc)
        self.btn_connect.setEnabled(1)
        self.btn_disconnect.setEnabled(0)
    
    def set_status(self):
        
        self.config = {
            "app_id": self.lnedit_app_id.text(),
            "state_text": self.lnedit_state_text.text(),
            "details_text": self.lnedit_details_text.text(),
            "large_image": self.lnedit_large_image.text(),
            "large_text": self.lnedit_large_text.text(),
            "small_image": self.lnedit_small_image.text(),
            "small_text": self.lnedit_small_text.text()
        }
        
        if not all(self.config.values()):
            self.label_error.setText("Указаны не все параметры!")
            return
        
        self.label_error.setText("")
        
        self.save_config()
        self.disconnect_rpc()
    
    def load_config(self):
        try:
            with open("config.json", 'r', encoding="utf-8") as file:
                self.config = json.load(file)
            
            self.lnedit_app_id.setText(self.config.get("app_id", ""))
            self.lnedit_state_text.setText(self.config.get("state_text", ""))
            self.lnedit_details_text.setText(self.config.get("details_text", ""))
            self.lnedit_large_image.setText(self.config.get("large_image", ""))
            self.lnedit_large_text.setText(self.config.get("large_text", ""))
            self.lnedit_small_image.setText(self.config.get("small_image", ""))
            self.lnedit_small_text.setText(self.config.get("small_text", ""))

        except Exception:
            self.config = {
            "app_id": "",
            "state_text": "",
            "details_text": "",
            "large_image": "",
            "large_text": "",
            "small_image": "",
            "small_text": ""
            }
            self.save_config()
    
    def save_config(self):
        with open("config.json", 'w', encoding="utf-8") as file:
            json.dump(self.config, file, ensure_ascii=False, indent=4)

    def closeEvent(self, event):
        # TODO: Сделать сворачивание в трей
        self.save_config()
        self.disconnect_rpc()
        """
        event.ignore()
        self.hide()
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CustomDiscordStatusWindow()
    main_window.show()
    sys.exit(app.exec())