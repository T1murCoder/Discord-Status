import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from ui_main import Ui_MainWindow


class CustomDiscordStatusWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with open("res\stylesheet\Hookmark.qss", "r") as styleFile:
            self.setStyleSheet(styleFile.read())
        self.setWindowIcon(QIcon("res\icons\discord.ico"))
        self.InitUI()
    
    def InitUI(self):
        pass
    
    def closeEvent(self, event):
        pass
        """
        event.ignore()
        self.hide()
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CustomDiscordStatusWindow()
    main_window.show()
    sys.exit(app.exec())