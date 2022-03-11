# Input & Output (Pertemuan 5)

## A. Latar Belakang
Pada umumnya setiap bahasa pemrograman mempunyai ragam fungsi yang mendukung untuk tiap operasi. Salah satu fungsi standar yang selalu melekat pada bahasa pemrograman terlebih Python adalah I/O atau (Input dan Output). Fungsi ini membantu banyak pengembang dalam menyelesaikan sebuah permasalahan, dengan input seorang pengembang dapat mengetikkan perintah dari teks editor kedalam program dan dengan output seorang pengembang akan menerima hasil dari perintah yang sebelumnya dituliskan. 
Walaupun fungsi I/O merupakan fungsi standar, tentu saja penerapannya pada setiap bahasa pemrograman akan berbeda-beda. Maka dari itu, pada laporan workshop ini akan mengulas seputar apa itu I/O di Python, apa perbedaannya dengan pemrograman lain dan bagaimana seharusnya penulisan sintaks yang benar untuk fungsi standar ini di Python. 

## B. Dasar Teori
Hal mendasar dari suatu program adalah jika ia mampu memperoleh data yang dimasukkan oleh seorang pengembang dan menampilkan hasil keluarannya kembali kepada seorang pengembang/user. Pada dunia programming hal ini disebut sebagai input dan output. Dalam berbagai bahasa pemrograman kedua cara tersebut sudah diwakili oleh suatu fungsi dengan nama yang berbeda-beda untuk setiap bahasa. Pada python, fungsi untuk mendapatkan data masukkan secara manual adalah input(), sedangkan yang bertindak untuk menampilkan hasil proses dari data masukan tadi adalah print(). Keduanya merupakan fungsi bawaan python atau sebutan lainnya built-in function. 

Dengan menggunakan fungsi input() pengembang dapat memasukkan data secara manual dengan teks editor tanpa perlu mengubahnya secara langsung melalui kode sumber programnya. 

Fungsi input() akan memberi jeda atau menghentikan sementara program sampai pengembang memasukkan data ke dalamnya, ketika data sudah dimasukkan, selanjutnya program akan berjalan kembali dan kemudian memproses data inputan pengembang tadi.

Setelah data dimasukkan lalu diproses, bagaimana cara pengembang mengetahui hasil dari pemrosesan tersebut? atau bagaimana sih komputer dapat memberitahukan hasil keluaran program pada usernya? Untuk menjawab pertanyaan tersebut gunakan fungsi print().

Fungsi print() juga dapat menginformasikan pada pengembang versi python yang digunakan suatu program. Jadi jika seorang pengembang menemukan program dengan deklarasi print() di dalamnya maka dapat dipastikan program tersebut sudah menggunakan versi python 3 ke atas. Sedangkan jika di dalam program tersebut ditemukan deklarasi print tanpa tanda kurung, maka dapat dipastikan program tersebut menggunakan python versi lama. Python 2.7 ke bawah.

## C. I/O
Terdapat beberapa cara untuk menampilkan output dari suatu program di Python, data tersebut dapat dicetak kedalam bentuk tulisan yang dapat dibaca oleh manusia atau bisa juga ditulis kedalam file yang sewaktu-waktu dapat digunakan lagi dikemudian hari. 

### 1. Pemformatan Output yang Lebih Menarik
Kadang kala seorang pengembang ingin melakukan pengontrolan terhadap pemformatan output dari program miliknya daripada hanya sekedar mencetak sebuah nilai yang dipisahkan oleh spasi. Terdapat beberapa cara untuk melakukan pemformatan output tersebut :

    * Menggunakan literal string berformat :
    ```python
    >>> year = 2016
    >>> event = 'Referendum'
    >>> f'Result if the {year} {event}'
    'Result of the 2016 Referendum'
    ```

    * Menggunakan metode str.format() :
    ```python
    >>> yes_votes = 42_572_654
    >>> no_votes = 43_132_495
    >>> percentage = yes_votes / (yes_votes + no_votes)
    >>> '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
    ' 42572654 YES votes 49.67%'
    ```

    * Melakukan semua penanganan string sendiri menggunakan operasi pengirisan string dan penggabungan tata letak data.

