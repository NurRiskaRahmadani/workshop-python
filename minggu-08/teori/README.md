# Standard Library &  (Pertemuan 8)
## A. Latar Belakang
Biasanya, *library* atau perpustakaan merupakan kumpulan buku, ruangan ataupun tempat dimana banyak buku disimpan untuk digunakan kembali kemudian waktu. Sama halnya dengan dunia pemrograman, *library* juga memiliki artian yang serupa yang mana terdiri atas kumpulan kode yang telah dikompilasikan sebelumnya yang kemudian dapat digunakan kembali suatu saat didalam sebuah program komputer. Sebagian besar bahasa pemrograman yang ada memiliki *library* termasuk pada Python. 

*Library* Python sendiri merupakan kumpulan modul yang saling terkait dan berisi kumpulan kode yang dapat digunakan secara berulang kali dalam program yang berbeda. Sehingga lebih sederhana, ringkas dan penggunaannya menjadi nyaman bagi programmer. *Library* Python memainkan peran yang sangat vital dalam banyak lingkup bidang, seperti : *Machine Learning*, *Data Scients*, visualisasi data dll. 

Pada laporan ini, pembahasan yang akan diterangkan adalah mengenai *library* yang ada di Python, apa saja yang ada didalamnya, bagaimana penggunaannya, serta bagaimana cara menerapkannya didalam sebuah program. 

## B. Dasar Teori
Pustaka Standar Python adalah kumpulan modul skrip yang dapat diakses oleh program Python untuk menyederhanakan proses pemrograman dan menghilangkan kebutuhan untuk menulis ulang perintah yang umum digunakan. Mereka dapat digunakan dengan 'memanggil/mengimpor' mereka di awal skrip.

Beberapa *library* Python yang sangat penting dan sering digunakan dalam membangun sebuah program komputer:

1. Matplotlib
Matplotlib membantu dengan analisis data, dan merupakan pustaka plot numerik. Kami membicarakannya dengan Python untuk Ilmu Data.

2. Panda
Panda adalah suatu keharusan untuk ilmu data yang menyediakan struktur data yang cepat, ekspresif, dan fleksibel untuk dengan mudah (dan intuitif) bekerja dengan data terstruktur (tabular, multidimensi, berpotensi heterogen) dan deret waktu.

3. Request
Request adalah Pustaka Python yang memungkinkan Anda mengirim permintaan HTTP/1.1, menambahkan header, data formulir, file multi-bagian, dan parameter dengan kamus Python sederhana yang juga memungkinkan pengaksesan data respons dengan cara yang sama.

4. NumPy
NumPy adalah pustaka Python yang digunakan untuk bekerja dengan array.

Ia juga memiliki fungsi untuk bekerja dalam domain aljabar linier, transformasi fourier, dan matriks.

5. SQLAlchemy
SQLAlchemy adalah perpustakaan dengan pola tingkat perusahaan yang terkenal. Ini dirancang untuk akses database yang efisien dan berkinerja tinggi.

6. BeautifulSoup
Beautiful Soup adalah pustaka Python untuk menarik data dari file HTML dan XML. Ia bekerja dengan parser favorit Anda untuk menyediakan cara idiomatik untuk menavigasi, mencari, dan memodifikasi pohon parse. Ini biasanya menghemat jam atau hari kerja programmer.

7. Pyglet
Pyglet adalah pilihan yang sangat baik untuk antarmuka pemrograman berorientasi objek dalam mengembangkan game.

## C. Library (Modul 10)
### 1. Operating System Interface
Menggunakan module os untuk menjalankan fungsi yang dapat melakukan interaksi dengan sistem operasi pada komputer lokal. 

```python
>>> import os
>>> os.getcwd()
'C:\\Users\\Riska\\workshop-python\\minggu-08'
>>> os.chdir('/server/accesslogs')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [WinError 3] The system cannot find the path specified: '/server/accesslogs'
>>> os.system('mkdir today') 
0
```

Saat akan melakukan interaksi dengan komputer lokal pastikanlah terlebih dahulu untuk menggunakan *import os* atau *from os import^* . Hal ini akan menjaga perintah os.open() tetap dapat dipantau dengan *built-in* dari fungsi open().

*Built-in* fungsi dir() dan help() sangatlah membantu karena bersifat interactive aids untuk bekerja dengan modul yang besar seperti os :

