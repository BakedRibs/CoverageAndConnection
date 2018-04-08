import random
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QColor, QPainter

class painterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.setFixedSize(600, 600)                                                        #为了能完整显示每一个圆，而不是截取其一部分，为左右各预留了50
        self.setAutoFillBackground(True)
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(255, 255, 255))              #设置背景颜色为白色
        self.setPalette(pal)                                                                  #设置背景
        
        self.circleNumber = 0
        
    def paintEvent(self, event):
        #在paintEvent中调用paintCircle
        qp = QPainter()
        qp.begin(self)
        self.paintCircle(event, qp)
        qp.end()

    def paintCircle(self, event, qp):
        #根据self.points中存储的圆的数量和位置，在绘图区域内绘制图形
        #在drawEllipse函数中，100为二倍半径
        for i in range(self.circleNumber):
            qp.setPen(QColor(0, 0, 0))
            qp.drawEllipse(self.points[i][0], self.points[i][1], 100, 100)
        
    def paintStatusChanged(self, count):
        #按钮按下时，执行随机生成圆过程，并通过union_find算法计算其连通性。找到相互连通的节点，并在图中标示出来。
        self.circleNumber = count                                                              #根据传递的参数修改self.circleNumber
        self.points = []                                                                            #存放所有点的坐标
        self.id = []                                                                                 #存放所有节点的根节点
        self.connections = []                                                                    #存放所有连接
        self.size = []                                                                               #为实现算法最优化，存放树的深度
        for i in range(count):
            point = []
            point.append(round(random.uniform(0, 500), 2))                           #在0-500范围内随机生成横纵坐标
            point.append(round(random.uniform(0, 500), 2))
            self.points.append(point)                                                          #将新点添加到
            self.id.append(i)                                                                      #将每个节点的根节点初始化为其自身
            self.size.append(1)
        for i in range(count):
            for j in range(i+1, count):
                if self.connectToAnother(i, j, 50) == True:                              #判断节点与其他节点是否相连，生成一系列连接，这一系列连接中包含了图中所有的相互连接关系
                    self.connections.append([i, j])
        for i in range(len(self.connections)):                                             #针对每一个连接
            self.unionRoot(self.connections[i][0], self.connections[i][1])          #将两个节点连接起来，修改其self.id属性
        for i in range(count):
            root = self.findRoot(i)                                                             #在所有节点连接完成后，将其self.id修改为其根节点
            self.id[i] = root
        self.update()
        
    def unionRoot(self, p, q):
        #将两节点p和q相连
        i = self.findRoot(p)                      #找到p的根节点为i
        j = self.findRoot(q)                     #找到q的根节点为j
        if i == j:                                   #若p和q的根节点相同，则两者已经相互连通
            return
        if self.size[i] < self.size[j]:            #为了避免最坏情况，根据树的深度选择修改p或q的根节点
            self.id[i] = j                           #将p的根节点设置为与q的根节点相同
            self.size[j] += self.size[i]
        else:
            self.id[j] = i                           #将q的根节点设置为与p的根节点相同
            self.size[i] += self.size[j]
        
    def findRoot(self, p):
        #查找p的根节点：若p不是指向自身的节点，则将p修改为p当前所指向的节点，直到最终找到一个指向自身的节点，认为其为p的根节点，返回此节点
        while p != self.id[p]:
            p = self.id[p]
        return p
        
    def connectToAnother(self, i, j, radius):
        #根据两个节点的横纵坐标，判断其距离是否小于二倍半径，若是，则认为两个节点相连，生成一条连接
        dis2 = pow((self.points[j][0] - self.points[i][0]), 2) + pow((self.points[j][1]-self.points[i][1]), 2)
        return dis2 <= pow(radius * 2, 2)
