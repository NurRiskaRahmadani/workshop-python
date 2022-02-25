# STRUKTUR DATA (Pertemuan 3)
## A. Latar Belakang
Struktur data merupakan cara penyimpanan dan pengaturan data yang dilakukan secara terstruktur didalam sebuah sistem komputer atau database sehingga mempermudah dalam hal pengaksesannya. Maka dari itu struktur data menjadi salah satu bagian penting yang wajib dipahami oleh seorang pengembang. Dengan adanya struktur data dapat memudahkan pengguna untuk mengakses segala jenis data yang dibutuhkan dan dapat disimpan dalam beberapa format khusus yang berfungsi untuk mengatur, memproses, mengambil, dan menyimpan data. Karena keterkaitan itulah, struktur data diterapkan hampir disemua jenis bahasa pemrograman komputer, tidak terkecuali di Python. Pada Python struktur data terdiri atas empat klasifikasi *built-in* seperti List/Daftar, Tuple, Dictionary, Set dan masih banyak lagi.

Berdasarkan uraian diatas, maka akan dibuat sebuah laporan workshop yang mengkaji tentang struktur data pada Python, mulai dari bagaimana membuat klasifikasi berdasarkan *built-in*? dan bagaimana cara mengimplementasikannya kedalam program Python.

## B. Dasar Teori
Struktur data adalah cara menyimpan dan mengatur data secara terstruktur pada sistem komputer atau database sehingga lebih mudah diakses. Secara teknis, data dalam bentuk angka, huruf, simbol, dan lainnya ini diletakkan dalam kolom-kolom dan susunan tertentu. 

Dalam menyusun data, terdapat beberapa istilah yang perlu Anda pahami, yaitu node dan indeks. Berikut adalah penjelasan tentang kedua istilah tersebut.
 
    * Node, yaitu elemen yang terdapat dalam struktur data. Setiap node berisi pointer ke node selanjutnya.
    * Indeks, yaitu objek dalam sistem database yang bisa mempercepat proses pencarian data. 

Struktur data bisa digunakan untuk mengelola database, melakukan kompres file, hingga mengolah data lainnya. Praktis, struktur ini menjadi hal yang harus dipelajari karena dapat membantu Anda untuk menyatukan berbagai elemen data secara efektif. Apalagi, struktur data juga akan mempengaruhi ketepatan algoritma suatu program.

Struktur data memiliki banyak tipe dan beberapa diantaranya adalah :
    1. List/Daftar
    Sebuah daftar mewakili jenis struktur data paling serbaguna di dalam Python. Itu dapat berisi item dengan jenis yang berbeda dan tidak memiliki aturan terhadap unicity. Daftar mengindeks dari nol, elemen yang dapat dicacah, digabungkan, dan sebagainya. Daftar juga memiliki banyak kesamaan dengan string, mendukung jenis operasi yang sama namun tidak seperti string, daftar dapat berubah.

    2. Pemahaman Daftar
    Sebuah pemahaman daftar berarti, membentuk sebuah daftar dalam sebuah cara yang sangat alami dari sudut pandang matematis. Code untuk melakukan ini singkat dan sangat mudah dibaca. Sebuah contoh sederhana ketika kamu akan menggunakan pemahaman daftar adalah ketika kamu ingin membuat sebuah daftar berdasarkan pada elemen dari daftar lainnya

    3. Tuple
    Sebuah tuple diwakili oleh sebuah angka nilai yang dipisahkan oleh koma. Tidak seperti daftar, tuple bersifat tetap dan outputnya dikelilingi oleh tanda kurung sehingga tuples yang menginduk diproses secara benar. Sebagai tambahan, walaupun tuples bersifat tetap, mereka dapat menampung data yang tidak tetap jika diperlukan.

    4. Dictionary
    Kamus disajikan dalam pasangan key:value. Dengan kata lain, mereka merupakan peta atau koleksi asosiatif. Key, tidak seperti daftar dimana berupa angka, dapat berupa jenis tetap apapun dan harus unik. Value dapat berupa jenis apapun, berubah atau tetap.

    5. Set
    Set adalah sebuah koleksi tanpa urut dan tanpa nilai yang terduplikasi. Sebuah set dapat dibuat dengan menggunakan kata kunci set atau dengan menggunakan kurung kurawal {}. Namun bagaimana pun juga, untuk membuat sebuah set kosong kamu hanya dapat menggunakan konstruksi set, kurung kurawal sendiri akan membuat sebuah kamus kosong.

