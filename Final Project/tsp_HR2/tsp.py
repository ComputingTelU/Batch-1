class Graph:
	def __init__(self,numVertices):
		self.num = numVertices
		self.mtr = \
			[ \
				[None for x in range(self.num)] \
					for y in range(self.num) \
			]
		self.sts = \
			[ \
				[None for x in range(self.num)] \
					for y in range(self.num) \
			]
		self.tsp = {}

	def add(self, src, des, weight=0):
		if src != des:
			self.mtr[src][des] = weight
			self.mtr[des][src] = weight
			self.sts[src][des] = weight
			self.sts[des][src] = weight

	def minimRow(self):
		for i in range(self.num):

			# mencari nilai paling kecil
			min = 9999
			for j in range(self.num):
				if self.mtr[i][j] is not None and self.mtr[i][j] < min:
					min = self.mtr[i][j]

			# kurangkan semuanya dengan nilai terkecil
			for j in range(self.num):
				if self.mtr[i][j] is not None:
					self.mtr[i][j] -= min

	def miniCollum(self):
		for j in range(self.num):

			# mencari nilai paling kecil
			min = 9999
			for i in range(self.num):
				if self.mtr[i][j] is not None and self.mtr[i][j] < min:
					min = self.mtr[i][j]

			# kurangkan semuanya dengan nilai terkecil
			for i in range(self.num):
				if self.mtr[i][j] is not None:
					self.mtr[i][j] -= min

	def penalty(self):
		max = 0
		i = 0
		j = 0

		# menghitung pinalti, sekalian mencari yg maks
		for x in range(self.num):
			for y in range(self.num):
				if self.mtr[x][y] == 0:

					# mencari nilai minimal baris
					minx = 9999
					for m in range(self.num):
						if m != x:
							if self.mtr[m][y] is not None:
								if minx > self.mtr[m][y]:
									minx = self.mtr[m][y]

					# mencari nilai minimal kolom
					miny = 9999
					for n in range(self.num):
						if n != y:
							if self.mtr[x][n] is not None:
								if miny > self.mtr[x][n]:
									miny = self.mtr[x][n]

					if max <= minx + miny:
						max = miny + minx
						i = x
						j = y
		
		# menyimpan direction ke self.tsp
		self.tsp[i] = j

		# eliminasi pinalti yang telah dipilih
			# menghapus baris dan kolom
		for x in range(self.num):
			self.mtr[x][j] = None
		for y in range(self.num):
			self.mtr[i][y] = None

			# hapus direction yang berlawanan
		self.mtr[j][i] = None

	def generateTSP(self):

		for count in range(self.num-2):
			self.minimRow()
			self.miniCollum()
			self.penalty()

		i = []
		j = []

		tmp = []
		for x in range(self.num):
			if x not in self.tsp:
				i.append(x)

		for x in self.tsp:
			tmp.append(self.tsp[x])
		for y in range(self.num):
			if y not in tmp:
				j.append(y)

		if self.mtr[i[0]][j[0]] is not None \
			and \
		   self.mtr[i[1]][j[1]] is not None :
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
			wet = self.sts[frm][self.tsp[frm]]
			print '--> ', self.tsp[frm],
			cost += wet
			frm = self.tsp[frm]
			if (frm == src):
				break
		print
		print cost

	def showGraph(self):
		for elm in self.mtr:
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
