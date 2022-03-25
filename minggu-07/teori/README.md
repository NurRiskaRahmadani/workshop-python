# Object-Oriented Programing (OOP) di Python (Pertemuan 7)
## A. Latar Belakang
Paradigma pemrograman merupakan sebuah pendekatan atau konsep dalam menstrukturisasi suatu kode program atau dapat sebut juga sebagai cara berpikir untuk menyusun pola penulisan program. Sebagian besar bahasa pemrograman dibuat mudah untuk mengadopsi suatu paradigma tertentu, dan sebagian bahasa yang lain juga dibuat lebih mudah untuk mengadopsi paradigma yang lain. 

Terdapat tiga paradigma yang cukup populer saat ini, ketiga paradigma tersebut adalah : Fungsional, OOP dan prosedural. 

Pada laporan ini, paradigma yang akan diangkat adalah OOP. Apa itu paradigma OOP, apa saja isinya dan bagaimana implementasinya di Python. 

## B. Dasar Teori
### 1. Konsep OOP
Pemrograman berorientasi objek/*object-oriented programming* (OOP) adalah metode penataan program dengan menggabungkan properti dan perilaku terkait kedalam objek individu. 

Paradigma OOP/PBO adalah paradigma yang menjadikan semua komponen program sebagai objek. Yang mana setiap objek memiliki identitas dan tugasnya masing-masing.

Misalnya, sebuah objek dapat mewakili seseorang dengan properti seperti nama, usia, dan alamat serta perilaku seperti berjalan, berbicara, bernapas, dan berlari. Atau bisa juga mewakili email dengan properti seperti daftar penerima, subjek, dan isi dan perilaku seperti menambahkan lampiran dan mengirim.

Dengan kata lain, pemrograman berorientasi objek adalah pendekatan untuk memodelkan hal-hal konkret, dunia nyata, seperti mobil, serta hubungan antara hal-hal, seperti perusahaan dan karyawan, siswa dan guru, dan sebagainya. OOP memodelkan entitas dunia nyata sebagai objek perangkat lunak yang memiliki beberapa data yang terkait dengannya dan dapat melakukan fungsi tertentu.

Paradigma pemrograman umum lainnya adalah pemrograman prosedural , yang menyusun program seperti resep yang menyediakan serangkaian langkah, dalam bentuk fungsi dan blok kode, yang mengalir secara berurutan untuk menyelesaikan tugas.

Kuncinya adalah bahwa objek berada di pusat pemrograman berorientasi objek dengan Python, tidak hanya mewakili data, seperti dalam pemrograman prosedural, tetapi juga dalam keseluruhan struktur program.

### 2. Mendefiniskan kelas dengan Python
Struktur data primitif —seperti angka, string , dan daftar—dirancang untuk mewakili potongan informasi sederhana, seperti harga apel, nama puisi, atau warna favorit Anda. Bagaimana jika Anda ingin merepresentasikan sesuatu yang lebih kompleks?

Misalnya, katakanlah Anda ingin melacak karyawan di sebuah organisasi. Anda perlu menyimpan beberapa informasi dasar tentang setiap karyawan, seperti nama, usia, posisi, dan tahun mereka mulai bekerja.

Salah satu cara untuk melakukannya adalah dengan mewakili setiap karyawan sebagai daftar :

```
ajun = ["Arjuna Kanagara", 25, "Captain", 2265]
esa = ["Mahesa Dwinaga", 24, "Science Officer", 2254]
siel = ["Harsiello Saujana", 22, "Chief Medical Officer", 2266]
```

Ada sejumlah masalah dengan pendekatan ini.

Pertama, ini dapat membuat file kode yang lebih besar lebih sulit untuk dikelola. Jika Anda mereferensikan ajun[0]beberapa baris dari tempat ajun daftar dideklarasikan, apakah Anda ingat bahwa elemen dengan indeks 0 adalah nama karyawan?

Kedua, dapat menimbulkan kesalahan jika tidak setiap karyawan memiliki jumlah elemen yang sama dalam daftar. Dalam siel daftar di atas, usianya hilang, jadi siel[1] akan kembali "Chief Medical Officer" sebagai ganti usia Dr. Siel.

Cara yang bagus untuk membuat kode jenis ini lebih mudah dikelola dan dipelihara adalah dengan menggunakan kelas.

### 3. Kelas vs Instance
Kelas digunakan untuk membuat struktur data yang ditentukan pengguna. Kelas mendefinisikan fungsi yang disebut metode , yang mengidentifikasi perilaku dan tindakan yang dapat dilakukan oleh objek yang dibuat dari kelas dengan datanya.

Kelas adalah cetak biru untuk bagaimana sesuatu harus didefinisikan. Itu tidak benar-benar berisi data apa pun. Kelas cat menentukan bahwa nama dan usia diperlukan untuk mendefinisikan seekor kucing, tetapi tidak berisi nama atau usia kucing tertentu.

Sementara kelas adalah cetak biru, *instance* adalah objek yang dibangun dari kelas dan berisi data nyata. Sebuah *instance* dari kelas *cat* tidak lagi menjadi cetak biru. Ini adalah kucing sungguhan dengan nama, seperti ruby, yang berusia empat tahun.

Dengan kata lain, kelas seperti formulir atau kuesioner. *Instance* seperti formulir yang telah diisi dengan informasi. Sama seperti banyak orang dapat mengisi formulir yang sama dengan informasi unik mereka sendiri, banyak contoh dapat dibuat dari satu kelas.

## C. Kelas
Kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama-sama. Membuat kelas baru membuat tipe objek baru, memungkinkan *instance* baru dari tipe itu dibuat. Setiap *instance* kelas dapat memiliki atribut yang dilampirkan untuk mempertahankan statusnya. *Instance* kelas juga dapat memiliki metode (didefinisikan oleh kelasnya) untuk memodifikasi statusnya.

Dibandingkan dengan bahasa pemrograman lain, mekanisme kelas Python menambahkan kelas dengan sintaks dan semantik baru minimal. Ini adalah campuran dari mekanisme kelas yang ditemukan di C++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat mengganti metode apa pun dari kelas atau kelas dasarnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang berubah-ubah. Seperti halnya modul, kelas mengambil bagian dari sifat dinamis Python: mereka dibuat saat *runtime*, dan dapat dimodifikasi lebih lanjut setelah pembuatan.

### 1. Sepatah Kata Tentang Nama dan Objek
Objek memiliki individualitas, dan beberapa nama (dalam beberapa cakupan) dapat diikat ke objek yang sama. Ini dikenal sebagai *aliasing* dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama di Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel). 

Namun, *aliasing* memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti pointer dalam beberapa hal. 

Misalnya, melewatkan sebuah objek adalah murah karena hanya sebuah pointer yang dilewatkan oleh implementasi; dan jika suatu fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahannya — ini menghilangkan kebutuhan akan dua mekanisme penerusan argumen yang berbeda seperti dalam Pascal.

### 2. Ruang Lingkup Python dan Namespacesnya
*Namespace* adalah pemetaan dari nama ke objek. Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa mendatang. 

Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian bawaan); nama global dalam modul; dan nama lokal dalam pemanggilan fungsi. Dalam arti set atribut dari suatu objek juga membentuk *namespace*. 

Hal penting yang perlu diketahui tentang *namespace* adalah bahwa sama sekali tidak ada hubungan antara nama di *namespace* yang berbeda; misalnya, dua modul berbeda dapat mendefinisikan suatu fungsi *maximize* tanpa kebingungan — pengguna modul harus mengawalinya dengan nama modul.

*Namespaces* dibuat pada saat yang berbeda dan memiliki masa hidup yang berbeda. *Namespace* yang berisi nama bawaan dibuat saat *interpreter* Python dijalankan, dan tidak pernah dihapus. *Namespace* global untuk sebuah modul dibuat ketika definisi modul dibaca; biasanya, ruang nama modul juga bertahan hingga juru bahasa berhenti. Pernyataan yang dieksekusi oleh pemanggilan tingkat atas dari juru bahasa, baik yang dibaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut __main__, sehingga mereka memiliki *namespace* globalnya sendiri.

Ruang nama lokal untuk suatu fungsi dibuat saat fungsi dipanggil, dan dihapus saat fungsi mengembalikan atau memunculkan pengecualian yang tidak ditangani di dalam fungsi. Tentu saja, pemanggilan rekursif masing-masing memiliki *namespace* lokal mereka sendiri.

Lingkup adalah wilayah tekstual dari program Python di mana *namespace* dapat diakses secara langsung. “Dapat diakses secara langsung” di sini berarti bahwa referensi yang tidak memenuhi syarat untuk sebuah nama mencoba menemukan nama tersebut di *namespace*.

Meskipun cakupan ditentukan secara statis, mereka digunakan secara dinamis. Setiap saat selama eksekusi, ada 3 atau 4 cakupan bersarang yang ruang namanya dapat diakses secara langsung:

* lingkup terdalam, yang dicari terlebih dahulu, berisi nama-nama lokal.
* cakupan dari setiap fungsi terlampir, yang dicari mulai dengan lingkup terlampir terdekat, berisi nama non-lokal, tetapi juga non-global.
* lingkup berikutnya-ke-terakhir berisi nama global modul saat ini.
* lingkup terluar (dicari terakhir) adalah *namespace* yang berisi nama bawaan

Biasanya, lingkup lokal mereferensikan nama lokal dari fungsi (secara tekstual) saat ini. Di luar fungsi, lingkup lokal merujuk *namespace* yang sama dengan lingkup global: *namespace* modul. Definisi kelas menempatkan *namespace* lain dalam lingkup lokal.

#### a. Contoh Ruang Lingkup dan Namespaces
Contoh penerapannya kedalam *interpreter* Python :

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

Adapun output yang akan didapatkan ketika kode program diatas dijalankan :

```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```


### 3. Sudut Pandang Pertama di Kelas
#### a. Sintaks Definisi Kelas
Pada umumnya bentuk sederhana dari sintaks definisi kelas :

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-2>
```

Definisi kelas, seperti yang terdapat pada definisi fungsi pada fungsi ini juga terdapat penyataan *def* yang harus dieksekusi sebelum memiliki efek apapun pada program yang dibuat. Dalam praktiknya, pernyataan yang berada didalam definisi kelas biasanya terdiri atas definisi fungsi dan membolehkan keberadaan pernyataan lain juga.

Ketika definisi kelas dimasukkan, *namespaces* baru akan terbuat sehingga dapat digunakan sebagai lingkup lokal. Dengan demikian, semua tugas yang diberikan ke variabel lokal akan masuk ke *namespaces* baru tersebut. 

Ketika definisi kelas akan dibiarkan secara normal, maka objek kelas tersebut akan dibuat. Pada dasarnya hal tersebut adalah pembungkus konten *namespaces* yang dibuat oleh definisi kelas. 


#### b. Class Objects
*Class Objects* atau objek kelas pada Python mendukung dua jenis operasi yakni, referensi atribut dan instantiasi. 

Penulisan referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python (contoh : obj.name). Nama atribut yang valid adalah semua nama yang ada diruang nama kelas saat objek kelas dibuat. Sehinga dapat didefinisikan seperti berikut ini :

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

Kelas "MyClass.i" dan "MyClass.f" pada potongan kode diatas adalah referensi atribut yang valid, masing-masing dapat mengembalikan nilai berupa bilangan bulat dan objek fungsi. Atribut kelas juga dapat ditetapkan sehingga dapat diubah nilainya berdasarkan tugas. 

Instansiasi kelas menggunakan notasi fungsi. Saat ini objek kelas didefenisikan sebagai fungsi tanpa parameter yang dapat mengembalikan *instance* baru dari kelas. 

```
x = MyClass()
```

Operasi instansiasi akan memanggil objek kelas sehingga membuat objek kosong. Seringkali terdapat kelas yang suka membuat objek dengan *instance* yang disesuaikan dengan keadaan tertentu. Oleh karena itu, sebuah kelas dapat mendefenisikan metode khusus bernama __init__(), berikut contoh penggunaannya :

```python
>>> class Complex:                          
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
... 
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

#### c. Instance Objects
Satu-satunya operasi yang dipahami oleh objek instan adalah referensi atribut. Ada dua jenis nama atribut yang valid: atribut data dan metode.

Atribut data sesuai dengan "variabel instan" di Smalltalk, dan "anggota data" di C++. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, mereka muncul saat pertama kali ditugaskan.

Berikut ini merupakan contoh penggunaannya :
```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

Jenis referensi atribut instance lainnya adalah metode . Metode adalah fungsi yang “milik” suatu objek. (Dalam Python, istilah metode tidak unik untuk instance kelas: tipe objek lain dapat memiliki metode juga. Misalnya, objek daftar memiliki metode yang disebut append, insert, remove, sort, dan sebagainya. Namun, dalam diskusi berikut, kita akan menggunakan istilah metode secara eksklusif untuk mengartikan metode objek instance kelas, kecuali jika dinyatakan lain secara eksplisit.)

Nama metode yang valid dari objek instance bergantung pada kelasnya. Menurut definisi, semua atribut kelas yang merupakan objek fungsi mendefinisikan metode yang sesuai dari instance-nya. Jadi dalam contoh kita, x.f adalah referensi metode yang valid, karena MyClass.f merupakan fungsi, tetapi x.ibukan, karena MyClass.i bukan. Tetapi x.f tidak sama dengan MyClass.f. Ini adalah objek metode , bukan objek fungsi.

#### d. Method Objects
Biasanya, suatu metode dipanggil tepat setelah terikat :
```
x.f()
```

Dalam MyClass contoh, ini akan mengembalikan string . Namun, tidak perlu memanggil metode segera: adalah objek metode, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh:'hello world'x.f

```python
xf = x.f
while True:
    print(xf())
```

Program diatas akan terus mencetak "hello world" hingga waktu tertentu. 

#### e. Instance dan Variabel Kelas
Secara umum, variabel instan adalah untuk data yang unik untuk setiap *instance* dan variabel kelas untuk atribut dan metode yang dibagikan oleh semua *instance* kelas:

```python
>>> class Cat:        
...     kind = 'persians'
...     kind1 = 'ragdoll'
...     def __init__(self, name):
...             self.name = name
...
>>> d = Cat('Coco')
>>> e = Cat('Pinky')
>>> d.kind
'persians'
>>> e.kind1
'ragdoll'
>>> d.name
'Coco'
>>> e.name
'Pinky'
```

Data bersama yang digunakan pada "Sepatah Kata Tentang Nama dan Objek" dapat memiliki efek yang mungkin saja dapat melibatkan objek yang dapat berubah seperti daftar dan kamus. Misalnya, daftar trik dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua *instance* Kucing :

```python
>>> class Cat:  
...     tricks = []
...     def __init__(self, name):
...         self.name = name
...     def add_trick(self, trick):
...         self.tricks.append(trick)
...
>>> d = Cat('Coco')
>>> e = Cat('Pinky')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over', 'play dead']
```

```python
>>> class Cat:
...     def __init__(self, name):
...         self.name = name
...         self.tricks = []
...     def add_trick(self, trick):
...         self.tricks.append(trick)
...
>>> d = Cat('Coco')
>>> e = Cat('Pinky')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

### 4. Random Remarks
Jika terdapat atribut yang memiliki nama serupa didalam dua *instance* dan kelas, maka eksekusi akan dimulai dengan pencarian atribut yang memprioritaskan *instance*, misal :

```python
>>> class  Warehouse:                                                 
...     purpose = 'storage'
...     region = 'west'
... 
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```

Atribut data dapat direferensikan oleh metode serta oleh pengguna biasa dari suatu objek. Atau dapat dikatakan juga, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni. Karena faktanya, Python tidak memungkinkan adanya penyembunyian data secara paksa dan semuanya harus didasarkan pada konvensi nilai. Maka dari itu, penggunaan atribut data oleh pengguna biasa haruslah berhati hati. 

Objek fungsi apapun yang merupakan atribut kelas mendefinisikan metode untuk *instance* kelas tersebut. Definisi fungsi tidak perlu secara tekstual dilampirkan dalam definisi kelas melainkan dapat juga dengan menetapkan objek fungsi ke variabel lokal yang berada didalam kelas. Misalnya :

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

Atau dapat juga dengan menggunakan metode yang dapat memanggil metode lain dengan atribut metode dari *self* argumen :

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

Metode ini dapat mereferensikan nama global dengan cara yang sama seperti fungsi biasa. Lingkup global yang akan terkait dengan suatu metode adalah modul berisi definisi. Meskipun jarang ditemukan penggunaan data global dalam suatu metode, terdapat banyak penggunaan sah dari lingkup global untuk masalah yang sama. Biasanya, kelas berisi metode itu sendiri akan didefenisikan dalam lingkup global ini. 

    Note :
    Setiap nilai adalah objek, dan karena itu memiliki kelas/tipe dan disimpan sebagai object.__class__.


### 5. Inheritance
Fitur bahasa kadang kala akan didukung dengan keberadaan *inheritance* (pewarisan). Berikut ini merupakan sintaks untuk mendefiniskan kelas turunan :

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Nama *BaseClassName* haruslah didefenisikan dalam lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi arbitrer lainnya juga diperbolehkan. Tentu saja ini dapat berguna pada keadaan tertentu. Contohnya :

```python
class DerivedClassName(modname.BaseClassName):
```

Eksekusi definisi kelas turunan berlangsung sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi atribut. Jika atribut yang diminta tidak ditemukan di kelas, pencarian akan dilanjutkan untuk mencari di kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri diturunkan dari beberapa kelas lain.

DerivedClassName() membuat *instance* baru dari kelas yang ada. Referensi metodenya akan diselesaikan melalui beberapa tahap seperti, atribut kelas yang sesuai dicari, menuruni rantai kelas dasar jika perlu, dan referensi metode valid jika ini menghasilkan objek fungsi. 

Python memiliki dua fungsi bawaan yang bekerja dengan pewarisan, yakni :
* Gunakan isinstance() untuk memeriksa jenis *instance*: isinstance(obj, int) jika bernilai *True* hanya jika obj.__class__ adalah *integer* atau kelas lain yang berasal dari int. 
* Gunakan issubclass() untuk memeriksa *inheritance* : issubclass(bool, int) adalah jika nilai True didapatkan sejak diketahui bahwa *bool* merupakan *subclass* dari int. Namun, issubclas(float, int) akan bernilai *False* karena *float* bukanlah sebuah *subclass* dari int. 

#### a. Multiple Inheritance 
Python juga mendukung *Multiple Inheritance* yang memungkinkan adanya pewarisan nilai ganda. Berikut ini adalah defenisi kelas dasarnya :

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Urutan resolusi metode akan berubah secara dinamis untuk mendukung panggilan kooperatif ke super(). Pendekatan seperti ini dikenal dengan nama pewarisan ganda / *multiple inheritance*.

Pengurutan dinamis diperlukan karena semua kasus pewarisan berganda menunjukkan satu atau lebih hubungan berlian (di mana setidaknya satu kelas induk dapat diakses melalui banyak jalur dari kelas paling bawah).

### 6. Private Variables
*Private Variable* instan tidak dapat diakses kecuali dari dalam objek yang tidak ada di Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama yang diawali dengan garis bawah seperti _spam akan diperlakukan sebagai non-publik dari API dan akan dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan. 

Karena ada kasus penggunaan yang valid untuk anggota kelas-pribadi (yaitu untuk menghindari bentrokan nama nama dengan nama yang ditentukan oleh subkelas), ada dukungan terbatas untuk mekanisme seperti itu, yang disebut *name mangling*. *Mangling* ini dilakukan tanpa memperhatikan posisi sintaks dari pengenal, selama itu terjadi ketika kelas didefenisikan. 

Berikut ini merupakan contoh penggunaan *name mangling* :

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

Contoh diatas akan berfungsi jika *MappingSubClass* muncul dan memperkenalkan sebuah __update pengidentifikasi karena masing masing diganti dengan _Mapping__updated di kelas *Mapping* dan _MappingSubClass__update di kelas *MappingSubClass*.

### 7. Odds and Ends
Definisi kelas kosong akan berfungsi dengan baik jika digabungkan beberapa item data yang bernama :

```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

Sepotong kode Python yang mengharapkan tipe data abstrak tertentu sering kali dapat dilewatkan ke kelas yang mengemulasi metode tipe data itu sebagai gantinya. Misalnya, jika Anda memiliki fungsi yang memformat beberapa data dari objek file, Anda dapat mendefinisikan kelas dengan metode read()dan readline()yang mendapatkan data dari *buffer* string sebagai gantinya, dan meneruskannya sebagai argumen.

Objek metode *instance* juga memiliki atribut: m.__self__adalah objek *instance* dengan metode m(), dan m.__func__merupakan objek fungsi yang sesuai dengan metode.

### 8. Iterators
Penggunaan iterasi pada objek kontainer menggunakan pernyataan *for* di Python :

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

Gaya akses ini jelas lebih ringkas dan juga nyaman. Didalam program, pernyataan *for* akan memanggil iter() objek *container*. Fungsi ini juga dapat mengembalikan objek iterator yang mendefinisikan metode __next__() yang mengakses elemen dalam wadah satu per satu. Dan ketika tidak ditemukan lagi elemen didalamnya maka __next__() akan memunculkan *exception* *StopIteration* untuk memberitahukan fungsi *for loop* untuk berhenti. 

Berikut ini merupakan cara kerjanya :

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x0000026F8CF71DE0>
>>> next(it)
'a' 
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Setelah melihat mekanisme dibalik protokol iterator, maka mudah saja untuk menambahkan perilaku iterator kedalam kelas anda. Dengan menentukan metode __iter__() yang dapat mengembalikan objek melalui metode __next__(), dan sebalikany jika kelas mendefinisikan __next__(), maka __iter__() bisa saja mengembalikan nilai *self* :

```python
>>> class Reverse:
...     """Iterator for looping over a sequence backwards."""
...     def __init__(self, data):
...         self.data = data
...         self.index = len(data)
...     def __iter__(self):
...         return self
...     def __next__(self):
...         if self.index == 0:
...             raise StopIteration
...         self.index = self.index - 1
...         return self.data[self.index]
...
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x0000026F8D1D7050>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

### 9. Generators
Generator adalah alat yang sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakan pernyataan *yield* setiap kali mereka ingin mengembalikan data. Setiap kali next() akan dipanggil, generator melanjutkan dari tempat terakhirnya (ia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi). Sebuah contoh menunjukkan bahwa generator dapat dengan mudah dibuat:

```python
>>> def reverse(data):
...     for index in range(len(data)-1, -1, -1):
...         yield data[index]
... 
>>> for char in reverse('golf'):
...     print(char)
... 
f   
l   
o   
g   
>>> 
```

Apa pun yang dapat dilakukan dengan generator juga dapat dilakukan dengan iterator berbasis kelas seperti yang dijelaskan di bagian sebelumnya. Apa yang membuat generator begitu kompak adalah bahwa __iter__() dan __next__()metode dibuat secara otomatis.

Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara panggilan. Ini membuat fungsi lebih mudah untuk ditulis dan jauh lebih jelas daripada pendekatan menggunakan variabel instan seperti self.index dan self.data.

Selain pembuatan metode otomatis dan penyimpanan status program, ketika generator dihentikan, mereka secara otomatis menaikkan StopIteration. Dalam kombinasi, fitur-fitur ini memudahkan untuk membuat iterator dengan tidak lebih dari menulis fungsi biasa.


### 10. Generator Expressions
Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan pemahaman daftar tetapi dengan tanda kurung alih-alih tanda kurung siku. Ekspresi ini dirancang untuk situasi di mana generator digunakan langsung oleh fungsi terlampir. Ekspresi generator lebih ringkas tetapi kurang fleksibel daripada definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.

```python
>>> sum(i*i for i in range(10))
285
>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))
260
>>> unique_words = set(word for line in page  for word in line.split())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'page' is not defined. Did you mean: 'range'?
>>> valedictorian = max((student.gpa, student.name) for student in graduates)   
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'graduates' is not defined
>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```


## D. Kesimpulan
Pemrograman berorientasi objek/*object-oriented programming* (OOP) adalah metode penataan program dengan menggabungkan properti dan perilaku terkait kedalam objek individu. 

Paradigma OOP/PBO adalah paradigma yang menjadikan semua komponen program sebagai objek. Yang mana setiap objek memiliki identitas dan tugasnya masing-masing.

Misalnya, sebuah objek dapat mewakili seseorang dengan properti seperti nama, usia, dan alamat serta perilaku seperti berjalan, berbicara, bernapas, dan berlari. Atau bisa juga mewakili email dengan properti seperti daftar penerima, subjek, dan isi dan perilaku seperti menambahkan lampiran dan mengirim.

Paradigma pemrograman umum lainnya adalah pemrograman prosedural , yang menyusun program seperti resep yang menyediakan serangkaian langkah, dalam bentuk fungsi dan blok kode, yang mengalir secara berurutan untuk menyelesaikan tugas.

Kuncinya adalah bahwa objek berada di pusat pemrograman berorientasi objek dengan Python, tidak hanya mewakili data, seperti dalam pemrograman prosedural, tetapi juga dalam keseluruhan struktur program.

Kelas digunakan untuk membuat struktur data yang ditentukan pengguna. Kelas mendefinisikan fungsi yang disebut metode , yang mengidentifikasi perilaku dan tindakan yang dapat dilakukan oleh objek yang dibuat dari kelas dengan datanya.

Kelas seperti formulir atau kuesioner. *Instance* seperti formulir yang telah diisi dengan informasi. Sama seperti banyak orang dapat mengisi formulir yang sama dengan informasi unik mereka sendiri, banyak contoh dapat dibuat dari satu kelas.

Kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama-sama. Membuat kelas baru membuat tipe objek baru, memungkinkan *instance* baru dari tipe itu dibuat. Setiap *instance* kelas dapat memiliki atribut yang dilampirkan untuk mempertahankan statusnya. *Instance* kelas juga dapat memiliki metode (didefinisikan oleh kelasnya) untuk memodifikasi statusnya.