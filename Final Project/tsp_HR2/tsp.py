class Graph:
	def __init__(self,numVertices):
		self.num = numVertices
		self.matrix = [[None for x in range(self.num)] for y in range(self.num)]
		self.stat = [[None for x in range(self.num)] for y in range(self.num)]
		self.tsp = {}

	def add(self,src,dest,weight=0):
		if src != dest:
			self.matrix[src][dest] = weight
			self.matrix[dest][src] = weight
			self.stat[src][dest] = weight
			self.stat[dest][src] = weight

	def minimBaris(self):
		for i in range(self.num):
			min = 9999
			for j in range(self.num):
				elm = self.matrix[i][j]
				if elm is not None and elm < min:
					min = elm
			for j in range(self.num):
				if self.matrix[i][j] is not None:
					self.matrix[i][j] -= min
			
			# print self.matrix[i]

	def minimKolom(self):
		for j in range(self.num):
			min = 9999
			for i in range(self.num):
				elm = self.matrix[i][j]
				if elm is not None and elm < min:
					min = elm
			for i in range(self.num):
				if self.matrix[i][j] is not None:
					self.matrix[i][j] -= min

		# for elm in self.matrix:
		# 	print elm

	def pinalti(self):
		num = self.num
		max = 0
		i = 0
		j = 0

		# for elm in self.matrix:
		# 	print elm

		for x in range(num):
			for y in range(num):
				if self.matrix[x][y] == 0:
					minx = 9999
					miny = 9999
					for m in range(num):
						val = self.matrix[m][y]
						if minx > val and m != x:
							if val is not None:
								minx = val

					for n in range(num):
						val = self.matrix[x][n]
						if miny > val and n != y:
							if val is not None:
								miny = val

					if max <= minx + miny:
						max = miny + minx
						i = x
						j = y

		self.matrix[j][i] = None
		self.tsp[i] = j
		for x in range(num):
			self.matrix[x][j] = None
		for y in range(num):
			self.matrix[i][y] = None

		# for elm in self.matrix:
		# 	print elm

	def generateTSP(self):
		for count in range(self.num-2):
			self.minimBaris()
			self.minimKolom()
			self.pinalti()

		i = []
		j = []

		for x in range(self.num):
			if x not in self.tsp:
				i.append(x)

		tmp = []
		for x in self.tsp:
			tmp.append(self.tsp[x])
		for x in range(self.num):
			if x not in tmp:
				j.append(x)

		if self.matrix[i[0]][j[0]] is not None and self.matrix[i[1]][j[1]] is not None:
				self.tsp[i[0]] = j[0]
				self.tsp[i[1]] = j[1]
		else:
			self.tsp[i[0]] = j[1]
			self.tsp[i[1]] = j[0]


	def showTSP(self,src):
		frm = src
		cost = 0
		print frm,
		while True:
			print ' --> ', self.tsp[frm],
			cost += self.stat[frm][self.tsp[frm]]
			frm = self.tsp[frm]
			if (frm == src):
				break
		print ''
		print cost

	def showGraph(self):
		for elm in self.stat:
			for el in elm:
				if el is None:
					print el, "\t",
				else:
					print el, "  \t",
			print

g = Graph(5)
g.add(0,1,1)
g.add(0,2,2)
g.add(0,3,3)
g.add(0,4,4)
g.add(1,2,5)
g.add(1,3,4)
g.add(1,4,3)
g.add(2,3,5)
g.add(2,4,2)
g.add(3,4,1)

g.showGraph()
print
g.generateTSP()
g.showTSP(1)
