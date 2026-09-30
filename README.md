# Simulasi Komunikasi Ciphertext dengan DES

## 1. Deskripsi

Program ini dibuat untuk mensimulasikan komunikasi dua arah antara **sender** dan **receiver** dengan menggunakan algoritma **Data Encryption Standard (DES)**.

Pada proses komunikasi, pesan yang dikirim tidak langsung dikirim dalam bentuk plaintext. Pesan terlebih dahulu dienkripsi menggunakan DES sehingga menjadi ciphertext. Ciphertext tersebut kemudian dikirim melalui koneksi TCP Socket. Setelah diterima, ciphertext didekripsi menggunakan key yang sama untuk mendapatkan plaintext.

Komunikasi dapat dilakukan dua arah, sehingga sender dan receiver dapat saling mengirim pesan.

## 2. Informasi Program

| Keterangan          | Detail                         |
| ------------------- | ------------------------------ |
| Algoritma           | DES (Data Encryption Standard) |
| Bahasa              | Python                         |
| Komunikasi          | TCP Socket                     |
| Komunikasi          | Dua arah                       |
| Key                 | `rahasiya`                     |
| Implementasi DES    | Manual                         |
| Library kriptografi | Tidak digunakan                |

Key sudah diketahui oleh sender dan receiver sejak awal dan **tidak dikirim melalui jaringan**.

## 3. Struktur File

Program terdiri dari tiga file utama:

* **`cipher.py`**
  Berisi implementasi algoritma DES, mulai dari pembentukan subkey, proses permutasi, fungsi Feistel, enkripsi, dekripsi, serta padding.

* **`sender.py`**
  Digunakan untuk mengirim pesan ke receiver dan menerima balasan dari receiver.

* **`receiver.py`**
  Digunakan untuk menerima pesan dari sender dan mengirimkan balasan.

## 4. Alur Komunikasi

Alur pengiriman pesan dari sender ke receiver adalah sebagai berikut:

**Sender → Plaintext → Enkripsi DES → Ciphertext → TCP Socket → Receiver → Dekripsi DES → Plaintext**

Sedangkan untuk balasan:

**Receiver → Plaintext → Enkripsi DES → Ciphertext → TCP Socket → Sender → Dekripsi DES → Plaintext**

Ciphertext yang dikirim juga ditampilkan dalam bentuk hexadecimal pada kedua sisi untuk menunjukkan data yang benar-benar dikirim melalui jaringan.

## 5. Key dan Padding

Key yang digunakan pada program adalah:

`rahasiya`

Key tersebut digunakan oleh kedua pihak dan tidak ikut dikirim saat proses komunikasi.

Karena DES bekerja dengan blok berukuran **8 byte**, plaintext akan diberi padding sebelum proses enkripsi. Setelah proses dekripsi selesai, padding akan dihapus kembali sehingga diperoleh plaintext asli.

Program juga melakukan penyesuaian apabila key memiliki panjang kurang dari 8 byte dengan mengulang key hingga mencapai panjang yang dibutuhkan.

## 6. Cara Menjalankan Program

Pertama, jalankan program receiver:

```
python receiver.py
```

Receiver akan menunggu koneksi dari sender.

Selanjutnya, jalankan program sender pada terminal lain:

```
python sender.py
```

Setelah berhasil terhubung, sender dapat memasukkan pesan untuk dikirim. Receiver akan menerima ciphertext, melakukan dekripsi, dan menampilkan plaintext. Receiver kemudian dapat mengirimkan balasan dengan proses yang sama.

Untuk mengakhiri komunikasi, masukkan:

```text
quit
```

## 7. Hasil Pengujian

Pengujian dilakukan dengan mengirimkan pesan dari sender ke receiver dan sebaliknya. Hasil pengujian menunjukkan bahwa pesan yang dikirim dalam bentuk ciphertext dapat diterima dan didekripsi kembali menjadi plaintext menggunakan key yang sama.

### Dokumentasi Pengujian

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/651bf249-253c-49e1-ae54-7d1605aafb78" />

## 8. Dokumentasi Wireshark

Jika dilakukan, proses pengiriman ciphertext dapat diamati menggunakan Wireshark untuk melihat data yang ditransmisikan melalui koneksi TCP.

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/ed3a6c04-2f02-42cc-8ddd-04e36118925e" />

## 9. Kesimpulan

Program berhasil mensimulasikan komunikasi dua arah antara sender dan receiver menggunakan algoritma DES. Pesan dienkripsi terlebih dahulu sebelum dikirim melalui TCP Socket dan kemudian didekripsi oleh penerima menggunakan key yang telah diketahui oleh kedua pihak. Key tidak dikirimkan selama proses komunikasi.
