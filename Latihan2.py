#Sebuah proyek dikerjakan selama x hari. 
#Tulislah algoritma untuk mengkonversi berapa tahun, berapa bulan, 
#dan berapa hari proyek tersebut dikerjakan. 
#Asumsikan : 1 tahun = 365 hari, 1 bulan = 30 hari. 
#Keluaran (tahun, bulan, hari) ditampilkan ke piranti keluaran

#Algoritma
#1. Mulai
#2. Input jumlah hari proyek dikerjakan (x)
#3. Hitung jumlah tahun dengan membagi jumlah hari dengan 365
#4. Hitung sisa hari setelah dikonversi ke tahun dengan menggunakan modulus
#5. Hitung jumlah bulan dengan membagi sisa hari dengan 30
#6. Hitung sisa hari setelah dikonversi ke bulan dengan menggunakan modulus
#7. Tampilkan hasil konversi (tahun, bulan, hari)
#8. Selesai 

# Implementasi dalam kode Python
x = int(input("Masukkan Jumlah Hari Proyek :"))

Tahun = x // 365
SisaTahun = x % 365

Bulan = SisaTahun // 30
Hari = SisaTahun % 30

print("Hasil Konversi :", x, "Hari Adalah,", Tahun, "Tahun,", Bulan, "Bulan,", Hari, "Hari")