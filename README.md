# Tugas Struktur Data

## Soal 01
1. Buat fungsi rekursif untuk menghitung bilangan Fibonacci ke-n
2. Gunakan fungsi yang anda buat untuk menghitung bilangan Fibonacci ke 5, 7, 10
3. Buat pohon rekursif untuk eksekusi pencarian Fibonacci ke 4

## Soal 02
1. Buat fungsi rekursif untuk mengecek apakah sebuh list bilangan integer merupakan 
palindrom atau bukan
2. Gunakan fungsi yang anda buat untuk memeriksa list berikut apakah palindrom
[1,2,3,4,4,3,2,1] atau bukan
3. Buat pohon rekursif untuk eksekusi pengecekan list berikut [1,2,3,4,4,3,2,1]

## Soal 03
Data
- panggil : bilangan >= 0 yang merepresentasikan nomor yang saat ini dilayani kasir
- antrian : bilangan >= 0 yang merepresentasikan nomor nasabah terakhir yang mengambil nomor antrian

Operasi
- upPanggil () : menaikkan nilai panggil sebanyak 1 (increment). bila sebelum operasi ini dieksekusi nilai 
panggil = antrian, maka panggil tidak diincrement.
- upAntrian () : menaikkan nilai antrian sebanyak 1 (increment). reset : memberi nilai 0 pada panggil dan 
antrian
- getPanggil() : mengembalikan (return value) nilai panggil saat ini
- getAntrian() : mengembalikan (return value) nilai panggil saat ini

1. Implementasikan ADT antrian bank menjadi struktur data
2. Gunakan struktur data anda untuk mensimulasikan kejadian berikut
    - 1 nasabah mengambil nomor antrian
    - 1 nasabah mengambil nomor antrian
    - 1 nasabah mengambil nomor antrian
    - 1 nasabah dilayani
    - 1 nasabah dilayani
    - 1 nasabah dilayani
    - 1 nasabah dilayani
    - 1 nasabah mengambil nomor antrian
    - 1 nasabah dilayani

## Soal 04
Data
- x : bilangan yang merepresentasikan koordinat x sebuah titik
- y : bilangan yang merepresentasikan koordinat y sebuah titik

Operasi
- geserHorizontal (dx) : menggeser titik secara horizontal sejauh dx (boleh ke kiri/ke kanan) 
- geserVertikal (dy) : menggeser titik secara vertikal sejauh dy (boleh ke atas/ke bawah)
- hitungJarak (titik lain) : menerima inputan titik lain yang juga bertipe titik 2D. Kemudian menghitung 
jarak antara titik ini dengan titik lain. Mengembalikan nilai (return value) jarak dalam nilai positif
- getX() : mengembalikan (return value) nilai x
- getY() : mengembalikan (return value) nilai y

1. Implementasikan ADT titik 2D menjadi struktur data
2. Gunakan struktur data anda untuk mensimulasikan kejadian berikut
    - Buat titik t1 dengan koordinat awal (2, 3)
    - Buat titik t2 dengan koordinat awal (4, 5)
    - Geserlah t1 ke kiri sebanyak 3 satuan
    - Geserlah t1 ke bawah sebanyak 7 satuan
    - Tampilkan koordinat t1 saat ini
    - Geserlah t2 ke kanan sebanyak 15 satuan
    - Geserlah t2 ke atas sebanyak 9 satuan
    - Tampilkan koordinat t2 saat ini
    - Tampilkan jarak t1 dengan t2
