import random
def fangsi(val):
    x=val[0]
    y=val[1]
    # a = 0.0000000000001 #mencegah pembagian nol
    # fungsi minimasi bukat 1/h-a
    h = ((x+(2*y)-7)*(x+(2*y)-7)) + ((((2*x)+y-5))*(((2*x)+y-5)))
    return h

def fitness(individu):
    GEDE = 9999999
    return GEDE - fangsi(genotofeno(individu))


def decode(code):
    # representasi telah diganti 
    ra = 10
    rb = -10
    N = len(code)
    c = 0
    a = 0

    for i in xrange(1,N+1):
        c = c + (2**(-i))

    for g in xrange(0,N):
        if (code[g]=="1"): 
            a += (2**(-(g+1)))

    return rb + ((ra-rb)*a/c)

def genotofeno(kromosom):
    # menampilkan fentipe dari genotipe satu individu
    if (len(kromosom)%2==1):
        print "panjang kromosom harus genap woy"
        return 0
    else:
        x,y = kromosom[:len(kromosom)/2], kromosom[len(kromosom)/2:]
        return decode(x),decode(y)


def randomindv(panjangkromosom):
    # panjangkromosom harus genap siah
    ret = ""
    for i in range(0,panjangkromosom):
        ret = ret + `random.randint(0,1)`
    return ret


def ranpopul(jumlahindividu,panjangkromosom):
    a = []
    for i in range(0,jumlahindividu):
        rando = randomindv(panjangkromosom)
        a += [[rando,fitness(rando)]]

    return a

# def rodaputar(popul):
#     # diputar sebanyak n kali
#     sumfit = 0;
#     for p in popul:
#         sumfit += fangsi(decode(p))


def listprobabi(popul):
    fitns = [fitness(p) for p in popul]
    totft = float(sum(fitns))
    prob = [f/totft for f in fitns]
    return [sum(prob[:i+1]) for i in range(len(prob))]

def rodaputar(popula,n):
    popul = [a[0] for a in popula]
    terpilih = []
    for nn in xrange(n):
    	probs = listprobabi(popul)
        r = random.uniform(0,1)
        for i in xrange(len(popul)):
            if r <= probs[i]:
                terpilih.append(popul.pop(i))
                break

    return terpilih

def crossover(indv1,indv2):
    t = random.randint(0,len(indv1))
    anak1 = indv1[:t] + indv2[t:]
    anak2 = indv2[:t] + indv1[t:]
    return [anak1,anak2]


def mutasi(individu):
    pm = 1/len(individu) #referensi dari wikiperdia https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)
    hasilmutasi = ""
    for iv in individu:
        p = random.uniform(0,1)
        if( p <= pm):
            if (iv == "0"):
                hasilmutasi += "1"
            if (iv == "1"):
                hasilmutasi += "0"
        else:
        	hasilmutasi += iv
    return [hasilmutasi,fitness(hasilmutasi)]

def terbaik(popo,nelitisme):
	dabes = []
	popo = sorted(popo,key=lambda x:x[1],reverse = True)
	return popo[:nelitisme]
			


kromo = 10
pop = 50 #banyaknya populasi
loop = 100 #jumlah perulangan
nelitisme = 2
popo = ranpopul(pop,kromo)
popo += terbaik(popo,nelitisme)
# for i in popo:
#     print genotofeno(i),"   |",fitness(i)


i = 0
while i<loop:
    ortu = rodaputar(popo,pop)
    anakanak = []
    for j in range(0,pop/2):
        anakanak += crossover(ortu[2*j],ortu[2*j+1])
    mutan = [mutasi(mut) for mut in anakanak]
    popo = terbaik(popo,nelitisme) + mutan

    fitneses = [decode(p)  for p in popo]
    print "generasi ke ",i
    print "fitness elitism : ",popo[0][1]
    for j in range(nelitisme):
    	print genotofeno(popo[j][0]), "nilai fungsi", fangsi(genotofeno(popo[j][0]))
    i += 1

# daftar kekurangan
# 1. yang dicari bukan minimum tapi malah maximum (solved dengan menambah konstanta yang besar pada fungsi fitness)
# 2. batasan untuk nilai x dan y bukan -10 sampai 10 tapi -16 sampai 16
# mohon maaf atas segala kekurangannya
