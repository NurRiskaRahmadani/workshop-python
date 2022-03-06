# Modul di Python (Pertemuan 4)
## A. Latar Belakang
Ketika seorang pengembang selesai menuliskan kode program melalui *interpreter* Python yang kemudian *logout* dari *interpreter* tersebut lalu melakukan *login* kembali, biasanya definisi yang telah dibuat baik itu berupa fungsi ataupun variabel akan hilang atau terhapus dengan sendirinya. Maka dari itu, alternatif yang dapat dilakukan adalah dengan menggunakan editor teks sehingga lebih mudah dan bisa langsung dijalankan  dengan file yang dapat dijadikan sebagai input dan dikenal sebagai membuat skrip. Saat kode program yang dibuat semakin panjang, mungkin saja pembagian beberapa file akan dilakukan untuk memudahkan perawatannya. 

Pada Python, kasus diatas dapat dikerjakan dengan cara menempatkan defenisi dalam file dan menggunakannya dalam skrip atau dalam *instance interpreter* yang interaktif. File tersebut dikenal sebagai modul. 

Berdasarkan uraian latarbelakang diatas, maka akan dibuat sebuah laporan workshop yang membahas tentang apa itu modul di Python? Bagaimana cara menggunakannya? dan apa saja perintah didalamnya?.

## B. Dasar Teori
Modul adalah sebuah file yang berisi definisi dan pernyataan Python. Definisi dari sebuah modul adalah dapat di*impor* ke modul lain atau modul utama (Berupa kumpulan variabel yang dapat diakses dalam skrip yang dijalankan di tingkat atas dan dalam mode kalkulator). Sedangkan untuk nama file sendiri merupakan nama dari modul dengan akhiran ditambahkan .py.  

Di dalam sebuah modul, nama modul akan mempunyai tipe data string yang tersedia sebagai nilai dari variabel global __name__.

## C. Modul
Menggunakan modul Python untuk membuat file yang dipanggil fibo.py di direktori komputer lokal. Berikut contoh penggunaanya untuk menghitung bilangan fibbonaci :

```python
# Fibonacci numbers module

def fib(n):     # write Fibonacci series up to n
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # return Fibbonaci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Setelah itu mencoba memasukan perintah pada *source code* diatas kedalam *interpreter* Python dan mengimpornya dengan perintah berikut : 

```python
>>> import fibo
```

Menggunakan file fibo.py yang telah dibuat sebelumnya untuk mencoba mengakses fungsi dari modulnya. Berikut contohnya :

```python
>>>fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>>fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>>fibo.__name__
'fibo'
```
atau :

```python
>>>fib = fibo.fib
>>>fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 1. Mengeksplor Modul
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya saat pertama kali nama modul ditentukan dalam pernyataan impor yang dapat juga dijalankan jika file tersebut dieksekusi sebagai skrip.

Setiap modul memiliki tabel simbolnya sendiri yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefenisikan dalam modul. Hal ini dapat meminimalisir terjadinya bentrokan antar pengguna global. Terdapat juga fungsi modname.itemname yang dijadikan sebagai rujukan ketika telah menyentuk variabel global dari modul dengan notasi yang sama dengan yang digunakan. 

Ada beberapa varian pernyataan import yang dapat mengimpor nama dari modul langsung ke tabel simbol modul pengimpor. Berikut ini contoh penerapannya didalam *interpreter* Python :

```python
>>>from fibo import fib, fib2
>>>fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Terdapat juga varian untuk mengimpor semua nama yang didefenisikan oleh modul, seperti pada contoh berikut ini :

```python
>>>from fibo import *
>>>fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Dapat dilihat pada output yang dihasilkan, semua data yang berhasil diimpor dapat dimuat kecuali yang dimulai dengan garis bawah. Dalam kebanyakan kasus bahasa Python tidak menggunakan fasilitas ini dikarenakan terlalu banyak memperkenalkan fungsi yang tidak diketahui dan bisa saja menyembunyikan fungsi yang telah dibuat. 

