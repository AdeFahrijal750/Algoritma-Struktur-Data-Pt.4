#input

TotalDetik = int(input("Masukkan Total Detik      :"))

#proses
Hari = TotalDetik //86400
SisaHari = TotalDetik % 86400

Jam = SisaHari // 3600
SisaJam = SisaHari % 3600

Menit = SisaJam // 60
Detik = SisaJam % 60

#output
print("Hasil Konversi :", TotalDetik, "Detik Adalah,", Hari, "Hari,", Jam, "Jam,", Menit, "Menit,", Detik, "Detik,")