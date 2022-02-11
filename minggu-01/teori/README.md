# INSTALASI DAN PENGGUNAAN INTERPRETER PYTHON (Pertemuan 1)
#
## A. Latar Belakang

Penggunaan teknologi dalam beberapa dekade belakangan sebagai salah satu kebutuhan manusia modern. Sejak ditemukan hingga saat ini pun, segala sesuatunya pasti memiliki keterkaitan dengan teknologi. Dan tak dapat dipungkiri, bahwa dengan berkembangnya zaman, teknologi pun semakin berkembang pesat. 

Hal mendasar yang sangat berperan penting pada perkembangan teknologi ini adalah perkembangan pada perangkat lunak. Saat ini ada banyak ragam jenis Bahasa pemrograman yang digunakan, seperti C/C++/Java. Penggunaan Bahasa-bahasa pemrograman ini, tentu saja dapat membuat tugas para pengembang perangkat lunak menjadi lebih mudah. Namun, terdapat kendala dalam penggunaan beberapa Bahasa pemrograman tertentu. Seperti, siklus tulis/kompilasi/uji/kompilasi ulang biasanya berjalan terlalu lambat, memakan banyak waktu, tidak cocok untuk pengembangan aplikasi tertentu dan masih banyak lagi.

Walaupun begitu, masih ada Bahasa pemrograman yang dapat digunakan oleh seorang pengembang dalam merancang dan mengimplementasikan Bahasa yang ia gunakan kedalam sebuah aplikasi didalam perangkat lunak, yaitu Python. Python lebih mudah digunakan dan tersedia diberbagai system operasi dan dapat membantu pengembang untuk menyelesaikan tugasnya dengan cepat. 

Berdasarkan uraian latar belakang diatas, maka akan dibuat sebuah laporan workshop yang membahas tentang apa itu Python? Bagaimana kegunaannya? Dan bagaimana cara penginstalannya didalam sebuah perangkat lunak.


## B. Dasar Teori

Python merupakan salah satu Bahasa pemrograman interpretatif yang dianggap mudah dipelajari serta berfokus pada keterbacaan kode. Dengan kata lain, python diklaim sebagai Bahasa pemrograman yang memiliki kode-kode pemrograman yang sangat jelas, lengkap, dan mudah dipahami. 
Python secara umum berbentuk pemrograman yang berorientasi objek, pemrograman imperatif, dan pemrograman fungsional. Istilah lainnya, Bahasa pemrograman multi-paradigma. 
Dikarenakan memiliki struktur data tingkat tinggi yang efesien dan pendekatan yang sederhana namun efektif. Python menjadi Bahasa pemrograman yang kerap kali digunakan diberbagai keperluan pengembangan perangkat lunak dan dapat berjalan diberbagai *platform* system operasi. 

Python adalah Bahasa yang ditafsirkan, yang dapat menghemat banyak waktu seorang pengembang program selama melakukan pengembangan program karena tidak diperlukan kompilasi dan penautan. Penerjemah (*Interpreter*) dapat digunakan secara interaktif, yang memudahkan untuk bereksperimen dengan fitur Bahasa, menulis ulang program ataupun menguji fungsi selama pengembangan berjalan. 
Python memungkinkan program ditulis dengan ringkas dan mudah dibaca. Program yang ditulis dengan python biasanya jauh lebih pendek daripada Bahasa pemrograman lainnya yang setara, karena beberapa alasan :
    1.	tipe data tingkat tinggi memunkinkan pengembang untuk  mengekspresikan operasi kompleks dalam satu pernyataan.
    2.	Pengelompokkan pernyataan dilakukan dengan indentasi alih-alih tanda kurung awal dan akhir.
    3.	Tidak diperlukan deklarasi variable atau argumen. 


## C. Penggunaan Penerjemah (Interpreter) Python
### 1. Meminta Penerjemah (Interpreter)
Penerjemah (*Interpreter*) python biasanya dapat diinstal melalui komputer lokal dan apabila telah berhasil terinstal, maka akan perintah akan tersedia. Jika seorang pengembang (*user*) menginstal py.exe *launcher*, maka perintah py dapat digunakan. 