Adapun fungsi dari tanda bintang (*) merupakan fungsi dari praktik mengimpor dari modul ataupun paket yang kurang diminati karena sering menyebabkan tidak terbacanya kode dengan baik. 

Menggunakan nama modul yang diikuti oleh as, berikut contoh penggunaannya :

```python
>>>import fibo as fib
>>>fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Penggunaan as merupakan cara yang efektif untuk mengimpor modul dengan cara yang sama seperti yang akan dilakukan dengan satu-satunya perbedaan tersedia sebagai fib. Selain as, terdapat juga fungsi from karena keduanya memiliki fungsi yang sama. Berikut contoh penggunaannya :

```python
from fibo import fib as fibonacci
fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

    Note :
    Setiap modul hanya dapat diimpor sekali per sesi untuk setiap bahasa pemrograman. Maka dari itu, jika terjadi perubahan modul, penerjemahan modul harus di ulangi atau jika hanya satu modul yang ingin di uji secara interaktif, dapat dengan perintah importlib.reload(), misa; : import importlib; importlib.reload(modulename)

#### a. Menjalankan Modul Sebagai Skrip
Ketika perintah :

```
python fibo.py <arguments>
```

dijalankan sebagai modul Python. Kode yang berada didalamnya akan dieksekusi, sama halnya ketika modul tersebut diimpor namun dengan __nama__ set ke "__main__" yang berarti dengan menambahkan kode ini diakhir skrip modul, seperti :

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
Dengan membuat file seperti diatas dapat digunakan sebagai skrip atau modul yang dapat diimpor karena kode nya mem-parsing baris perintah yang hanya akan berjalan ketika modul dijalankan sebagai file utama. 

```
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

Ketika modul diatas diimpor, maka kode programnya tidak akan dijalankan.

#### b. Jalur Pencarian Modul
Ketika sebuah modul spam diimpor, *interpreter* pertama akan mencari modul *built-in* dengan nama tersebut. Jika tidak ditemukam maka akan mencari file dengan nama spam.py didalam daftar direktori yang diberikan oleh variabel sys.path. sys.path yang diinisialisasi dari lokasi :
    * Direktori yang berisi skrip input.
    * PYTHONPATH.
    * Default yang bergantung pada instalasi. 

    Note :
    Pada sistem file yang mendukung symlink, direktori yang berisi skrip input dihitung setelah symlink diikuti. Dengan kata lain direktori yang berisi symlink tidak ditambahkan ke jalur pencarian modul. 

Setelah dilakukan inisiasi, program Python dapat dimodifikasi file sys.path. Direktori yang berisi skrip yang sedang dijalankan akan ditempatkan di awal jalur pencarian atau di depan jalur *library* standar. Hal ini dapat dikatakan bahwa skrip di direktori tersebut akan dimuat alih-alih modul dengan nama yang sama yang tersimpan di direktori *library*.

#### c. Kompilasi File Python 
Untuk mempercepar pemuatan sebuah modul, Python mendukung fungsi yang dapat menyimpan versi terkompilasi dari setiap modul didalam __pycache__ direktori dengan nama module.version.pyc, dimana versi tersebut mengkodekan format file yang telah dikompilasi yang biasanya berisi nomor versi Python. 

Python akan memeriksa tanggal modifikasi sumber terhadap sumber terhadap versi yang dikompilasi untuk melihat apakah itu kadaluarsa dan perlu dikompilasi ulang. Dan hal ini sepenuhnya otomatis prosesnya. Sama halnya pada modul yang dikompulasi seperti platform-independen, sehingga *library* yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda. 

Python tidak akan memeriksa *cache* dalam dua keadaan. 
    - Selama mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah.
    - Tidak memeriksa *cache* jika tidak ada modul sumber untuk mendukung distribusi non-sumber (hanya dikompilasi), modul yang dikompilasi harus berada di direktori sumber dan tidak boleh ada sumber modul. 

 
### 2. Modul Standar
Python mempunyai *library* modul standar yang dijelaskan didalam file terpisah seperti pada Python *library reference*. Beberapa modul yang dibangun dibeberapa bahasa pemrograman justru menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibuat baik hanya diperuntukkan sebagai efesiensi atau menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalam opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. 

Berikut ini merupakan contoh penggunaan modul yang hanya disediakan sistem operasi Windows :

```python
>>>import sys
>>>sys.ps1
'>>> '
>>>sys.ps2
'... '
>>>sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