```python
>>> import os
>>> dir(os)
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
>>> help(os)
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    https://docs.python.org/3.11/library/os.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
```

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir
```

### 2. File Wildcards
Menjalankan fungsi dari modul glob untuk membuat file list dari direktori pencarian wildcard.

```python
>>> import glob      
>>> glob.glob('*.py')
[]
```

### 3. Command Line Arguments
Menjalankan skrip utilitas umum yang kerap kali digunakan untuk memproses argumen pada baris perintah dan menyimpannya kedalam atribut modul argv sys.

```python
>>> import sys
>>> print(sys.argv)
['']
```

Atau bisa juga dengan menjalankan modul argparse yang menyediakan mekanisme yang lebih canggih dalam hal memproses argumen dari baris perintah. 
```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
### 4. Error Output Redirection and Program Termination
Menjalankan modul sys dengan menggunakan atribut seperti stdin, stdout dan stder.

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```


### 5. String Pattern Matching
Melakukan pencocokan pola string menggunakan modul re yang menyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. Agar lebih kompleks, ringkas dan dapat dioptimalkan. 

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

### 6. Mathematics
Menjalankan modul math yang dapat memberikan akses ke fungsi pustaka c yang mendasari floating point math :

```python
>>> import math
>>> math.cos(math.pi / 4)
0.7071067811865476
>>> math.log(1024, 2)
10.0
```
ataupun menjalankan fungsi yang sama dengan mengunakan modul random untuk membuat pilihan acak.

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'pear'
>>> random.sample(range(100), 10)
[23, 56, 86, 50, 59, 55, 18, 14, 63, 9]
>>> random.random() 
0.37896565159939977
>>> random.randrange(6) 
1
```

atau bisa juga dengan menjalankan modul statistic untuk menghitung properti statisti dasar seperti rata-rata, median, varian, dll. Yang asalnya dari data numerik. 

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

### 7. Internet Access
Mengakses internet dan memproses protokol internet dengan menjalankan modul urllib.request untuk mengambil data dari URL dan smtplib untuk mengirimkan email. 

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...    for line in response:
...        line = line.decode()             # Convert bytes to a str
...       if line.startswith('datetime'):
...            print(line.rstrip()) 
...
datetime: 2022-04-18T16:33:32.308553+00:00


>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```

### 8. Dates and Times
Menjalankan modul datetime yang menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. 

```python
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2022, 4, 18)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'04-18-22. 18 Apr 2022 is a Monday on the 18 day of April.'
>>> birthday = date(2001, 12, 13)
>>> age = now - birthday
>>> age.days
7431
```

### 9. Data Compression
Melakukan pengarsipan data umum dengan menggunakan format kompresi yang secara langsung didukung oleh model termasuk : zlib, gzib, bz2, lzma, zipfile dan tarfile.

```python
>>> import zlib
>>> s = b'Whatever you want... Whatever you need....'
>>> len(s)
42
>>> t = zlib.compress(s)
>>> len(t)
39
>>> zlib.decompress(t)
b'Whatever you want... Whatever you need....'
>>> zlib.crc32(s)
1775755584
```

### 10. Performance Measurement
Melakukan pengukuran kinerja relatif menggunakan pendekatan yang berbeda untuk masalah yang sama. Serta mengimplementasikan modul timeit untuk menggunakan fitur pengepakan dan pembongkaran tuple. 

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.18918389999998908
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.08774200000152632
```

### 11. Quality Control
Menggunakan salah satu pendekatan untuk mengembangkan perangkat lunak yang berkualitas tinggi dengan menulis tes untuk setiap fungsi pada saat dikembangkan dan menjalankan tes tersebut sesering mungkin selama proses pengembangan. Dan mengimplementasikan modul doctest yang menyediakan alat untuk memindai modul serta memvalidasi tes yang tertanam dalam dokumen program. 

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()  
```

ataupun menggunakan modul unittest yang memungkinkan serangkaian pengujian yang lebih komperehensif untuk mempertahankan file yang berbeda tempat penyimpanannya.

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main() 
```

### 12. Batteries Included
Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan kuat dari paket-paketnya yang lebih besar. Sebagai contoh:

* Modul xmlrpc.client and xmlrpc.server membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama modul, tidak ada pengetahuan langsung atau penanganan XML yang diperlukan.

* email package adalah perpustakaan untuk mengelola pesan email, termasuk MIME dan lainnyaDokumen pesan berbasis RFC 2822 . Tidak sepertismtplibdan poplibyang benar-benar mengirim dan menerima pesan, paket email memiliki perangkat lengkap untuk membangun atau mendekode struktur pesan yang kompleks (termasuk lampiran) dan untuk menerapkan pengkodean internet dan protokol header.

* json, Paket ini menyediakan dukungan kuat untuk menguraikan format pertukaran data populer ini. Modul ini csvmendukung pembacaan dan penulisan file secara langsung dalam format Comma-Separated Value, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh xml.etree.ElementTree, xml.domdan xml.saxpaket. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.

* Modul sqlite3 ini adalah pembungkus untuk pustaka database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.

* Internasionalisasi didukung oleh sejumlah modul termasuk gettext, locale, dan codecspaket.

## D. Library II (Modul 11)
### 1. Output Formatting
Menggunakan modul reprlib yang merupakan versi custom dari fungsi repr() yang disesuaikan untuk tampilan singkat dalam bucket besar. 

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

ataupun menjalankan modul print yang menawarkan kontrol yang lebih canggih untuk hsil output yang lebih bagus.

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

atau bisa juga dengan menerapkan modul textwrap untuk memformat paragraf teks agar sesuai lebar dari layar yang ada. 

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