Fitur penyuntingan baris penerjemah mencakup penyuntingan interaktif, pergantian riwayat dan penyelesaian kode pada sistem yang mendukung *library GNU Readline*. Pada sistem operasi windows beberapa modul python juga berguna sebagai skrip. 

Berikut ini merupakan tampilan yang akan diperoleh jika  *interpreter* Python berhasil terinstal (tampilan yang didapat adalah hasil operasi yang dilakukan lewat cmd komputer lokal saya).

```shell
$python3.11
Python 3.11.0a5 (main, Feb 3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32 
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

#### 1.1 Penulisan Argumen (Argument Passing)

Pada saat bahasa program berhasil diterjemahkan oleh interpreter. Nama skrip dan argumen tambahan setelahnya dapat diubah menjadi list string dan ditetapkan menjadi “argv” variabel dalam “sys” modul. List ini dapat diakses dengan mengeksekusi “import sys”. Jika tidak terdapat skrip atau argumen didalamnya, “sys.argv[0]” output yang akan diperoleh akan berupa :

```python
>>> import sys
>>> sys.argv[0]
''
>>> sys.argv
['']
```

Ketika nama skrip diberikan sebagai inputan standar lalu di setel saat perintah digunakan lalu disetel lagi ke modul kemudian digunakan. Opsi yang akan ditemukan setelahnya akan digunakan oleh *interpreter* python tapi akan tersimpan pada “sys.argv” sebagai perintah atau modul.

#### 1.2 Mode Interaktif

Ketika perintah dibaca, *interpreter* akan berada pada mode interaktif. Dalam mode ini biasanya sistem akan meminta inputan berikutnya melalui *prompt* utama dengan diikuti oleh tiga tanda panah kekanan seperti berikut (>>>) dan untuk perintah selanjutnya akan dilanjutkan melalui *prompt* kedua dengan diikuti tanda tiga titik berurutan. Penerjemah (*Interpreter*) akan mencetak sebuah pesan disertai nomor versi dan juga *copyright* sebelum akhirnya akan dicetak pada baris paling awal di *prompt*.

Berikut ini merupakan contoh kontruksi multi-baris dengan menggunakan *statement* if :

```python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...    print("Be careful not to fall off!")
...
Be careful not to fall off!
>>>
```

### 2. Interpreter dan Lingkungannya
#### 2.1 Source Code

Secara default, sumber file python memiliki kode UTF-8. Dalam pengkodean tersebut, karakter sebagian besar bahasa di dunia dapat digunakan secara bersamaan dalam literal string, pengidentifikasian dan komentar.
Meskipun begitu, dalam standar library karakter yang digunakan masih karakter ASCII untuk pengidentifikasian, dan segala jenis kode portabelnya masih harus mengikuti.

Berikut ini merupakan sintaks yang dapat digunakan :

```python
>>> # -*- coding: encoding -*-
>>> # -*- coding: cp1252 -*-
>>> #!/usr/bin/env python3
>>> # -*- coding: cp1252 -*-
```

## D. Pengantar Informal Python

Pada bagian ini, input dan output dibedakan dengan ada atau tidaknya prompt (>>> dan ..). Agar perintah dapat dijalankan, perintah tersebut haruslah diketik setelah prompt terbuat, baris yang tidak dimulai dengan prompt adalah output dari interpreter. Perintah sekunder pada baris diketikkan baris kosong agar perintah multi-baris dapat diakhiri penggunaannya. 

Untuk memulai komentar pada python dapat diawali dengan menuliskan karakter hash (#) dan diperpanjang hingga baris fisik. 

Berikut contoh penggunaannya :

```python
>>> # this is the first comment
>>> spam = 1 # and this is the second comment
             # ... and now is third!
