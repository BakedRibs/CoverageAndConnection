from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QColor

class painterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.setFixedSize(500, 500)
        self.setAutoFillBackground(True)
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(255, 255, 255))
        self.setPalette(pal)