Dan jangan lupa dengan modul locale yang dapat melakukan pengaksesan pada database melalui format data yang spesifik. Dengan attribut pengelompokan yang bertindak sesuai fungsi dan menyediakannya secara langsung untuk memformat angkat dengan pemisah.

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
<stdin>:1: DeprecationWarning: This method will be removed in a future version of Python. Use 'locale.format_string()' instead.
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

### 2. Templating
Menjalankan modul string sebagai template yang mencakup kelas serbaguna yang memiliki sintaks yang disederhanakan dan cocok untuk diedit oleh pengguna. Sehingga memungkinkan pengguna untuk menyesuaikan aplikasinya tanpa perlu mengubahnya.

Format yang digunakan menggunakan nama placeholder yang dibentuk dengan $ dengan pengidentifikasian Python yang valid.

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

Menggunakan metode subtitute() untuk memunculkan sebuah KeyError ketika tidak ditemukan placeholder didalam kamus atau argumen kata kunci. 

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.167.0_x64__qbz5n2kfra8p0\Lib\string.py", line 121, in substitute
    return self.pattern.sub(convert, self.template)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.167.0_x64__qbz5n2kfra8p0\Lib\string.py", line 114, in convert
    return str(mapping[named])
               ~~~~~~~^^^^^^^
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```

atau bisa juga dengan menjalankan subkelas template yang dapat menentukan pembatas custom.

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...    delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Riska

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...    base, ext = os.path.splitext(filename)
...    newname = t.substitute(d=date, n=i, f=ext)
...    print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Riska
img_1076.jpg --> Riska
img_1077.jpg --> Riska
```

### 3. Working with Binary Data Records Layouts
Menggunakan modul struct yang menyediakan fungsi pack() dan unpack() yang berfungsi untuk bekerja dengan format record biner dengan panjang variabel. 

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

### 4. Mutli-threading
Threading merupakan teknik yang digunakan untuk memisahkan tugas yang tidak bergantung secara berurutan. Sehingga dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima masukan pengguna saat tugas lain berjalan di latar belakang. 

Berikut ini merupakan contoh penerapannya :

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

### 5. Logging
Menjalankan modul logging yang menawarkan sistem logging berfitur lengkap dan fleksibel.

```python
>>> import logging
>>> logging.debug('Debugging information')
>>> logging.info('Informational message')
>>> logging.warning('Warning:config file %s not found', 'server.conf')
WARNING:root:Warning:config file server.conf not found
>>> logging.error('Error occurred')
ERROR:root:Error occurred
>>> logging.critical('Critical error -- shutting down')
CRITICAL:root:Critical error -- shutting down
```

### 6. Weak References
```python
>>> import weakref, gc
>>> class A:
...    def __init__(self, value):
...        self.value = value
...    def __repr__(self):
...        return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
    ~^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.167.0_x64__qbz5n2kfra8p0\Lib\weakref.py", line 136, in __getitem__
    o = self.data[key]()
        ~~~~~~~~~^^^^^
KeyError: 'primary'
```

### 7. Tools for Working with Lists
Menjalankan modul array yang menyediakan fungsi array() sebagai objek yang berupa daftar yang hanya dapat menyimpan data homogen.

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

Menjalankan modul collections yang menyediakan fungsi deque() sebagai objek yang berupa daftar dengan penambahan dan kemunculan yang lebih cepat. 

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```

```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```

Menggunakan modul bisect untuk memanipulasi daftar yang diurutkan. 

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

Menggunakan modul heapq yang menyediakan fungsi untuk mengimplementasikan heap berdasarkan daftar reguler. Sehingga entri yang bernilai kecil akan disimpan di posisi nol.

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]
[-5, 0, 1]
```

### 8. Decimal Floating Point Arithmetic
Menggunakan modul decimal yang menawarkan tipe data decimal untuk aritmatika titik mengambang desimal. Dan membandingkannya dengan implementasi float untuk built-in dari floating point biner.

Berikut ini cara penerapannya dalam menghitung pajak.

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```

Hasil dari desimal akan tetap nol, dan secara otomatis akan menyimpulkan secara signifikan ke empat tempat dari perkalian dengan signifikan dua tempat. 

Representasi yang tepat memungkinkan kelas Decimal adalah untuk melakukan perhitungan modulo dan tes kesetaraan yang tidak cocok untuk floating point biner. 

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995
>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```

Dengan menjalankan modul decimal dengan presisi yang banyak. 
```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```


## E. Kesimpulan
Pustaka Standar Python adalah kumpulan modul skrip yang dapat diakses oleh program Python untuk menyederhanakan proses pemrograman dan menghilangkan kebutuhan untuk menulis ulang perintah yang umum digunakan. Mereka dapat digunakan dengan 'memanggil/mengimpor' mereka di awal skrip.

Beberapa *library* Python yang sangat penting dan sering digunakan dalam membangun sebuah program komputer:
1. Matplotlib
2. Panda
3. Request
4. NumPy
5. SQLAlchemy
6. BeautifulSoup
7. Pyglet

