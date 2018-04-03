import random
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
        
        self.circleNumber = 0
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.paintCircle(event, qp)
        qp.end()

    def paintCircle(self, event, qp):
        for i in range(self.circleNumber):
            qp.setPen(QColor(0, 0, 0))
            qp.drawEllipse(self.points[i][0]-50, self.points[i][1]-50, 100, 100)
        
    def paintStatusChanged(self, count):
        self.circleNumber = count
        self.points = []
        self.id = []
        self.connections = []
        self.size = []
        for i in range(count):
            point = []
            point.append(round(random.uniform(0, 500), 2))
            point.append(round(random.uniform(0, 500), 2))
            self.points.append(point)
            self.id.append(i)
            self.size.append(1)
        for i in range(count):
            for j in range(i+1, count):
                if self.connectToAnother(i, j, 50) == True:
                    self.connections.append([i, j])
        for i in range(len(self.connections)):
            self.unionRoot(self.connections[i][0], self.connections[i][1])
            print(self.connections[i], self.id)
        self.id.sort()
        self.update()
        
    def unionRoot(self, p, q):
        i = self.findRoot(p)
        j = self.findRoot(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
        
    def findRoot(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p
        
    def connectToAnother(self, i, j, radius):
        dis2 = pow((self.points[j][0] - self.points[i][0]), 2) + pow((self.points[j][1]-self.points[i][1]), 2)
        return dis2 <= pow(radius * 2, 2)
