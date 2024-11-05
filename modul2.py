nilai_ampere = [1.34, 1.34, 1.34]
perubahan_suhu = [11,21,36]
v = 9  # tegangan
t = 240  # waktu

kapasitas_kalor = []

# Loop untuk nilai_ampere dan perubahan_suhu
for i in range(len(nilai_ampere)):
    rumus = v * nilai_ampere[i] * t  # Menghitung rumus untuk setiap nilai ampere
    rumus_kapasitas = rumus / perubahan_suhu [i]
    kapasitas_kalor.append(rumus_kapasitas)

print("Kapasitas Kalor : ", kapasitas_kalor)

mean = sum(kapasitas_kalor)/3

print("Rata-rata : ", mean)
