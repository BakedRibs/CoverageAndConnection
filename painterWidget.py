from PyQt5.QtWidgets import QWidget

class painterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.setFixedSize(500, 500)
        self.setAutoFillBackground(True)
