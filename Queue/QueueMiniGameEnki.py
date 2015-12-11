class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)

# MINI GAMES
def potatoGame(pemain,langkah):
	n = Queue()
	for i in pemain:
		n.enqueue(i)
	while n.size()>1:
		yangMegangRemote = n.dequeue()
		for i in range(langkah):
			n.enqueue(yangMegangRemote)
			yangMegangRemote=n.dequeue()
	print n.items,

yangIkutanMain = ["enki","fadhil","satrio","isa","adnan"]

potatoGame(yangIkutanMain,1); print "menang"
print yangIkutanMain