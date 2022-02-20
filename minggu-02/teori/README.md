# PENGENDALI ALIRAN PROGRAM 
## 4. FLOW TOOLS
### 4.1 IF Statements

Dalam bahasa pemrograman seringkali ditemukan pernyataan untuk menyelesaikan suatu permasalahan, pernyataan tersebut terkadang memberi ruang untuk seorang pengembang dalam menentukan nilai seharusnya. Salah satu pernyataan yang banyak digunakan adalah IF, pernyataan atau statemen ini akan menghasilkan dua kemungkinan, yakni benar atau salah, True or False, 0 atau 1, ya atau tidak dsb. 

Didalam bahasa pemrograman Python pun terdapat fungsi yang serupa yang mana pada tingkatan IF kemungkinan yang dihasilkan hanya berupa satu pernyataan saja, untuk mendapat dua atau lebih kemungkinan maka dbutuhkan tingkat Else If (Elif – singkatan dari else if). 

Berikut ini merupakan contoh penggunaan IF *statement*/pernyataan pada bahasa python. 

```python
x = int(input("Masukkan nilai integer : "))
if x < 0:
    x = 0
    print('Nilai negatif diubah menjadi nol')
elif x == 0:
    print('nol')
elif x == 1:
    print('satu')
else:
    print('lebih')

```


### 4.2 FOR Statements

Walaupun pada bahasa pemrograman Python ini terdapat FOR *statement*/pernyataan FOR seperti pada bahasa pemrograman lainnya, penggunaannya dalam bahasa ini mempunyai penerapan yang berbeda. Jika pada bahasa lainnya memerlukan pengulangan operasi aritmatika terlebih pada sebuah angka atau menentukan langkah berdasarkan iterasi dan kondisi penghentian, maka pada Python pengulangan hanya akan terjadi pada item dan akan tersusun membentuk sebuah daftar (susunan data dalam urutan) dengan tipe data string. 

Berikut ini merupakan contoh penggunaan FOR :

```python
# Mencoba nilai string:
words = ['kucing', 'jendela', 'defenestrate']
for j in words:
    print(j, len(j))
```

*source code* yang digunakan untuk memodifikasi sebuah koleksi saat perulangan iterasi untuk koleksi yang sama sedang berjalan akan mengalami kesulitan dalam perbaikannya, atau bisa dikatakan sulit untuk diperbaiki jika sedang berjalan. Adapun hal yang dapat dilakukan sebagai gantinya adalah mengulang salinan *source code* dari koleksi atau membuat yang baru. 

Berikut adalah contohnya :

```python
# Membuat sampel koleksi
users = {'Mashiho': 'active', '김준규': 'inactive', 'ハルト': 'active'}

# Strategi: Mengulang salinan
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        
# Strategi: Membuat koleksi baru
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

### 4.3 Fungsi range()

Selain *statement* perulangan (for) dan seleksi (if), pada Python juga terdapat fungsi range(), fungsi yang dapat digunakan untuk mengurutkan kembali urutan angka. Fungsi ini merupakan bawaan dari Python. Fungsi ini dapat digunakan dalam progresi aritmatika. 

```python
for i in range(5):
    print(i)
```

Titik akhir pada pengurutan nilai bukanlah bagian dari urutan yang dihasilkan, contoh "range(10)" akan menghasilkan 10 nilai, indeks hukum untuk item tersebut hanya akan menampilkan nilai 10 saja. Hal tersebut juga berlaku untuk nilai yang bersifat negatif :

```python
range(10)
```


```python
list(range(5, 10))

list(range(0, 10, 3))

list(range(-10, -100, -30))
```

Jika user ingin mengulangi indeks urutan nilai, maka dapat menggabungkan fungsi range() dan len() pada *source code* nya, seperti berikut ini :

```python
a = ['Haruto', 'is', 'the', 'rapper', 'in', 'TREASURE']
for i in range(len(a)):
    print(i, a[i])
```

Selain itu, penggunaan enumerate() juga dapat dilakukan jika ingin lebih mudah dalam penanganan kasus serupa yang membutuhkan fungsi tersebut. Berikut ini contoh penggunaan enumerate() berupa sum() :

```python
sum(range(4)) # 0 + 1 + 2 + 3
```

### 4.4 break dan continue Statements, and else Clauses Loops

Pernyataan break, seperti di bahasa C, akan keluar melalui penutup dibagian for ataupun while dari perulangan (loop) paling dalam. 

Pernyataan perulangan (loop) mungkin memiliki else berupa klausa yang nantinya dapat dieksekusi ketika proses *looping* berakhir melalui iterasi for ataupun ketika kondisi bernilai salah ketika while berjalan, namun hal ini tidak akan terjadi jika sebuah perulangan (loop) diakhiri dengan sebuah break didalam pernyataan. 
Berikut ini merupakan contoh penggunaannya :

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```

