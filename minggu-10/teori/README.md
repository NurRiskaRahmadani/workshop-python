# AKSES KE BASIS DATA (PERTEMUAN 10)

## A. Dasar Teori
### 1. PEP-249
PEP 249 merupakan versi 2.0 dari *database API Spesification* pada Python. API pada versi ini telah didefenisikan untuk mendorong kesamaan antara modul Python yang digunakan untuk mengakses sebuah database. 

#### a. Module Interface
1. Contructors
Akses ke database tersedia melalui objek koneksi. Maka dari itu modul haruslah menyediakan sebuah konstruktor. Seperti, connect(*parameters...*) untuk membuat koneksi menuju database. 

2. Globals
Modul secara global biasanya didefenisikan melalui beberapa hal, seperti : 
* **apilevel**
* **threadsafety**
* **paramstyle**

3. Exceptions
Sebuah modul haruslah memuat informasi kesalahan melalui exception ataupun melalui subkelas, seperti : 
* **Warning**
* **Error**
* **InterfaceError**
* **DatabaseError** 
* **DataError**
* **OperationalError**
* **IntegrityError**
* **InternalError**
* **ProgrammingError**
* **NotSupportedError**

```
StandardError
|__Warning
|__Error
   |__InterfaceError
   |__DatabaseError
      |__DataError
      |__OperationalError
      |__IntegrityError
      |__InternalError
      |__ProgrammingError
      |__NotSupportedError
```

#### b. Connection Objects
Sebuah *Connection objects*/objek koneksi haruslah merespon beberapa metode berikut :

1. Connection Methods
* **.close()**
* **.commit()**
* **.rollback()**
* **.cursor()**

#### c. Cursor Objects
Objek ini mewakili kursor database yang digunakan untuk mengelola konteks operasi pengambilan. Kursor yang dibuat dari sebuah koneksi yang salam tidak terisolasi, yaitu ketika setiap perubahan yang dilakukan ke database oleh kursor akan segera terlihat oleh kursor lain. 

1. Cursor Attributes
* **.description**
* **.rowcount**

2. Cursor Methods
* **.callproc(*procname*[, *parameters*])**
* **.close()**
* **.execute(*operation*[, *parameters*])**
* **.executemany(*operation, seq_of_parameters*)**
* **.fetchone()**
* **.fetchmany([ *size=cursor.arraysize* ])**
* **.fetchall()**
* **.nextset()**
* **.arraysize**
* **.setinputsizes(*sizes*)**
* **.setoutputsize(*size*[, *column*])**

#### d. Type Objects and Constructor
Kebanyakan database memerlukan inputan dengan format yang berbeda untuk mengikat parameter untuk input operasi. 

#### e. Implementation Hints for Module Authors
* Objek tanggal/waktu dapat diimplementasikan sebagai objek dari modul datetime Python.
* Contoh implementasi dari konstruktor berbasis Unix ticks
```python
import time

def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])

def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])

def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])
```
* Tipe objek yang disukai untuk objek Biner adalah tipe buffer yang tersedia dalam Python standar dimulai dengan versi 1.5.2.


### 2. Psycopg
Psycopg adalah adaptor PostgreSQL paling populer untuk bahasa pemrograman Python yang mana merupakan implementasi terlengkap dari spesifikasi untuk versi Python DB API 2.0 dan keamanan utas yang dirancang untuk aplikasi multi-utas berat yang membuat dan menghancurkan banyak kursor dan membuat sejumlah besar insert/update. Saat ini Psycopg yang paling ramah penggunaannya adalah versi Psycopg2 karena bersifat unicode. 

### 3. PyMongo
PyMongo adalah distribusi Python yang berisi alat untuk bekerja dengan MongoDB, dan merupakan cara yang disarankan untuk bekerja dengan MongoDB dari Python. 

### 4. SQLAlchemy
SQLAlchemy adalah toolkit Python SQL dan object relation mapper yang memberi pengembang aplikasi kekuatan penuh dan fleksibilitas SQL. SQLAlchemy menganggap database sebagai mesi aljabar relasional, bukan hanya sekedar kumpulan tabel. Baris dapat dipilih tidak hanya dari tabel tetapi juga gabungan dan pernyataan pemilihan lainnya.

Pendekatan keseluruhan SQLAlchemy untuk masalah ini sama sekali berbeda dari kebanyakan alat SQL/ORM lainnya, berakar pda apa yng disebut pendekatan berorientasi pujian, alih-alih menyembunyikan SQL dan detail relasional objek di balik dinding otomatisasi, semua proses diekspos sepenuhnya dalam serangkaian alat yang dapat dikomposisi dan transparan. 


## B. Akses Basis Data
1. Pengaksesan melalui Psycopg2
* Step 1. Start CockroachDB
- Create a free cluster
  a. Membuat akun CockroachDB Cloud. 
  b. Masuk ke laman akun Cloud CockroachDB.
  c. Pada laman Clusters, klik Create Cluster.
  d. Pada lama Create your cluster, pilih Serverless.
  e. Klik Create cluster. 

- Create a SQL user
    a. Memasukan username pada bagian SQL user atau gunakan opsi untuk masuk secara default.
    b. Klik Generate & save password.
    c. Salin password yang dihasilkan dan simpan di lokasi penyimpanan yang aman.
    d. Klik Next.

- Get the root certificate
    a. Pilih General connection string dari opsi pilihan Select option
    b. Buka terminal baru di komputer lokal, lalu jalankan perintah CA Cert download command pada Download CA cert section. 

- Get the connection string
    Membuak General connection string section, kemudian salin koneksi string yang disediakan dan simpan dilokasi yang aman. 

* Step 2. Get the sample code
- Kloning repo Github dengan kode sampel :
```
$ git clone https://github.com/NurRiskaRahmadani/workshop-python
```

- Kode sampel pada file example.py :
    a. Buat akun tabel dan inserts beberapa baris
    b. Lakukan transfer dana antara kedua akun dalam suatu transaksi
    c. Hapus akun dari tabel sebelum keluar dari terminal sehingga perintah dapat dijalankan kembali sebagai code contoh. 

* Step 3. Install the Psycopg2 driver
psycopg2-binary adalah satu-satunya dependensi modul pihak ketiga aplikasi sampel. 

Untuk melakukan instalasi, cukup dengan menjalankan perintah berikut :
```
$ pip install psycopg2-binary
```

* Step 4. Run the code 

2. Pengaksesan melalui SQLAlchemy
* Step 1. Start CockroachDB
- Create a free cluster
- Create a SQL user
- Get the root certificate
- Get the connection string
* Step 2. Get the sample code
* Step 3. Install the application requirements
* Step 4. Initialize the database
* Step 5. Run the code
