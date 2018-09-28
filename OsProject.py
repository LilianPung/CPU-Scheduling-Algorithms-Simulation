#!/usr/bin/python3
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import Process

'''
TODO
''' 

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "CPU Scheduling Algorithms Simulation"
        self.top = 100
        self.left = 1000
        self.width = 800
        self.height = 500

        self.flag = False
        self.firstTime= True

        self.numberOfProcess = 0
        self.timeForEachProcess = []
        self.startingTime = []
        self.nums = [] # Number on ruler
        self.processLabel = []
        self.processStartLineEdit = []
        self.processTimeLineEdit = []
        self.priorityLineEdit = []
        self.enterStart = QLabel(self)
        self.enterTime = QLabel(self)
        self.enterPriority = QLabel(self)
        self.trueSequence = []
        self.trueBurstTime= []
        self.priority = []
        self.nop = 0 # Number of process
        self.count = 0
        self.simulateClicked = False # Prevent run from running by itself :(

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        #self.setGeometry(0, 0, self.screenSize.width(), self.screenSize.height())
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        space = 30
        titleLabel = QLabel("CPU Scheduling Algorithms Simulation", self)
        titleLabel.move(50, space)
        algorithmsLabel = QLabel("Algorithms : ", self)
        algorithmsLabel.move(50, space+30)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("FCFS")
        self.comboBox.addItem("RR")
        self.comboBox.addItem("Three-level Queue Scheduling")
        self.comboBox.addItem("SRTN")
        self.comboBox.move (140, space+25)
        numberOfProcessLabel = QLabel("Number of Process (1-10)", self)
        numberOfProcessLabel.move(50, space+70)
        self.numberOfProcessET = QLineEdit(self)
        self.numberOfProcessET.move(225,space+65)
        simulateBtn = QPushButton("Simulate",self)
        simulateBtn.move(50, space+100)
        simulateBtn.clicked.connect(self.SimulateClicked)
        self.runBtn = QPushButton("Run", self)
        self.runBtn.move(50, 250)
        self.runBtn.resize(0,0)
        self.hideStuff()

        self.show()

    def SimulateClicked(self):
        try:
            self.flag = False
            self.simulateClicked = True
            self.nop = self.numberOfProcessET.text()
            self.nop = int(self.nop)
            if self.nop < 3 or self.nop > 10:
                QMessageBox.question(self, 'ERROR', "Invalid process number", QMessageBox.Ok)

            else:
                for i in range(self.nop):
                    self.processStartLineEdit[i].setText("")
                    self.processTimeLineEdit[i].setText("")
                    self.priorityLineEdit[i].setText("")

                self.clearStuff()
                self.update()
     
                self.nop = self.numberOfProcessET.text()
                self.nop = int(self.nop)
                self.enterStart.setText("Enter process value for start time :  ")
                self.enterStart.adjustSize()
                self.enterStart.move(50, 160)
     
                self.enterTime.setText("Enter burst time :  ")
                self.enterTime.adjustSize()
                self.enterTime.move(50, 190)
     
                self.enterPriority.setText("Enter Priority :  ")
                self.enterPriority.adjustSize()
                self.enterPriority.move(50, 220)
     
                # Display start time and time
                for i in range(self.nop):
                    self.processStartLineEdit[i].resize(24,24)
                    self.processTimeLineEdit[i].resize(24,24)
                    self.priorityLineEdit[i].resize(24,24)
     
                self.runBtn.resize(80,24)
                self.runBtn.clicked.connect(self.Run)
        except:
            QMessageBox.question(self, 'ERROR', "Invalid process number", QMessageBox.Ok)


    def Run(self):
        #if self.simulateClicked == True '''and self.count == 0''':
        if self.simulateClicked == True:
            try:
                totalTime = 0
                for i in range(self.nop):
                    a = int(self.processStartLineEdit[i].text())
                    b = int(self.processTimeLineEdit[i].text())
                    c = int(self.priorityLineEdit[i].text())
                    self.startingTime.append(a)
                    self.timeForEachProcess.append(b)
                    self.priority.append(c)
                    totalTime += b

                if totalTime > 60:
                    QMessageBox.question(self, 'ERROR', "Total time exceeds the limit", QMessageBox.Ok)

                else:
     
                    if self.comboBox.currentText()=="FCFS":
                        print("FCFS")
                        self.FCFS()
                    elif self.comboBox.currentText()=="RR":
                        print("RR")
                        self.RR()
                    elif self.comboBox.currentText()=="TLQS":
                        print("TLQS")
                        self.TLQS()
                    else:
                        print("SRTN")
                        self.SRTN()
                        print("after SRTN")
                    self.flag = True
                    self.simulateClicked = False
                    self.count = 0
                    self.update()
            except:
                #self.simulateClicked = False
                print("exception>> simulatedClicked>> ", self.simulateClicked)
                self.timeForEachProcess.clear()
                #QMessageBox.question(self, 'ERROR', "Must enter all boxes", QMessageBox.Ok)
        else:
            #self.simulateClicked = True 
            print("else>> simulatedClicked>> ", self.simulateClicked)


    def paintEvent(self, event):
        if self.flag:
            color = [(255, 64, 0), (255, 128, 0), (255, 191, 0),
                    (255, 255, 0), (128, 255, 0), (0, 255, 191),
                    (0, 191, 255), (0, 128, 255), (128, 0, 255), (255, 0, 255)]
            painter = QPainter(self)
            painter.begin(self)
            painter.setPen(QPen(Qt.white, -1, Qt.SolidLine))

            mapColor = {}
            uniqueTrueSequence = set(self.trueSequence)
            colorIndex = 0
            for i in uniqueTrueSequence:
                mapColor[i] = colorIndex
                colorIndex += 1

            print(mapColor)

            letsMovetogether = 100
            # Color bars
            tailPos = 50
            j = 0
            for i in self.trueBurstTime:
                r = color[mapColor[i]][0]
                g = color[mapColor[i]][1]
                b = color[mapColor[i]][2]
                painter.setBrush(QColor(r, g, b))
                painter.drawRect(tailPos, (200+letsMovetogether), i*30, 30)

                # Process label
                p = "P" + str(self.trueSequence[j])
                self.processLabel[j].setText(p)
                midBar = tailPos+((i*30)/2)
                self.processLabel[j].move(midBar-8, 207+letsMovetogether)
                self.processLabel[j].adjustSize()
                tailPos += i*30
                j += 1


            # Ruler
            rulerPos = 50
            sumTime = sum(self.timeForEachProcess)
            for i in range(sumTime+1):
                painter.setBrush(QColor(0,0,0))
                painter.drawRect(rulerPos, 235+letsMovetogether, 1, 15)
                self.nums[i].setText(str(i))
                self.nums[i].move(rulerPos-3, 250+letsMovetogether)
                self.nums[i].adjustSize()
                rulerPos += 30

            painter.drawRect(50, 242.5+letsMovetogether, sumTime*30, 1)
            self.firstTime = False
            painter.end()

        else:
            painter = QPainter(self)
            painter.begin(self)
            painter.setPen(QPen(Qt.white, -1, Qt.SolidLine))
            painter.drawRect(0, 300, self.screenSize.width(), 900)
            for j in range(len(self.trueSequence)):
                # Process label
                p = ""
                self.processLabel[j].setText(p)

            sumTime = sum(self.timeForEachProcess)
            for i in range(sumTime+1):
                self.nums[i].setText("")

            painter.end()


    def FCFS(self):
        print("Enter the number of processess: ")
        n=int(input())
        processes=[]
        for i in range(0,n):
            processes.insert(i,i+1)

        print("Enter the burst time of the processes: \n")
        burstTime=[]
        burstTime=list(map(int, raw_input().split()))

        print("Enter the arrival time of the processes: \n")
        at=[]
        at=list(map(int, raw_input().split()))
        at.sort()

        print("Enter the priority of the processes: \n")
        priority=[]
        priority=list(map(int, raw_input().split()))
       

        processes.sort()

        print("\n")
        print("Process\t  Burst Time\t  Arrival Time\t  Priority\t")
        for i in range(0,n):
            print(str(processes[i])+"\t\t"+str(burstTime[i])+"\t\t"+str(at[i])+"\t\t"+str(priority[i]))

        processes = []
        for i in range(0,len(priority)-1):
            for j in range(0,len(priority)-i-1):
                if(self.priority[j]>self.priority[j+1]):
                    swap=self.priority[j]
                    self.priority[j]=self.priority[j+1]
                    self.priority[j+1]=swap
                    
                    swap=self.enterTime[j]
                    self.enterTime[j]=bt[j+1]
                    self.enterTime[j+1]=swap

                    swap=processes[j]
                    processes[j]=processes[j+1]
                    processes[j+1]=swap

        for i in self.enterTime:
            self.trueBurstTime.append(i)
        
        self.trueSequence = processes

    def RR(self):
        pass
    
    def TLQS(self):
        pass

    def SRTN(self):
        # reference:
        # self.startingTime = list of arrival time
        # self.timeForEachProcess = list of burst time
        # self.priority = list of priority 
    
        # local variables of SRTN
        arrivalTime = self.startingTime 
        burstTime = self.timeForEachProcess
        priority = self.priority
        remainingTime = burstTime # initialize each initial remaining time as burst time
        finishTime = sum(self.timeForEachProcess)
        processList = [] # list of process to be colored per 1 time unit
        
        currentTime = 1 # initialize at 1
        readyQueue = []
        processLabel = 1
    
        print("In SRTN")
        for i in range(self.nop):
            a = list(processLabel, arrivalTime[i], burstTime[i], priority[i], remainingTime[i])
            processList.append(a)
            if(processList[i].arrivalTime == 0):
                firstProcess = processList[i]
            processLabel += 1
    
        runningProcess = firstProcess # initialize runningProcess
        
        while(currentTime != finishTime):
            # adds new process to ready queue
            for i in range(self.numberOfProcess):
                if(processList[i].arrivalTime == currentTime):
                    readyQueue.append(processList[i])
                    
            print("break point")
            # compare and do preemption when new process arrives
            if(len(readyQueue) != 0):
                if(readyQueue[-1].arrivalTime == currentTime):
                    if(runningProcess == firstProcess):
                        processList.append(readyQueue[0].processLabel) # color it
                        readyQueue = readyQueue[1:] # delete from ready queue
                        runningProcess.remainingTime -= 1
                    else: # compare remaining time
                        # if running process remaining time < new process burst time, then continue do the running process
                        if(runningProcess.remainingTime < readyQueue[0].burstTime):
                            processList.append(runningProcess.processLabel)
                            runningProcess.remainingTime -= 1
                        # if running process remaining time = new process burst time, then compare priority
                        elif(runningProcess.remainingTime == readyQueue[0].burstTime):
                            if (runningProcess.priority <= readyQueue[0].priority):
                                processList.append(runningProcess.processLabel)
                                runningProcess.remainingTime -= 1
                            else:
                                readyQueue.append(runningProcess)
                                runningProcess = readyQueue[0]
                                readyQueue = readyQueue[1:]
                                processList.append(runningProcess.processLabel)
                                runningProcess.remainingTime -= 1
                        # if running process remaining time > new process burst time, then preempt
                        else:
                            readyQueue.append(runningProcess)
                            runningProcess = readyQueue[0]
                            readyQueue = readyQueue[1:]
                            processList.append(runningProcess.processLabel)
                            runningProcess.remainingTime -= 1
                currentTime += 1
            else:
                processList.append(runningProcess.processLabel)
                runningProcess.remainingTime -= 1
                currentTime += 1
                
            # sort the readyQueue according to shortest remainingTime and priority
            # to-do
            readyQueue = sorted(readyQueue, key = lambda x: (x.remainingTime, x.priority))
    
            # new running process will be the shortest remaining time
            if(runningProcess.remainingTime == 0):
                runningProcess = readyQueue[0]
            readyQueue = readyQueue[1:]

            # Everything has ended, create new list  
            for i in processList.processLabel:
                if i not in self.trueSequence:
                    self.trueSequence.append(i)
                    self.trueBurstTime.append(1)
                else:
                    self.trueBurstTime[-1] += 1

        print("processList >> ",processList) 
        print("burstTime >> ",burstTime)


    def hideStuff(self):
        j = 280
        # LineEdit for starting time each process
        for i in range(10):
            st = QLineEdit(self)
            st.resize(0, 0)
            st.move(j, 155)
            self.processStartLineEdit.append(st)

            t = QLineEdit(self)
            t.resize(0, 0)
            t.move(j, 185)
            self.processTimeLineEdit.append(t)

            p = QLineEdit(self)
            p.resize(0,0)
            p.move(j,215)
            self.priorityLineEdit.append(p)
            j += 30
            
        # Number for ruler
        for i in range(100):
            self.num = QLabel("", self)
            self.nums.append(self.num)

        # Label for each process
        for i in range(10):
            self.pro = QLabel("",self)
            self.processLabel.append(self.pro)

    def clearStuff(self):
        for i,j,k,l in zip(self.processStartLineEdit,self.processTimeLineEdit,self.nums,self.processLabel,):
            i.resize(0,0)
            j.resize(0,0)
            l.setText("")
        
        for k in self.nums:
            k.setText("")

        self.trueBurstTime.clear()
        self.trueSequence.clear()
        self.startingTime.clear()
        self.timeForEachProcess.clear()
        self.nop = 0

    def checkInput(self, text):
        print(text," ",type(text))
        if text != "1" or text != "2" or text != "3" or text != "4" or text != "5" or text != "6" or text != "7" or text != "8" or text != "9" or text != "10":
            return False
        else:
            return True 



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