>>> text = "# This is not a comment because it's inside quotes."
```

### 1. Penggunaan Python Sebagai Kalkulator
#### 1.1 Angka

Penerjemah (Interpreter) bertindak sebagai kalkulator sederhana dengan menjalankan ekspresi padanya. Berikut ini sintaks ekpresi mudah : operator +, - , * dan / bekerja seperti pada bahasa pemrograman lainnya.

```python
>>> 2 + 2
4
>>> 30 - 12*2
6
>>> (90 - 25*3) / 5
3.0
>>> 26 / 5 # Pembagian akan selalu menghasilkan output dengan tipe data float atau nilai pecahan
5.2 
>>>
```

Jika dilihat pada potongan skrip diatas dapat diketahui bahwa, bilangan bulat seperti 2, 4, 6 dst mempunyai tipe data integer. Dan untuk bilangan pecahan dalam tipe data float. 

Pembagian (/) dapat mengembalikan nilai dari tipe data float. Jika tanda pembagian bertingkat (//) dinputkan, maka nilai yang seharusnya bernilai pecahan akan bulatkan oleh kompiler. Dan untuk menghitung sisa nilai yang tidak tercatat pada output dapat menggunakan karakter persen (%) :

```python
>>> 15 / 5 # Pembagian akan selalu menghasilkan output dengan tipe data float
3.0
>>> 15 // 5 # Pembagian bertingkat akan mengembalikan nilai dengan tipe data integer
3
>>> 15 % 5 # Operator % akan menghitung nilai sisa
0
>>> 3 * 5 + 0 # Hasil pembagian bertingkat * hasil bagi + nilai sisa
15
>>>
```

Operator “**” pada python dapat mengembalikan nilai berupa nilai perpangkatan. Sedangkan untuk operator “=” dapat digunakan untuk memberi nilai pada variabel, nilai pada variabel akan dipanggil ketika user mengetikkan nama variabel. Namun, jika suatu variabel tidak didefenisikan atau tidak diberi nilai, maka output yang akan didapatkan adalah error. Selain itu, dalam mode interaktif juga ekspresi terakhir dapat ditetapkan ke variabel “_” yang menunjukan penggunaan python sebagai kalkulator meja dan akan mempermudah perhitungan nilai. 

```python 
>>> 5 *** 2 # 5 Kuadrat
25
>>> 2 ** 7 
128
>>> width = 35
>>> height = 6 * 5
>>> width * height
1050
>>> n # Mencoba mengakses variabel yang tidak didefenisikan 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> 3 * 2.12 - 8
-1.6399999999999997
>>> tax = 42.2 / 53
>>> price = 100.30
>>> price * tax
79.86150943396227
>>> price +_
180.16150943396227
>>> round(_, 2)
180.16
```


#### 1.2 String

Selain angka, python juga dapat memanipulasi nilai string yang dapat diekspresikan dalam beberapa cara. Nilai string biasanya akan ditandai dengan kutip tunggal (‘...’) atau kutip ganda (“...”) dan akan menghasilkan output yang sama.

```python
>>> 'spam eggs' # Kata Tunggal
'spam eggs'
>>> 'doesn\'t' # Menggunakan \' untuk membendung kata tunggal
"doesn't"
>>> "doesn't" # atau menggunakan dua tanda kutip
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes, \" they said."
'"Yes, " they said.'
>> '"Isn\'t, " they said.'
'"Isn\'t," they said.'
```

Dalam mode interpreter interaktif, nilai string biasanya diapit oleh tanda kutip ataupun karakter tertentu. Meskipun begitu, output yang didapat kadang kala akan berbeda dari inputannya. Adapun fungsi print() dapat menghasilkan output berupa nilai string yang inputkan dengan menghilangkan tanda kutipnya.

```python
>>> s = 'First line.\nSecond line.' # \n berarti garis baru
>>> s # Tanpa menggunakan perintah print(), \n adalah include dari output
'First line.\nSecond line.'
>>> print(s) # Dengan perintah print(), \n akan membuat baris baru
First line.
Second line.
>>>
```

Menambahkan karakter ‘r’ pada baris untuk string mentah sebelum kutipan pertama, menambahkan tanda kutip tiga (“””...”””) atau (‘’’...’’’) lalu menambahkan \ diakhir baris, menggabung string dengan operator, dan menggabungkan dua nilai pada kutip berbeda. 

```python
>>> print('C:\some\name') # \n mengundang arti memulai baris baru
C:\some
ame
>>> print("""\
... Usage: thingy [OPTIONS]
...       -h                    Display this usage message
...       -H hostname           Hostname to connect to
... """)
Usage: thingy [OPTIONS]
      -h                   Display this usage message
      -H hostname          Hostname to connect to

