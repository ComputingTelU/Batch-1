class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

q = Queue()
q.enqueue(4)
q.enqueue('cat')
q.enqueue(True)
q.enqueue(8.4)

for i in range(0,q.size()) :
	print q.dequeue()
# print q.size()