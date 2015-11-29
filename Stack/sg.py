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
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

s = Stack() #inisialisasi
print s.isEmpty()
s.push(4)
s.push('cat')
print s.size()
print s.peek()
s.push(True)
print s.isEmpty()
print s.pop() #True
print s.pop() #Cat
print s.pop() #4