>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' 'thon'
'Python'
```

Fitur pada python ini dapat membantu user untuk menghubungkan kalimat yang terputus, namun hanya akan berfungsi pada dua literal saja tidak dengan variabel atapun ekspresi, jika ingin menggabungkan keduanya diharuskan untuk menggunakan operator “+”.

```python
>>>  text = ('Hari ini jauh berbeda dengan hari-hari sebelumnya ' 'begitu juga esok.')
>>> text
'Hari ini jauh berbeda dengan hari-hari sebelumnya begitu juga esok.'
>>> prefix = 'Py'
>>> prefix 'thon' # Dengan perintah seperti dua literal tidak dapat digabungkan dengan variabel dan string literal

File "<stdin>", line 1
  prefix 'thon' # Dengan perintah seperti dua literal tidak dapat digabungkan dengan variabel dan string literal
        ^^^^^^
SyntaxError: invalid syntax
>>> ('tres' * 5) 'quatro'
   File "<stdin>", line 1
     ('tres' * 5) 'quatro'
                  ^^^^^^^^
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
>>>
```

Nilai string dapat diindeks dengan karakter pertama yang memiliki indeks 0 dan tidak membutuhkan karakter yang terpisah, indeks juga bisa berupa angka negatif, yang nantinya akan dihitung dari kanan, karena nilai -0 sama dengan 0 maka indeks negatif akan dimulai dari -1. Selain pengindeksan, pengirisan juga didukung. Sementara pengindeksan digunakan untuk mendapatkan karakter individu, slicing memungkinkan untuk mendapatkan nilai dari substring.


```python
>>> prefix + 'thon'
'Python'
>>> word = 'Python'
>>> word[0] # karakter berada di posisi ke 0
'p'
>>> word[5] # karakter berada di posisi ke 5
'n'
>>> word[-1] # karakter terakhir
'n'
>>> word[-2] # karakter kedua sebelum akhir
'o'
>>> word[-6]
'p'
>>> word[0:2] # karakter dari posisi ke 0 akan include ke posisi ke 2
'Py'
>>> word[2:5] # karakter dari posisi ke 2 akan include ke posisi ke 5
'tho'
>>>
```

Indeks irisan memiliki nilai default yang berguna, indeks pertama yang dihilangkan oleh nilai defaultnya adalah 0, indeks kedua yang dihilangkan defaultnya adalah ukuran string yang didapat. Perhatikan bagaimana karakter awal selalu disertakan, dan akhir selalu dikecualikan, ini memastikan bahwa nilainya akan selalu sama dengan : s[:i] + s[i:]s. Salah satu cara untuk mengingat cara kerja irisan adalah dengan menganggap indeks sebagai penunjuk antar karakter, dengan tepi kiri karakter pertama bernomor 0. Kemudian tepi kanan karakter terakhir dari string n karakter memiliki indeks n. 

```python
>>> word[:2] # karakter dari posisi awal ke posisi 2 (exclude)
'Py'
>>> word[4:] # karakter dari posisi ke 4 akan include ke posisi akhir
'on'
>>> word[-2:] # karakter dari posisi kedua sebelum akhir (include) ke posisi akhir
'on'
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
>>> word[42]
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>>
```

Namun, indeks irisan di luar jangkauan akan digunakan untuk mengiris, string python tidak dapat diubah, oleh karena itu menetapkan ke posisi yang diindeks dalam string akan menghasilkan output yang error. Agar outputnya dapat dihasilkan, maka string yang inputkan harus berbeda dengan membuat yang baru. Adapun funsgi len() pada python adalah untuk mengembalikan panjang string.

```python
>>> word[4:42]
'on'
>>> word[42:]
''
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assigment
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
>>>
```


#### 1.3 Daftar

Python mengenal sejumlah jenis tipe data gabungan yang digunakan untuk mengelompokkan nilai-nilai lain dan diantaranya adalah daftar/list, yang dapat ditulis sebagai daftar nilai (item) yang dipisahkan koma di antara tanda kurung siku. Daftar mungkin berisi item dari jenis yang berbeda, tetapi biasanya semua item memiliki jenis tipe data yang sama. Seperti string dan semua jenis urutan bawaan lainnya. Semua operasi irisan mengembalikan daftar baru yang berisi elemen yang diminta. 

```python
>>> squares = [1,4 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0] # mengembalikan nilai indeks
1
>>> squares[-1]
25
>>> squares[-3:] # mengiris kembali daftar baru
[9, 16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]
>>>
```

Daftar juga mendukung penggunaan operasi gabungan, tidak seperti string yang tidak dapat diubah, daftar adalah jenis tipe data yang dapat diubah. 

```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cubes = [1, 3, 6, 9, 15, 63, 324]
>>> 2 ** 9
512
>>> cubes[2]
6
>>> cubes
[1, 3, 6, 9, 15, 63, 324]
>>> cubes.append(216) 
>>> cubes.append(7 ** 3)
>>> cubes
[1, 3, 6, 9, 15, 63, 324, 216, 343]
>>>
```

Penetapan irisan juga dimungkinkan dan ini bahkan dapat mengubah ukuran daftar atau menghapus seluruhnya. Fungsi len() juga dapat digunakan pada tipe daftar ini. Dan dimungkinkan untuk membuat daftar bersarang yang memuat daftar berisi daftar lainnya. 

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # memindahkan values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # kemudian menghapus beberapa values
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # membersihkan daftar dan memindahkan semua elemen yang ada di daftar kosong
>>> letters[:] = []
>>> letters
[]
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>>
```
### 2. Langkah - langkah programming