Kebutuhan menggunakan output yang dapat ditampilkan dengan cepat hanya dari beberapa buah variabel yang perlu untuk di debug dapat dikonversikan kenilai apa saja menjadi string dengan menggunakan fungsi repr() / str().

Fungsi str() ini dimaksudkan untuk melakukan pengembalian nilai representasi yang cukup untuk dibaca manusia saja, sedangkan untuk fungsi repr() hanya dapat menghasilkan nilai representasi yang sekedar dapat dibaca oleh *interpreter* saja. 

Berikut ini merupakan contoh penggunaan fungsi str() dan fungsi repr() :

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

#### a. Literal String Terformat (f-string)
Dengan literal string terformat (t-string) seorang pengembang dimungkinkan untuk memasukkan nilai ekspresi Python di dalam string dengan mengawali string dengan perintah 'f' atau 'F' dan menulis ekspresi nya "{expression}". Penentuan format ini bersifat opsional sehingga dapat mengikuti ekspresi yang digunakan. 

Berikut ini contoh penggunaan f-string :
```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142'
```

Atau bisa juga dengan melewati bilangan bulat setelah ":" yang dapat membuat jumlah karakter menjadi minimum :
```python
>>> table = {'Ondu': 4001, 'Sabeom': 1321, 'Bangjeon': 5214, 'Jokwon': 3920}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...     
Ondu       ==>       4001
Sabeom     ==>       1321
Bangjeon   ==>       5214
Jokwon     ==>       3920
```

Alternatif lain yang dapat digunakan untuk mengonversikan nilai juga sebelum di format adalah menggunakan '!a' yang berlaku sebagai ascii(), '!s' berlaku sebagai str() dan '!r' berlaku sebagai repr(). Berikut contoh penggunaannya :
```python
>>> animals = 'Quokka'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of Quokka.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'Quokka'.
```

#### b. Method Format String() / str.format()
Penggunaan metode format string() dapat dilakukan dengan menuliskan perintah str.format(), berikut contoh penggunaannya :
```python
>>> print('Find your {} Hi we are "{}!"'.format('Treasure', 'Treasure'))
Find your Treasure Hi we are "Treasure!"
```

Tanda kurung dan karakter yang berada didalam *source code* diatas dapat sebut sebagai bidang format yang dapat digantikan dengan objek yang dapat diteruskan ke method str.format(). Sedangkan untuk angka yang berada didalam tanda kurung kurawal akan merujuk pada posisi objek yang akan disimpan sesuai dengan method str.format() perintahkan. Berikut contoh penggunaannya :
```python
>>> print('{0} and {1}'.format('merch', 'lightstic'))
merch and lightstic
>>> print('{1} and {0}'.format('merch', 'lightstic')) 
lightstic and merch
```

