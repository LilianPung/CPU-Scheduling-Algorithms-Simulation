def FCFS(self, numberOfProcess, processLabel, arrivalTime, startingTime, burstTime, waitingTime, turnAroundTime, priority):

		self.numberOfProcess = numberOfProcess
		self.processLabel = processLabel
        self.arrivalTime = arrivalTime
        self.startingTime = startingTime
        self.burstTime = burstTime
        self.waitingTime = waitingTime
        self.turnAroundTime = turnAroundTime
        self.priority = priority
 	

numberOfProcess=[]
turnAroundTime = []
waitingTime = []
#processList = []


 
#Sorting processes burst time, on the basis of their priority
for i in range(0,len(priority)-1):
 for j in range(0,len(priority)-i-1):
  if(priority[j]>priority[j+1]):
	swap=priority[j]
	priority[j]=priority[j+1]
	priority[j+1]=swap
 
	swap=burstTime[j]
	burstTime[j]=bt[j+1]
	burstTime[j+1]=swap
 
 	swap=processes[j]
	processes[j]=processes[j+1]
	processes[j+1]=swap
 
waitingTime.insert(0,0) #insert element 0 into index 0 of list waitingTime
turnAroundTime.insert(0,burstTime[0]) #insert element of burstTime[0] into index 0 of list turnAroundTime 
 
 
#Calculating of waiting time and Turn Around Time of each process
for i in range(1,len(processes)):
	waitingTime.insert(i,waitingTime[i-1]+burstTime[i-1])
	turnAroundTime.insert(i,waitingTime[i]+burstTime[i])
 
#calculating average waiting time and average turn around time
avgTurnAroundTime=0
avgWaiting=0

for i in range(0,len(processes)):
	avgWaitingTime = avgWaitingTime + waitingTime[i]
	avgTurnAroundTime = avgTurnAroundTime + turnAroundTime[i]
	avgWaitingTime = float(avgWaitingTime) / numberOfProcess
	avgWaitingTime = float(avgTurnAroundTime) / numberOfProcess

