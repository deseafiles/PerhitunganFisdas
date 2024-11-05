import  math

print("Statis")
bebanstatis = [0.1, 0.15, 0.2, 0.25]
dX1 = [0.036, 0.055, 0.080,0.098] #perubahan panjang ideal itu 0.04, 0.06, 0.08, 0.1
dX2 = [0.239, 0.339, 0.440, 0.556]

for i in range(len(bebanstatis)) :
    rumus1 = bebanstatis [i] * 9.8 / dX1 [i]
    rumus2 = bebanstatis [i] * 9.8 / dX2 [i]
    print("Hasil : ", round(rumus1, 2))
    print("Hasil 2 : ", round(rumus2, 2))



print(" ")
print(" ")
print("Dinamis")
bebandinamis = 0.25
t = [22.81, 23.03, 22.97]
n = 15


T = [round(x / n, 2) for x in t]  
print("T :", T)

T2 = [round(x ** 2, 2) for x in T]  

print("T²:", T2)  

tetapan_dinamis = []
for i in range(len(T2)):
    k = (4 * 9.8596 * bebandinamis) / T2[i]  
    tetapan_dinamis.append(round(k, 2))  
    print("k:", round(k, 2)) 


mean = sum(tetapan_dinamis) / 3
print("Nilai rata-rata:", round(mean, 2))  

print(" ")
print("Perulangan")

mean2 = sum(t) / len(t)
print("Rata- rata t : ", round(mean2, 2))

hasil_pengukuran = []
for i in range(len(t)) :
   rumusratat = (t[i] - mean2)**2
   hasil_pengukuran.append(rumusratat)
   print("Rata- rata ketidakpastian : ", round(rumusratat, 2))

mean3 = math.sqrt(sum(hasil_pengukuran) / len(hasil_pengukuran)) 
print(round(mean3, 2))
