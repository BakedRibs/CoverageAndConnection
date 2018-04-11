import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QSpinBox
from painterWidget import painterWidget

class CoverageAndConnection(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.setWindowTitle('CoverageAndConnection')
        self.pw = painterWidget()                              #绘图区域
        self.sensorNum = QSpinBox()
        self.sensorNum.setRange(1, 300)                    #节点数量下限为1，上限为300
        self.sensorNum.setValue(200)                         #默认节点数量为200
        self.connectBt = QPushButton('生成并连接')
        
        controlLayout = QHBoxLayout()
        controlLayout.addStretch()
        controlLayout.addWidget(self.sensorNum)        #控制栏添加节点数量窗口
        controlLayout.addWidget(self.connectBt)        #控制栏添加开始连接按钮
        controlLayout.addStretch()
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.pw)                     #主界面添加绘图区域
        mainLayout.addLayout(controlLayout)            #主界面添加控制栏
        
        self.setLayout(mainLayout)
        self.show()
        self.move(0, 0)
        
        self.connectBt.clicked.connect(self.connectBtClicked)        #按钮按下时，响应事件
        
    def connectBtClicked(self):
        self.pw.paintStatusChanged(self.sensorNum.value())         #调用painterWidget类中的paintStatusChanged函数，将修改后的节点数量传递过去
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    CAC = CoverageAndConnection()
    app.exit(app.exec_())