Kedua ariabel yang digunakan pada *source code* diatas hanya dapat ditentukan jika *interpreter* dalam mode interaktif saja. 

Variabel sys.path merupakan daftar string yang dapat menentukan jalur pencarian *interpreter* untuk modul. Ini diinisialisasi ke jalur default yang diambil dari *environment variabel* PYTHONPATH atau dari default bawaan sehingga tidak dapat diatur. Namun masih dapat dimodifikasi dengan *standard list operation* :

```python
import sys
sys.path.append('/ufs/guido/lib/python')
```


### 3. Fungsi dir()
Fungsi bawaan dir() pada Python dapat digunakan untuk mengetahui nama mana yang akan didefenisikan oleh modul sehingga dapat dikembalikan nilainya dengan daftar string yang telah diurutkan. 

```python
>>>import fibo, sys
>>>dir(fibo)
['__name__', 'fib', 'fib2']
>>>dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```

Selain itu, menggunakan fungsi dir() juga dapat dilakukan walaupun tanpa argumen didalamnya :

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

Fungsi dir() tidak akan mencantumkan nama dari fungsi ataupun variabel bawaan lainnya Python. Jika membutuhkan daftar atau list, Python mendefenisikannya dengan modul standar *builtins* :

```python
>>>import builtins
>>>dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```


### 4. Package
*Package* merupakan cara menyusun *namespace* modul Python dengan menggunakan "nama modul bertitik". Misal : modul A.B menunjuk sebuah submodul yang dinamai B dalam sebuah *package* bernama A. Sama seperti penggunaan modul yang menyelamatkan pembuat modul yang berbeda dari keharusan khawatir tentang nama variabel global satu sama lain, penggunaan modul bertitik menyelamatkan penulis *package multi-module* seperti NumPy atau Pillow dari kekhawatiran nama modul yang digunakan. 

Contoh : akan dirancang sebuah kumpulan modul atau *package* untuk penanganan file suara dan data suara yang seragam. Terdapat begitu banyak format file untuk ragam suara yang berbeda, untuk mengatasinya hal yang dapat dilakukan adalah dengan membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file yang ada. 

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Saat pengimpor-an paket di Python biasanya akan dicari melalui direktori untuk sys.path mencari subdirektori paket. 

File __init__.py pada modul diatas berfungsi untuk membuat sebuah direktori yang memperlakukan Python yang berisi file sebagai *package*. Hal ini dapat mencegah terjadinya kesamaan pada nama di direktori dengan nama umum, seperti string. Dan secara tidak sengaja akan menyembunyikan modul valid yang biasanya muncul setelahnya pada jalur pencarian modul. Kadangkala didalam kasus sederhana, terdapat file __init__.py yang hanya berupa file kosong tetapi dapat mengeksekusi kode inisialisasi untuk *package* atau mengatur __all__ variabel yang akan dijelaskan kemudian. 

Pengguna *package* dapat mengimpor modul individual dari *package* dengan perintah :

```python
import sound.effects.echo
```
Perintah diatas memuat submodul sound.effects.echo. Namun itu harus dirujuk dengan nama lengkapnya. 

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

Adapun cara alternatif untuk mengimpor submodul adalah :

```python
from sound.effects import echo
```