## C. Data Structures

### 1. List/Daftar
Berikut ini merupakan metode objek yang digunakan pada list/daftar pada Python :
    ```
    list.append(*x*)
    ```
        Item ini ditambahkan pada akhir sebuah daftar.

    ```
    list.extend(*iterable*)
    ```
        *Extend* pada daftar dapat ditambahkan ke semua item yang berada di *iterable*.

    ```
    list.insert(*i*, *x*)
    ```
        *Insert* dapat digunakan untuk memberikan posisi pada sebuah item. Argumen pertama merupakan indeks dari elemen sebelum dimasukkan dengan *insert*/
    
    ```
    list.remove(*x*)
    ```
        *Remove* dapat digunakan untuk menghilangkan item pertama disebuah daftar yang nilainya sama dengan *x* dan akan menghasilkan ValueError jika tidak ditemukan item yang serupa. 
    
    ```
    list.pop([i])
    ```
       Perintah ini dapat menghapus item yang berada pada posisi tertentu didalam daftar dan dapat juga dikembalikan lagi. Jika tidak ditemukan indeks yang ditentukan akan dihapus dan dikembalikan sehingga menjadi item terakhir didalam daftar.

    ```
    list.clear()
    ``` 
        Memindahkan semua item dari daftar.
    
    ```
    list.index(*x*[, *start*[, *end*]])
    ```
        Mengulang data dari indeks *zero-base* pada daftar menjadi item pertama dengan *value* berupa x atau yang setara dan akan menghasilkan ValueError jika tidak ditemukan perintah serupa didalamnya.
    
    ```
    list.count(*x*)
    ```
        Menghitung kembali nomor dari variabel *x* yang berada didalam daftar.
    
    ```
    list.sort(*, key=None, Reverse=False)
    ```
        *Sort* berfungsi untuk menyortir item didalam daftar.
    
    ```
    list.reverse()
    ```
        *Reverse* berfungsi untuk membalikkan elemen didaftar pada tempat sebenarnya.
    
    ```
    list.copy()
    ```
        Perintah ini berfungsi untuk mengembalikan salinan daftar yang dangkal.
    
Contoh penggunaan metode didalam daftar :
    ```python
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits.count('apple')

    fruits.count('tangerine')

    fruits.index('banana')

    fruits.index('banana', 4)   # Mencari banana setelah memulai pencarian dari posisi 4

    fruits.reverse()
    fruits

    fruits.append('grape')
    fruits

    fruits.sort()
    fruits

    fruits.pop()
    ```

#### a. Menggunakan Daftar Sebagai Tumpukan
Metode daftar sangatlah mudah penerapannya jika dibuat sebagai sebuah tumpukan, dimana elemen terakhir yang ditambahkan akan menjadi elemen pertama yang dapat diambil. Sebagai contoh :
```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop()

stack

stack.pop()

stack.pop()

stack
```
#### b. Menggunakan Daftar Sebagai Antrian
Selain dengan tumpukan, Python juga memungkinkan penggunaan daftar sebagai sebuah antrian, dimana elemen pertama yang ditambahkan merupakan elemen pertama yang dapat diambil. Walaupun begitu penggunaan daftar ini tidaklah efesien karena pengambilan data menjadi lambat. 

Berikut ini merupakan pengimplementasian antrian pada Python :
```python
from collections import deque
queue = deque(["David Kim", "Mama Takata", "Travis Watanabe"])
queue.append("Daniel Choi")           # Memasukkan Daniel kedalam antrian
queue.append("Kyle Bang")          # Memasukkan Kyle kedalam antrian
queue.popleft()                 # Memindahkan data pertama

queue.popleft()                 # Memindahkan data kedua

queue                           # Menyusun kembali antrian berdasarkan data yang dimasukkan 
```
#### c. Pemahaman Daftar 
Metode ini menyediakan cara pembuatan daftar secara ringkas. Metode ini biasanya digunakan untuk membuat sebuah daftar baru dimana setiap elemen merupakan hasil dari beberapa operasi yang diterapkan ke setiap item dari urutan lain atau *iterable*, atau untuk membuat sub urutan dari elemen yang memenuhi kondisi tersebut. 