Sedangkan untuk penggunaan argumen sebagai kata kunci menggunakan method str.format() akan dipanggilkan nilainya dari nama argumen yang dibuatkan oleh pengembang. Contohnya :
```python
>>> print('This {food} is {adjective}.'.format( 
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

Posisi atau letak dari argumen dan kata kunci juga dapat digabungkan kedalam satu kalimat, Contohnya :
```python
>>> print('Once upon {0} in the {1}, the world must be {other}.'.format('fish', 'sky', other='weird'))
Once upon fish in the sky, the world must be weird.
```

Terdapat sebuah alternatif jika pengembang memiliki string format yang sangat panjang namun tak ingin memisahkan data yang ada didalam programnya. Hal tersebut dapat dilakukan dengan hanya melewatkan *dictionary* dan menggunakan tanda '[]' saja untuk mengakses kuncinya, berikut contoh penggunaannya :
```python
>>> table = {'Ondu': 4001, 'Sabeom': 1321, 'Bangjeon': 5214, 'Jokwon': 3920}
>>> print('Bangjeon: {0[Bangjeon]:d}; Jokwon: {0[Jokwon]:d}; ' 
...     'Ondu: {0[Ondu]:d}; Sabeom: {0[Sabeom]:d}'.format(table))
Bangjeon: 5214; Jokwon: 3920; Ondu: 4001; Sabeom: 1321
```

Atau bisa juga dengan menggunakan kata kunci yang memiliki notasi ** didalam programnya, seperti :
```python
>>> table = {'Ondu': 4001, 'Sabeom': 1321, 'Bangjeon': 5214, 'Jokwon': 3920}
>>> print('Bangjeon: {Bangjeon:d}; Jokwon: {Jokwon:d}; Ondu: {Ondu:d}; Sabeom: {Sabeom:d}'.format(**table))
Bangjeon: 5214; Jokwon: 3920; Ondu: 4001; Sabeom: 1321
```

Adapun untuk penerapan baris yang dapat menghasilkan kumpulan kolom yang tersusun rapi serta bilangan bulat, kuadrat dan kubusnya dapat dituliskan seperti berikut ini :
```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
... 
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```


#### c. Pemformatan String Manual / str.rjust()
Contoh penggunaan pemformatan string manual untuk membuat tabel kotak dan kubus yang sama :
```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
... 
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Penggunaan metode str.rjust() sebagai objek string akan bertugas untuk membenarkan setiap string yang berada di bidang dengan lebar tertentu dengan mengisi nilainya dulu dengan spasi dari sebelah kiri. Adapun metode yang serupa dengannya adalah str.ljust() dan str.center().  

Pada dasarnya metode str.rjust() ini tidak akan menuliskan kembali nilaii apapun dan hanya akan mengembalikan string baru saja. Hal ini berlaku ketika string input terlalu panjang dan tidak dipotong. Tentu saja tindakan tersebut akan menyebabkan tata letak kolom menjadi kacau dan tidak beraturan. Untuk mengantisipasinya terdapat satu alternatif yang dapat dilakukan yakni dengan berbohong tentang nilai yang dipakai. Berikut ini contoh penggunaannya dengan menggunakan metode str.zfill() :
```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

#### d. Pemformatan String Lama
Penggunaan operator % (modulo) juga dapat digunakan untuk melakukan pemformatan string sebagai pengganti nilai sebenarnya dengan nilai nol atau elemen dari sebuah operasi. Operasi ini biasanya disebut *Interpolasi string*. Berikut ini contoh penggunannya :
```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

### 2. Membaca dan Menulis File
Fungsi open() pada Python dapat digunakan untuk membuka sebuah objek file dan juga dapat membacanya serta mengembalikan lagi nilainya. perintah yang kerap kali digunakan untuk menggunakan fungsinya ialan open(filename, mode). Atau :
```python
>>> f = open('workfile', 'w')
```

Argumen pertama yang akan dibaca akan berupa string yang berisi nama dari file, sedangkan untuk argumen kedua nilai yang dibaca adalah string berisi beberapa karakter yang menjelaskan cara file tersebut digunakan. Beberapa mode yang bisa digunakan selain 'w' adalah 'r' untuk membaca file, 'a' untuk membuka file yang ditambahkan, 'b' agar file dapat dibuka dalam mode biner.

Ada kalanya, file yang terbuka berada dalam mode teks atau tulisan yang berarti seorang pengembang yang mengaksesnya dapat membaca dan menulis lagi stringnya dari dan ke file tersebut dengan kode program tertentu. 

Ketika berada dalam mode teks tersebut, defaultnya akan membaca (Mengonversi akhiran baris khusus di platform tertentu) menjadi hanya \n. Pemodifikasian file sebenarnya baik namun dapat merusak data biner yang berbentuk file JPEG/file EXE. Maka dianjurkan untuk berhati-hati saat penggunaan dalam mode biner. 

Berikut ini merupakan contoh penggunaan membaca dan membuka file dengan kata kunci 'with' :
```python
>>> with open('workfile') as f:
... read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```
    
    Note :
    Memanggil fungsi f.write() tanpa menyertakan penggunaan kata kunci with atau panggilan f.close() dapat mengakibatkan argumen untuk f.write() tidak dapat sepenuhnya dituliskan ke disk bahkan ketika output diterima. 