Perintah diatas juga memuat submodul echo dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan.

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

Namun variasi lainnya adalah mengimpor fungsi atau variabel yang diinginkan secara langsung, seperti :

```python
from sound.effects.echo import echofilter
```

Sedangkan untuk mengakses submodel echo nya secara langsung dapat menggunakan perintah berikut :

```python
echofilter(input, output, delay=0.7, atten=4)
```

    Note :
    Saat menggunakan sebuat from package import item, item dapat berupa submodul/subpaket atau paket/*package*, seperti sebuah fungsi, kelas ataupun variabel. Pernyataan pertama akan menguji item lalu mendefinisikannya kedalam sebuah *package*, jika tidak maka ia akan menganggapnya sebagai modul dan akan mencoba memuatnya. Namun jika gagal menemukannya maka sebuah perintah seperti ImportError akan dijalankan. 

    Sebaliknya, ketika menggunakan sintaks seperti import item.subitem.subsubitem, setiap item kecuali yang terakhir harus berupa *package*, item terakhir pun dapat berupa modul atau *package* namun tidak dapat berupa kelas/fungsi/variabel yang ditentukan dalam item sebelumnya. 

#### a. Mengimpor * Dari Package
Solusi agar pengakses dapat menemukan dimana letak submodule yang berada didalam sebuah *package* dan bisa mengimpor semua isinya adalah dengan membagi pembuat *package* untuk memberikan indeks eksplisit dari *package* tersebut. Pernyataan import menggunakan konvensi : Jika sebuah *package* seperti __init__.py didefenisikan sebuah daftar nama __all__, hal ini akan dianggap sebagai daftar nama modul yang harus diimpor ketika ditemukan.

Berikut ini contoh penerapannya :

```python
__all__ = ["echo", "surround", "reverse"]
```

Maksud dari perintah diatas adalah from sound.effects import yang berarti ketiga submodul yang disebutkan akan diimpor dari *package* sound. 

Jika __all__ tidak didefenisikan, pernyataan from sound.effects import * tidak akan mengimpor semua submodul dari *package* ke *namespace* saat ini, namun hanya akan memastikan bahwa *package* tersebut telah diimpor dengan nama apa saja. 

Berikut ini merupakan contoh penggunaan import untuk beberapa submodul :

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

Dalam contoh penggunaan import diatas modul echo dan surround diimpor dalam  *namespace* saat ini karena telah didefenisikan didalam *packaga* sound.effects.

Meskipun begitu terdapat beberapa modul yang dirancang untuk mengekspor hanya berupa nama saja yang mengiktui pola tertentu saat digunakan dan masih dianggap sebagai alternatif penggunaan yang buruk untuk kode produksi import *. 

#### b. Intra-package References
Ketika *package* disusun menjadi sebuah *subpackage*, pengakses dapat menggunakan impor absolutnya untuk merujuk ke submodul lain yang masih berada di *package* yang sama.

Berikut contoh penggunaannya :

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

    Note :
    Impor relatif didasarkan pada nama modul saat ini. Karena nama modul utama selalu "__main__", modul yang dimaksudkan untuk digunakan sebagai modul utama pada Python yang harus selalu menggunakan impor absolut.


#### c. Package in Multiple Directories
Sebuah *package* mendukung satu atribut khusus seperti __path__. Atribut ini dapat diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan paket __init__.py sebelum kode didalam file tersebut dieksekusi. Variabel ini dapat dimodifikasi, namun akan mempengaruhi pencarian modul dan subpaket yang terdapat didalam *package* dikemudian hari. 

## D. Kesimpulan
Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam instance interpreter yang interaktif. File seperti itu disebut modul ; definisi dari sebuah modul dapat diimpor ke modul lain atau ke modul utama (kumpulan variabel yang dapat Anda akses dalam skrip yang dijalankan di tingkat atas dan dalam mode kalkulator).

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .pyditambahkan. Di dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai dari variabel global __name__.