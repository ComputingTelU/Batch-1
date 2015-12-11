class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)
	def printStack(self):
		print self.items

# MINI GAMES
def isSeimbang(kataberkurung):
	n = Stack()
	for i in kataberkurung:
		if i in ['(',')']:
			if i == '(':
				n.push(1)
			else:
				if not n.isEmpty():
					n.pop()
				else:
					return False
	n.printStack
	if n.isEmpty():
		return True
	else:
		return False

katta = ")"
print isSeimbang(katta)

#MINI GAME
def nilaiBiner(biner):
	n = Stack()
	while (biner != 0):
		n.push(biner%2)
		biner /= 2
	while not n.isEmpty():
		print n.pop(),

biner = 155

nilaiBiner(biner)