Maka dari itu setelah sebuah objek file ditutup baik itu menggunakan kata kunci with atau fungsi f.close() upaya untuk menggunakan objek file tersebut akan otomatis gagal dilakukan.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

#### a. Method Objek File
Untuk membaca konten atau isi dari sebuah file dapat dilakukan dengan menjalankan fungsi f.read(size), fungsi ini akan membaca sejumlah data didalam file dan mengembalikannya sebagai nilai string ataupun bentuk objek byte (biner). *size* yang dimaksudkan disini adalah argumen numerik yang bersifat opsional. Yang mana ketika ukuran dihilangkan atau negatif maka seluruh isi file akan dibaca dan dikembalikan namun akan memakan ruang yang lebih besar pada memori atau tempat penyimpanan. Berikut ini contoh penggunaannya :
```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

Selain perintah dengan fungsi f.read(), fungsi f.realine() juga dapat digunakan untuk membaca satu baris dari sebuah file. Seperti :

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

Pembacaan baris file dengan mengulang objek file juga dapat dilakukan jika pengembang ingin melalukan penyesuaian memori agar lebih hemat, cepat dan lebih sederhana. Berikut contoh penerapannya :
```python
>>> for line in f:
...    print(line, end='')
...
This is the first line of the file.
Second line of the file
``` 

Adapun hal yang dapat dilakukan jika pengembang ingin menulis isi dari string kedalam file dan ingin mengembalikan jumlah karakter yang ditulis, pengembang cukup menuliskan fungsi f.write(string) kedalamnya :
```python
>>> f.write('This is a test\n')
15
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

Fungsi f.tell() akan mengembalikan nilai berupa bilangan bulat yang memberikan posisi untuk objek file yang saat ini tengah direpresentasikan sebagai jumlah byte dari awal file saat berada dalam mode biner dan angka buram ketika dalam mode teks. 

Untuk melakukan perubahan terhadap posisi untuk objek file tadi akan dilakukan perhitungan untuk posisinya lalu akan ditambahkan offset ke titik referensi yang telah dipilih oleh argumen where. Agar lebih jelas lagi berikut contoh penerapannya pada Python :
```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

#### b. Menyimpan Struktur Data Dengan Json
Nilai sebuah string dapat dengan mudah ditulis ataupun dibaca jika berbentuk sebuah file. Sedangkan untuk sebuah angka akan membutuhkan sedikit usaha, karena fungsi dari metode read() hanya mengembalikan nilai string saja. Maka untuk sebuah angka akan diteruskan dulu ke fungsi lainnya seperti int() sebelum akhirnya dapat terbaca. 

Daripada membuat pengembang terus - menerus menulis dan mendebug kode lalu menyimpannya menjadi tipe daya yang rumit menjadi bentuk file, maka Python menyediakan solusi untuk memudahkan format pertukaran data yakni dengan JSON (JavaScript Object Notation). Json merupakan modul standar yang dapat dipanggil untuk mengambil hirarki data di Python dan dapat mengubahnya menjadi representasi string. 

Berikut ini merupakan contoh penggunaan modul json di Python, pada contoh ini objek yang digunakan adalah x :
```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

Varian lain dari fungsi dumps() yang digunakan pada *source code* diatas adalah dump() yang fungsinya adalah membuat serial objek menjadi file teks. 
```
json.dump(x, f)
```

Sedangkan untuk memecahkan kode didalamnya dapat dilakukan dengan menggunakan kata kunci 'f' agar objek file terbuka. 
```
x = json.load(f)
```

## D. Kesimpulan
Fungsi I/O termasuk fungsi standar yang dimiliki oleh Python untuk itu penggunaannya termasuk penting. Selain dapat menuliskan dan merepresentasikan kode yang dibuat, fungsi ini juga sangat membantu pengembang dalam menyelesaikan permasalahannya melalui kode program. 