Berikut ini merupakan contoh penerapan untuk membuat sebuah daftar berbentuk kotak :

```python
squares = []
for x in range(4):
    squares.append(x**2)

squares
```
Adapun untuk menghilangkan variabel yang menumpuk pada *source code* diatas daoat dilakukang dengan perintah berikut ataupun ekuivalen berikut :

```python
squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]
```

Pemahaman daftar sendiri terdiri atas tanda kurung yang berisi ekspresi dan diikuti klausa for lalu kemudian nol atau for lainnya atau klausa if. Berikut ini contoh penggunaan listcomp yang menggabungkan elemen dari dua daftar jika tidak sama : 

```python
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs

vec = [-4, -2, 0, 2, 4]
# Membuat list baru dengan value berlipat
[x*2 for x in vec]

# Mem-filter daftar tidak termasuk bilangan negatif
[x for x in vec if x >= 0]

# Mengaplikasikan sebuah fungsi untuk semua elemen yang ada
[abs(x) for x in vec]

# Memanggil method dari elemen lain
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# Membuat sebuah list dari 2 tuple seperti nomer atau kotak
[(x, x**2) for x in range(6)]

# Sebuah tuple haruslah memiliki parenthesized atau tidak akan mengalami error
[x, x**2 for x in range(6)]

# Meratakan daftar menggunakan listcomp dengan dua seleksi for
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]
```

#### d. Pemahaman Daftar Bersarang  
Ekspresi awal yang digunakan dalam pemahaman daftar dapat berupa ekspresi arbitrer. Berikut ini merupakan contoh dari matriks 3x4 yang diimplementasikan sebagai 3 daftar panjang 4 :
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed

list(zip(*matrix))

```

### 2. Del Statements
Untuk menghapus sebuah item dari daftar terdapat beberapa cara yang dapat dilakukan, salah satunya adalah pernyataan del. Berbeda dengan Pop() metode yang dapat mengembalikan nilai item. Pernyataan ini juga dapat digunakan untuk menghapus sebuah irisan dari daftar atau menghapus semua isi daftar. 

```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a

del a[2:4]
a

del a[:]
a

del a
```
### 3. Tuples & Sequences
Daftar dan string memiliki banyak sekali properti umum seperti operasi pengindeksan dan pengirisan. Pada python tipe data berurutan dapat ditambahkan dan juga dapat dimasukan pada tipe data urutan standar lainnya yakni tuple. Tuple sendiri terdiri atas sejumlah nilai yang dipisahkan oleh koma :

```python
t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
```

Seperti yang terlihat pada potongan *source code* diatas, tuple keluaran selalu diapit tanda kurung, sehingga sebuah tuple bersarang dapat diterjemahkan dengan benar. 

Meskipun tuple dan daftar hampir serupa, namun penggunaan keduanya berbeda. Penggunaan tuple tidak dapat diubah dan biasanya berisi urutan elemen yang beragam yang dapat diakses melalui pembongkaran atau pengindeksan, sementara daftar dapat diubah penggunaannya. 

Masalah khusus adalah kontruksi tuple yang berisi 0 atau 1 item sintaks kebiasaan tambahan untuk mengakomodasi sebuah daftar. Tuple kosong terdiri atas sepasang tanda kurung kosong, tuple dengan satu item dibangun dengan mengikuti nilai diikuti oleh koma. 

```python
empty = ()
singleton = 'Annyeonghaseo',    # <-- note trailing comma
len(empty)

len(singleton)

singleton

