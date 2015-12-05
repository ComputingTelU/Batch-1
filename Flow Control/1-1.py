from random import randint

a = [randint(0,100) for i in range(0,10)]
# print a


b = a
# print a
# print sorted(b)

for i in range(0,len(a)-1):
	for j in range(i+1,len(a)):
		if a[i] > a[j]:
			a[i],a[j] = a[j],a[i]

# print a
def checker(str1, str2):
	return sorted(str1) == sorted(str2)


# print checker("katok", "kotak")

kata1 = "febrian imanda effendy"
kata2 = "kotak"

print kata1[5:]

x = [randint(1,10)]

# for i in kata1:
	# print i

kataa = sorted(kata1)
katab = sorted(kata2)

# print "kataa : ",kataa
# print "katab : ",katab
# if kataa == katab:
# 	print True
# else:
# 	print False


