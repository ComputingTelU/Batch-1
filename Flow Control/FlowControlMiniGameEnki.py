#MINI GAMES
def checker(str1,str2):
	return sorted(str1) == sorted(str2)

kata1 = "katok"
kata2 = "kotak"

print checker(kata1,kata2)

def hilang(kata):
	b = ""
	for i in kata:
		if i.lower() not in ['a','i','u','e','o']:
			b += i
	print b

hilang("Febrian Imanda Effendy")