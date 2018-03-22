from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QColor, QPainter, QPen

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
        
        self.painter = QPainter(self)
        self.pen = QPen(QColor(0, 0, 0))
        self.painter.setPen(self.pen)
        
    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.paintCircle(event, qp)
        qp.end()

    def paintCircle(self, event, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.drawEllipse(100, 100, 20, 20)