Dengan Python, penyelesaian masalah yang rumit dapat terselesaikan. Sebagai contoh, menulis sub-urutan awal dari deret Fibbonaci. 

```python
>>> # Deret Fibbonaci:
    # Nilai dari dua elemen akan didefenisikan setelahnya
>>> a, b = 0, 1
>>> while a < 10:
...       print(a)
...       a, b = b, a+b
...
0
1
1
2
3
5
8
>>>
```

Dalam potong skrip diatas menunjukkan beberapa fitur, yakni :
    •	Baris pertama yang berisi statemen = variabel a dan b secara bersamaan mendapatkan nilai bari 0 dan 1. Pada baris terakhir, kedua variabel tersebut digunakan lagi dan menunjukkan bahwa ekspresi di sisi kanan semuanya dievaluasi terlebih dahulu sebelum penugasan dilakukan. Ekspresi sisi kanan dievaluasi dari kiri ke kanan. 
    •	Perintah looping untuk while akan dijalankan ketika kondisi pada variabel ‘a’ bernilai benar. 
    •	Tubuh loop diindentasi = indentasi merupakan salah satu cara Python dalam mengelompokkan pernyataan. Pada prompt interaktif, biasanya pengetikkan kode skrip akan mengetikkan tab atau spasi untuk membuat baris baru indentasi. 
    •	Adapun fungsi print() pada skrip adalah untuk menulis nilai argumen yang diberikan. Berbeda dengan hanya menulis ekspresi saja. 

Dalam cara menangani banyak argumen, jumlah floating point dan string. String akan dicetak tanpa perlu menggunakan tanda kutip, dan spasi akan disisipkan diantara item, sehingga didapat format data yang lebih baik. Argumen kata kunci ‘end’ juga dapat digunakan untuk menghindari pembuatan baris baru setelah output berakhir. 

```python
>>> i = 125*125
>>> print('Value dari variabel i adalah ', i)
Value dari variabel i adalah 15625
>>> a, b = 0, 1
>>> while a < 1000:
...       print(a, end=',')
...       a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,>>>
```


## Kesimpulan

Python merupakan salah satu bahasa pemrograman yang banyak digunakan oleh seorang pengembang perangkat lunak, selain karena bahasanya yang mudah dipahami. Python juga mendukung banyak sistem operasi dalam penggunaannya. Secara umum, Python merupakan pemrograman yang berorientasikan objek, pemrograman imperatif dan juga pemrograman fungsional, maka dari itu dijuluki sebagai bahasa pemrograman multi-paradigma. 