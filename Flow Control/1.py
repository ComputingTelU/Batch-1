class Human:
	def __init__(self):
		self.hands = 2
		self.legs = 2

	def doWalk(self, n=False):
		if n :
			print "I'm walking with",n,"legs"
		else :
			print "I'm walking with",self.legs,"legs"

h = Human()
h.doWalk()
h.doWalk(10)
print "i have",h.hands,"hands"