Ketika digunakan dengan perulangan (loop), klausa else akan memiliki lebih banyak kesamaan dengan klausa else pada pernyataan try. Sebaliknya, jika pernyataan if berjalan ketika tidak ditemukan klausa untuk pernyataan try didalamnya maka pengecualian tidak akan terjadi dan klausa else untuk penyataan perulangan (loop) juga tidak akan ditemukan. 
Berikut ini merupakan contoh penggunaan klausa lanjut (continue) :

```python
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
```

### 4.5 Pernyataan Pass

Pernyataan pass pada Python pada dasarnya tidak menghasilkan nilai apapun, namun dapat digunakan untuk menguji pernyataan secara sintaksis dan tidak memerlukan sebuah tindakan, contohnya :

```python
while True:
    pass # Busy-wait for keyboard interrupt (Ctrl+C)
```

Atau bisa juga digunakan untuk membuat kelas minimal dan badan kondisional ketika pengembang sedang mengerjakan *source code* yang baru :

```python
class MyEmptyClass:
    pass
```

```python
def initlog(*args):
    pass   # Remember to implement this!
```

### 4.6 Pernyataan match

Pernyataan march berfungsi untuk mengambil ekspresi dan membandingkan nilai suatu variabel sesuai dengan pola berurutan yang diberikan sebagai satu atau lebih blok kasus. Pernyataan ini hampir serupa dengan pernyataan switch pada bahasa lain, namun lebih handal dalam mengekstrak komponen dari suatu nilai kedalam variabel. 

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"
```

Penggunaan _ dalam *source code* berfungsi sebagai *wildcard* yang akan mencocokkan nilai yang mana jika tidak ditemukan kasus yang cocok atau tidak ditemukan cabang yang akan dieksekusi. Selain _, penggunaan | yang berarti "atau" dalam *source code* juga dapat diterapkan sebagai sebuah pola, pola sendiri dapat terlihat seperti membongkar tugas dan mengikat sebuah variabel : 

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

Menggunakan class point untuk mengikat nilai dari variabel pada dua pola yang membuatnya konseptual mirip dengan tugas membongkar (x, y) = point. 

```python
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

Pola dapat bersarang secara sewenang-wenang. Misalnya, jika kita memiliki daftar poin yang pendek, maka dapat dicocokkan dengan cara seperti berikut ini : 

```python
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```

ataupun dengan cara berbeda seperti yang satu ini :

