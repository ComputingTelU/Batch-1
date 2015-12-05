from random import randint



a = [randint(0,100) for i in range(0,10)]
b = [i for i in range(0,10)]
print a
for i in range(0,len(a)):
	ind = i
	for j in range(i,len(a)):
		if a[ind] < a[j]:
			ind = j
	a[i],a[ind] = a[ind], a[i]
		
print a
