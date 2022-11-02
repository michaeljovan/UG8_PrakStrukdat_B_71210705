class CircularQueue():

	def __init__(self, size): 
		self.size = size
		
		self.queue = [None for i in range(size)]
		self.front = self.rear = -1

	def enqueue(self, data):
		
		if ((self.rear + 1) % self.size == self.front):
			print(" Antrian penuh\n")
			
		elif (self.front == -1):
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		else:
			
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = data
			
	def dequeue(self):
		if (self.front == -1):
			print ("Antrian kosong\n")
			
		elif (self.front == self.rear):
			temp=self.queue[self.front]
			self.front = -1
			self.rear = -1
			return temp
		else:
			temp = self.queue[self.front]
			self.front = (self.front + 1) % self.size
			return temp

	def display(self):
	
		if(self.front == -1):
			print ("Antrian Kosong")

		elif (self.rear >= self.front):
			print("Yang ada pada antrian adalah:",
											end = " ")
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		else:
			print ("Yang ada pada antrian circular:",
										end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(0, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		if ((self.rear + 1) % self.size == self.front):
			print("Antrian penuh")

circularQueue = CircularQueue(5) 
circularQueue.enqueue(14) 
circularQueue.enqueue(22) 
circularQueue.enqueue(13) 
circularQueue.enqueue(-6) 
circularQueue.display() 
print ("data yang dihapus adalah = ", circularQueue.dequeue())  
print ("data yang dihapus adalah = ", circularQueue.dequeue()) 
circularQueue.display() 
circularQueue.enqueue(9) 
circularQueue.enqueue(20) 
circularQueue.enqueue(5) 
circularQueue.display() 