```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

```python
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
```


### 4.7 Mendefenisikan Fungsi 

Membuat deret fibonacci menggunakan fungsi bawaan python :
```python
def fib(n):    # Menulis fibonacci
    """ Mencetak nilai fibonacci ."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Memanggil fungsi yang telah didefenisikan:
fib(2000)
```

Kata kunci pada cuplikan atau potongan *source code* diatas memperkenalkan fungsi def. Penggunaan fungsi ini haruslah diikuti dengan nama fungsi serta daftar parameter formal dalam kurung. Pernyataan - pernyataan yang membentuk badan fungsi akan dimulai pada baris berikutnya dan akan melalui proses diindentasi. 


Definisi fungsi mengaitkan nama fungsi dengan objek fungsi dalam tabel simbol saat ini. Interpreter mengenali objek yang ditunjuk dengan nama itu sebagai fungsi yang ditentukan pengguna. Nama lain juga dapat menunjuk ke objek fungsi yang sama dan juga dapat digunakan untuk mengakses fungsi:

```python
fib

f = fib
f(100)

fib(0)
print(fib(0))
```
Sangat mudah untuk menulis fungsi yang mengembalikan daftar nomor deret Fibonacci, alih-alih mencetaknya:

```python
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result
```


### 4.8 Mendefenisikan lebih lanjut tentang fungsi

#### 4.8.1 Nilai Argumen
Bentuk yang paling berguna adalah untuk menentukan nilai default untuk satu atau lebih argumen. Ini menciptakan fungsi yang dapat dipanggil dengan argumen yang lebih sedikit daripada yang ditentukan untuk diizinkan. Sebagai contoh:

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```


#### 4.8.2 Argumen Kata
Fungsi juga dapat dipanggil menggunakan argumen kata kunci dari formulir kwarg=value. menerima satu argumen wajib ( voltage) dan tiga argumen opsional ( state, action, dan type). Misalnya, fungsi berikut:

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword    
```

Dalam panggilan fungsi, argumen kata kunci harus mengikuti argumen posisi. Semua argumen kata kunci yang diteruskan harus cocok dengan salah satu argumen yang diterima oleh fungsi (misalnya actorbukan argumen yang valid untuk parrotfungsi tersebut), dan urutannya tidak penting. Ini juga termasuk argumen non-opsional (misalnya parrot(voltage=1000)valid juga). Tidak ada argumen yang dapat menerima nilai lebih dari sekali. Berikut adalah contoh yang gagal karena pembatasan ini:

```python
def function(a):
    pass

function(0, a=0)
```

Ketika parameter formal terakhir dari formulir **name hadir, ia menerima kamus yang berisi semua argumen kata kunci kecuali yang terkait dengan parameter formal. Ini dapat digabungkan dengan parameter formal dari formulir *name yang menerima tupel yang berisi argumen posisi di luar daftar parameter formal. Misalnya, jika kita mendefinisikan fungsi seperti ini:

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

#### 4.8.3 Parameter
Secara default, argumen dapat diteruskan ke fungsi Python baik dengan posisi atau secara eksplisit dengan kata kunci. Untuk keterbacaan dan kinerja, masuk akal untuk membatasi cara argumen dapat diteruskan sehingga pengembang hanya perlu melihat definisi fungsi untuk menentukan apakah item dilewatkan berdasarkan posisi, posisi atau kata kunci, atau kata kunci.

Definisi fungsi mungkin terlihat seperti :

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

Dimana karakter / dan * adalah pilihan opsional yang mana jika digunakan akan menunjukkan jenis parameter melalui bagaimana argumen dapat diteruskan ke fungsi baik itu sebagai hanya posisional, posisional ataupun kata kunci dan hanya kata kunci. Parameter kata kunci juga kerap kali disebut parameter bernama. 

1. Parameter posisional
    Jika karakter / dan * tidak tercatat didalam defenisi fungsi, maka argumen dapat diteruskan ke fungsi berikutnya berdasarkan posisi atau kata kunci berada. 

2. Parameter hanya posisional
    Melihat ini sedikit lebih detail, dimungkinkan untuk menandai parameter tertentu sebagai hanya posisional . Jika hanya posisional , urutan parameter penting, dan parameter tidak dapat diteruskan oleh kata kunci. Parameter posisional saja ditempatkan sebelum /(garis miring ke depan). The /digunakan untuk secara logis memisahkan parameter posisional saja dari parameter lainnya. Jika tidak ada /dalam definisi fungsi, tidak ada parameter posisional saja.

    Parameter yang mengikuti /mungkin berupa posisi-atau-kata kunci atau hanya-kata kunci .

3. Parameter hanya kata kunci
    Untuk menandai parameter sebagai hanya kata kunci , yang menunjukkan parameter harus diteruskan oleh argumen kata kunci, tempatkan an *di daftar argumen tepat sebelum parameter khusus kata kunci pertama .

4. Contoh
    Contoh definisi fungsi menggunakan karakter / dan * :
    ```python
    def standard_arg(arg):
    print(arg)

    def pos_only_arg(arg, /):
        print(arg)

    def kwd_only_arg(*, arg):
        print(arg)

    def combined_example(pos_only, /, standard, *, kwd_only):
        print(pos_only, standard, kwd_only)
    ```

    * Fungsi pertama, standard_arg, bentuk yang paling dikenal, tidak membatasi konvensi pemanggilan dan argumen dapat diteruskan oleh posisi atau kata kunci :
        ```python
        standard_arg(2)

        standard_arg(arg=2)
        ```

    * Fungsi kedua pos_only_arg dibatasi hanya menggunakan parameter posisi karena ada / dalam definisi fungsi :
        ```python
        pos_only_arg(1)

        pos_only_arg(arg=1)
        ```

    * Fungsi ketiga kwd_only_argshanya mengizinkan argumen kata kunci seperti yang ditunjukkan oleh a * dalam definisi fungsi :
        ```python
        kwd_only_arg(3)

        kwd_only_arg(arg=3)
        ```
    
    * Menggunakan ketiga konvensi pemanggilan dalam definisi fungsi yang sama :
        ```python
        combined_example(1, 2, 3)

        combined_example(1, 2, kwd_only=3)

        combined_example(1, standard=2, kwd_only=3)

        combined_example(pos_only=1, standard=2, kwd_only=3)
        ```

        Akhirnya, pertimbangkan definisi fungsi ini yang memiliki potensi benturan antara argumen posisi name dan **kwds yang memiliki name kunci:
        ```python
        def foo(name, **kwds):
            return 'name' in kwds

        foo(1, **{'name': 2})


        def foo(name, /, **kwds):
            return 'name' in kwds
        >>> foo(1, **{'name': 2})
        True
        ```

    5. Rekap
    Kasus penggunaan akan menentukan parameter mana yang akan digunakan dalam definisi fungsi :
    ```
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    ```

#### 4.8.4 Daftar Argumen 
Opsi yang paling jarang digunakan adalah menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen yang berubah-ubah. Argumen-argumen ini akan dibungkus dalam sebuah tuple. Sebelum jumlah variabel argumen, nol atau lebih argumen normal dapat terjadi.

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

Biasanya, variadic argumen ini akan menjadi yang terakhir dalam daftar parameter formal, karena mereka mengambil semua argumen input yang tersisa yang diteruskan ke fungsi. Parameter formal apa pun yang muncul setelah *args parameter adalah argumen 'hanya kata kunci', artinya parameter tersebut hanya dapat digunakan sebagai kata kunci daripada argumen posisi.

```python
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")
```

#### 4.8.5 Membongkar Daftar
Situasi sebaliknya terjadi ketika argumen sudah ada dalam daftar atau tupel tetapi perlu dibongkar untuk pemanggilan fungsi yang memerlukan argumen posisi terpisah. Misalnya, range()fungsi bawaan mengharapkan argumen mulai dan berhenti yang terpisah. Jika tidak tersedia secara terpisah, tulis pemanggilan fungsi dengan *-operator untuk membongkar argumen dari daftar atau tupel:

```python
list(range(3, 6))            # normal call with separate arguments

args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
```

Dengan cara yang sama, kamus dapat mengirimkan argumen kata kunci dengan **-operator:

```python
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
```

#### 4.8.6 Ekspresi 

Fungsi anonim kecil dapat dibuat dengan lambda kata kunci. Fungsi ini mengembalikan jumlah dari dua argumennya: . Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas pada satu ekspresi. Secara semantik, mereka hanyalah gula sintaksis untuk definisi fungsi normal. Seperti definisi fungsi bersarang, fungsi lambda dapat mereferensikan variabel dari cakupan yang berisi:lambda a, b: a+b

```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)
```

Penggunaan lain adalah untuk melewatkan fungsi kecil sebagai argumen:

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
```

#### 4.8.7 String Dokumentasi
Beberapa konvensi tentang konten dan pemformatan string dokumentasi.

```python
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
```

#### 4.8.8 Fungsi Anotasi 
Anotasi fungsi merupakan sebuah informasi metadata opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna. Anotasi disimpan dalam__annotations__ atribut fungsi sebagai kamus dan tidak berpengaruh pada bagian lain dari fungsi tersebut. Anotasi parameter ditentukan oleh titik dua setelah nama parameter, diikuti dengan ekspresi yang mengevaluasi nilai anotasi. Contoh berikut memiliki argumen yang diperlukan, argumen opsional, dan nilai kembalian yang dianotasi :

```python
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
```

### 4.9 Intermezzo : Gaya
Sekarang Anda akan menulis bagian Python yang lebih panjang dan lebih kompleks, ini saat yang tepat untuk berbicara tentang gaya pengkodean . Sebagian besar bahasa dapat ditulis (atau lebih ringkas, diformat ) dalam gaya yang berbeda; beberapa lebih mudah dibaca daripada yang lain. Mempermudah orang lain untuk membaca kode Anda selalu merupakan ide yang bagus, dan mengadopsi gaya pengkodean yang bagus sangat membantu untuk itu.

Untuk Python,PEP 8 telah muncul sebagai panduan gaya yang dipatuhi sebagian besar proyek; itu mempromosikan gaya pengkodean yang sangat mudah dibaca dan menyenangkan mata.