x, y, z = t
```

### 4. Sets
Kurung kurawal atau set() fungsi dapat digunakan untuk membuat sebuah himpunana. Sebuah set kosong bisa dibuat menggunakan perintah set(), bukan {}, serta dapat juga digunakan untuk membuat sebuah dictionari kosong. 

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)          # Menampilkan duplikat setelah dipindahkan

'orange' in basket     # Menguji kecepatan membership

'crabgrass' in basket


# Mendemonstrasikan operasi set dengan unique letter dari dua kata

a = set('abracadabra')
b = set('alacazam')
a          # unique letters in a

a - b      # letters in a but not in b

a | b      # letters in a or b or both

a & b      # letters in both a and b

a ^ b      # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a
```


### 5. Dictionaries

Operasi utama pada *dictionary* adalah menyimpan sebuah nilai dengan beberapa kunci dan dapat mengekstrak nilai yang diberikan kunci tersebut. Pada pernyataan ini juga dimungkinkan untuk menghapus pasangan key (del). Sebuah nilai yang sudah terlalu lama disimpan akan hilang atau terlupakan. 

Untuk membuat daftar pada *dictionary* dapat dilakukan dengan perintah list(), biasanya nilai pada daftar dapat sisipkan berdasarkan urutan dengan perintah sorted(d) saja. 

Berikut ini contoh penggunaan *dictionary* :

```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{x: x**2 for x in (2, 4, 6)}

dict(sape=4139, guido=4127, jack=4098)
```


### 6. Teknik Looping
Pengulangan pada dengan *dictionary*, key dan value dapat dilakukan dengan metode items() ini, enumerate(), zip(), reversed(), sorted(). 

```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['Kevin Steward', 'patronous', 'black']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


for i in reversed(range(1, 10, 2)):
    print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
```

Membuat daftar baru dengan teknik *looping* :
```python
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data
```

### 7. Lebih Banyak Kondisi
Kondisi yang digunakan dalam while dan if pernyataan dapat berisi operator apa pun, bukan hanya perbandingan.

Operator perbandingan in dan merupakan tes keanggotaan yang menentukan apakah suatu nilai ada di (atau tidak) dalam wadah. Operator dan membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik.not in is is not

Perbandingan dapat dirantai. Misalnya, menguji apakah kurang dari dan apalagi sama dengan .a < b == cabbc

Perbandingan dapat digabungkan menggunakan operator Boolean and dan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; antara mereka, not memiliki prioritas tertinggi dan or terendah, sehingga setara dengan . Seperti biasa, tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan.A and not B or C(A and (not B)) or C

Operator Boolean and dan oryang disebut operator hubung singkat : argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C benar tetapi B salah, tidak mengevaluasi ekspresi . Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat adalah argumen terakhir yang dievaluasi. A and B and C C

Contoh penggunaan :
```python
string1, string2, string3 = '', 'Trondheim', 'Chicken noddle soup dance'
non_null = string1 or string2 or string3
non_null
```

### 8. Mencocokkan Sequences Dengan Tipe Lainnya
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingannya menggunakan *leksikografis* pemesanan: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, perbandingan *leksikografis* dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu barisan merupakan sub-urutan awal dari yang lain, barisan yang lebih pendek adalah yang lebih kecil (lebih kecil). Urutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual.

## D. Kesimpulan 
Struktur data adalah cara menyimpan dan mengatur data secara terstruktur pada sistem komputer atau database sehingga lebih mudah diakses. Secara teknis, data dalam bentuk angka, huruf, simbol, dan lainnya ini diletakkan dalam kolom-kolom dan susunan tertentu. 

Dalam menyusun data, terdapat beberapa istilah yang perlu Anda pahami, yaitu node dan indeks.

Struktur data bisa digunakan untuk mengelola database, melakukan kompres file, hingga mengolah data lainnya. Praktis, struktur ini menjadi hal yang harus dipelajari karena dapat membantu Anda untuk menyatukan berbagai elemen data secara efektif. Apalagi, struktur data juga akan mempengaruhi ketepatan algoritma suatu program.

Struktur data memiliki banyak tipe dan beberapa diantaranya adalah :
    * List/Daftar
    * Pemahaman Daftar
    * Tuple
    * Dictionary
    * Set