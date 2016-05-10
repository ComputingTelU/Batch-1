import random
def fangsi(val):
    x=val[0]
    y=val[1]
    return ((x+(2*y)-7)**2) + ((((2*x)+y-5))**2)

def fitness(individu):
    return fangsi(decode(individu))

def encode(x,y):
    xbin = '{0:05b}'.format(((1 << 5) - 1) & x)
    ybin = '{0:05b}'.format(((1 << 5) - 1) & y)
    return xbin+ybin

def decode(code):
    return twocomplement(code[0:5]),twocomplement(code[5:10])

def twocomplement(a):
    x=int(a,2)
    if (x>(2**len(a)-1)-(2**(len(a)-1))):
        return x - (1 << len(a))
    else:
        return x

def randomindv():
    ret = ""
    for i in range(0,16):
        ret = ret + `random.randint(0,1)`
    return ret

def ranpopul(l):
    a = []
    for i in range(0,l):
        a += [randomindv()]
    return a

# def rodaputar(popul):
#     # diputar sebanyak n kali
#     sumfit = 0;
#     for p in popul:
#         sumfit += fangsi(decode(p))

def listprobabi(popul):
    #mengembalikan list probabilitas kumulatif
    fitns = [fitness(p) for p in popul]
    totft = float(sum(fitns))
    prob = [f/totft for f in fitns]
    return [sum(prob[:i+1]) for i in range(len(prob))]

def rodaputar(popul,probs,n):
    terpilih = []
    for nn in xrange(n):
        r = random.random()
        for (i,indv) in enumerate(popul):
            if r <= probs[i]:
                terpilih.append(indv)
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
    return hasilmutasi

pop = 16 #banyaknya populasi
terbaik = list()
popo = ranpopul(pop)
print [fitness(t) for t in popo]
i = 0
while i<10000:
    ortu = rodaputar(popo,listprobabi(popo),16);
    anakanak = []
    for j in range(0,pop/2):
        anakanak += crossover(ortu[2*j],ortu[2*j+1])
    mutan = [mutasi(mut) for mut in anakanak]
    popo = mutan
    fitneses = [fitness(p) for p in popo]
    print "generais ke ",i,fitneses
    i += 1
    # #pilih solusi terbaik
    # ytb = popo[fitneses.index(max(fitneses))]
    # print fitness(ytb)
    # if (terbaik.count(ytb) <= 0):
    #     if len(terbaik) > 0:
    #         if fitness(terbaik[len(terbaik)]-1) < fitness(ytb):
    #             terbaik.append(ytb)
    #     else:
    #         terbaik.append(ytb)

# print "hasil"
# print terbaik
# print [fitness(t) for t in terbaik]

# daftar kekurangan
# 1. yang dicari bukan minimum tapi malah maximum
# 2. batasan untuk nilai x dan y bukan -10 sampai 10 tapi -16 sampai 16
# 3. entah kenapa setelah menjalani perulangan yang cukup banyak individunya ga berkembang
# mohon maaf atas segala kekurangannya
