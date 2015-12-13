class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)

class Family_Tree:
	def __init__(self,name,depth=0,partner=None):
		self.name = name
		self.children = []
		self.depth = depth
		self.partner = partner
	def __repr__(self,level=0):
		ret = "\t"*level+repr(self.name)+"\n"
		for child in self.children:
			ret += child.__repr__(level+1)
		return ret
	def searchFamily(self,name): # search using breadth-first search
		Q=Queue()
		Q.enqueue(self)
		while not Q.isEmpty():
			current = Q.dequeue()
			if current.name == name:
				break
			else:
				if current.partner != None and current.partner.name == name:
					break
			for child in current.children:
				Q.enqueue(child)
		if current.name == name:
			return current
		else:
			if current.partner != None and current.partner.name == name:
				return current.partner
			else:
				return None
	def newChild(self,parent,childName):
		parent = self.searchFamily(parent)
		child = self.searchFamily(childName)
		if parent != None and child == None:
			parent.children.append(Family_Tree(childName,parent.depth+1))
		else:
			print 'there are no such parent'
			print 'or'
			print 'parent are already had',childName
	def marry(self,name1,name2):
		name1 = self.searchFamily(name1)
		if name1 != None:
			name2 = Family_Tree(name2,name1.depth,name1)
			name2.children = name1.children
			name1.partner = name2
		else:
			print 'there is no',name1,'in family tree'
	def relationshipBetween(self,name1,name2):
		name1 = self.searchFamily(name1)
		name2 = self.searchFamily(name2)
		if name1 != None and name2 != None:
			if name1 == name2:
				print name1.name,'is',name2.name
			else:
				dif = name1.depth - name2.depth
				if dif == 2:
					print name1.name,'is grandchild of',name2.name
				elif dif == 1:
					if name1 in name2.children:
						print name1.name,'is child of',name2.name
					else:
						print name1.name,'is nephew of',name2.name
				elif dif == 0:
					print name1.name,'is brother of',name2.name
				elif dif == -1:
					if name2 in name1.children:
						print name1.name,'is parent of',name2.name
					else:
						print name1.name,'is uncle of',name2.name
				elif dif == -2:
					print name1.name,'is grandparent of',name2.name
		else:
			print 'something wrong!!'
# creating a family tree
happyFamily = Family_Tree('joko') # the head of family
happyFamily.newChild('joko','bima') # creating child for joko
happyFamily.newChild('joko','sani') # creating child for joko
happyFamily.newChild('bima','boni') # creating child for bima
happyFamily.newChild('bima','boko') # creating child for bima
happyFamily.newChild('bima','haram') # creating child for bima
happyFamily.newChild('sani','budi') # creating child for sani
happyFamily.newChild('sani','momon') # creating child for sani
happyFamily.newChild('sani','maman') # creating child for sani 
happyFamily.newChild('sani','maman') # example of creating child that already had
happyFamily.marry('sani','handsome') # sani marrying handsome

#printing family tree
print '\nthe happy family tree'.upper()
print happyFamily

# testing function
print 'relationship'.upper()
happyFamily.relationshipBetween('joko','joko') # example of selecting their self
happyFamily.relationshipBetween('joko','maman') # example of grandparent
happyFamily.relationshipBetween('bima','boni') # example of parent
happyFamily.relationshipBetween('sani','bima') # example of brother
happyFamily.relationshipBetween('haram','joko') # example of grandchild
happyFamily.relationshipBetween('boko','bima') # example of child
happyFamily.relationshipBetween('maman','bima') # example of nephew
happyFamily.relationshipBetween('bima','budi') # example of uncle
happyFamily.relationshipBetween('handsome','budi') # result of married yielding handsome to be the parent of budi 
happyFamily.relationshipBetween('enki','rizkiyana') # example of wrong input
happyFamily.relationshipBetween('isa','fadhil') #example of wrong input