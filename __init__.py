import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton
from painterWidget import painterWidget

class CoverageAndConnection(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.setWindowTitle('CoverageAndConnection')
        self.pw = painterWidget()
        self.connectBt = QPushButton('生成并连接')
        
        controlLayout = QHBoxLayout()
        controlLayout.addStretch()
        controlLayout.addWidget(self.connectBt)
        controlLayout.addStretch()
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.pw)
        mainLayout.addLayout(controlLayout)
        
        self.setLayout(mainLayout)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    CAC = CoverageAndConnection()
    app.exit(app.exec_())
