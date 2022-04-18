# Penanganan Error dan Exception (Pertemuan 6)
## A. Latar Belakang
Sangat lumrah terjadi apabila pada saat seorang pengembang sedang menjalankan programnya mengalami *error* (Kesalahan) atau *exception* (Pengecualian). Maka dari itu pengembang haruslah sigap dan mengetahui cara penanganannya, agar pada saat menjalankan program output dapat diterima. Walaupun begitu, bahasa pemrograman yang dipakai juga dapat membantu menangani error ataupun exception yang terjadi. 

Pada Python terdapat beberapa pembagian error yang dapat di pecahkan dan juga dapat diterapkan untuk mempermudah pengembang dalam merumuskan serta menjalankan program miliknya tanpa adanya gangguan.

## B. Dasar Teori
*error* (Kesalahan) merupakan masalah dalam suatu program yang menyebabkan program akan menghentikan eksekusi. Adapun *exception* (Pengecualian) akan dimunculkan ketika beberapa peristiwa internal yang terjadi mengubah aliran normal program. 

Pada Python terdapat dua jenis error, yakni :
- *Syntax Errors* (Kesalahan Sintaks)
- *Logical Errors* (Kesalahan Logis/Pengecualian)

## C. Penanganan Error dan Exception
### 1. Syntax Errors
*Syntax errors* atau kesalahan sintaks yang juga dikenal sebagai kesalahan dalam penguraian dan mungkin merupakan jenis keluhan paling umum yang dapat didapatkan pada bahasa Python. Berikut ini contoh penerapannya :

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

*Parser* atau pengurai akan mengulangi baris yang bersinggungan dan yang menampilkan tanda panah kecil yang menunjuk pada titik paling awal di baris tempat error/kesalahan terdeteksi. Error yang terjadi disebabkan oleh token sebelum tanda panah. Dapat dilihat pada potongan skrip kode diatas bahwa error yang terdeteksi adalah pada fungsi print(), diketahui bahwa error tersebut terjadi karena tidak adanya tanda titik dua (':') yang merupakan sintaks yang seharusnya didalam kode program. Untuk memberitahu bahwa sintaks yang dimasukan salah maka program akan mencetak kembali nama file dan nomor dari baris yang terdeteksi salah, sehingga memudahkan pengembang untuk mengetahui dimana letak terjadinya kesalahan. 


### 2. Exceptions
Pada umumnya, walaupun sebuah program memiliki pernyataan/ekspresi yang dituliskan benar secara sintaksisnya, namun tidak menutup kemungkinan bahwa program tersebut tidak memiliki error didalamnya ketika di eksekusi. 

Error yang terdeteksi selama eksekusi disebut sebagai *exception* (Pengecualian) yang keberadaannya tidak fatal dengan syarat: pengembang mengetahui cara penanganannya pada Python. Selain itu, sebagian besar *exception* tidak dapat ditangani oleh program sehingga menghasilkan output berupa pesan kesalahan. 

Berikut ini merupakan contoh program yang menunjukkan pesan kesalahan ketika dieksekusi :

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Dibaris terakhir dari pesan error yang menunjukkan apa yang terjadi pada kode program diatas. Muncul sebuah *exception* dalam tipe berbeda dan tipe tipe tersebut dicetak sebagai bagian dari pesan: 
    contoh untuk tipe pertama dapat dilihat pada program yang memunculkan pesan *ZeroDivisionError*, *NameError* dan *TypeError*. 

Adapun untuk string yang dicetak sebagai tipe *exception* adalah nama dari *exception* bawaan yang terjadi. Hal ini berlaku untuk semua jenis *exception* bawaan, kecuali untuk yang telah ditentukan oleh user/pengembang. Nama *exception* standar sendiri adalah untuk mengidentifikasi sintaks bawaan.

Sisa dari baris akan memberikan detail berdasarkan jenis *exception* yang ditampilkan serta penyebab munculnya. Bagian dari pesan error pada program sebelumnya akan menunjuk kearah konteks di mana adanya *exception* terjadi. Baik itu dalam bentuk *stack traceback*.

### 3. Handling Exceptions
Python memungkinkan seorang pengembang untuk menulis program yang dapat menangani *exception* sendiri. Berikut contoh implementasinya didalam Python :

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number. Try again...")
...
```

Pernyataan *try* pada program yang dibuat memiliki beberapa fungsi seperti :
    - Klausa *try* seperti *statement* yang berada diantara kata kunci *try* dan *except* dapat dieksekusi.
    - Jika tidak terjadi *exception* pada program, klausa *except* akan dilewati dan eksekusi untuk pernyataan *try* selesai.
    - Jika tidak terdapat *exception* selama proses eksekusi untuk klausa *try*, maka sisa klausa yang ada akan dilewati. Kemudian, jika tipenya cocok dengan *exception* yang dinamai dengan kata kunci *except*, klausa tersebut akan dieksekusi dan dilanjutkan lagi setelah melewati baris *try*/*except*.
    - Jika terjadi *exception* yang tidak cocok dengan *exception* yang disebutkan dalam klausa *except* maka ekskusi akan diterukan ke pernyataan luar untuk *try*, yang mana jika penanganannya tidak ditemukan.

Pada dasarnya sebuah pernyataan *try* mungkin saja memiliki lebih dari satu klausa *except* yang dapat menentukan penanganan untuk *exception* yang berbeda. Paling banyak akan mengeksekusi satu handler pada saat program dieksekusi. 

Adapun untuk penanganan yang hanya menangani *exception* yang terjadi pada klausa *try* yang sesuai akan dilakukan oleh *handler*. Klausa *exception* dapat menyebutkan beberapa *excpetion* lain sebagai tuple didalam kurung, contoh :

```python
... except (RuntimeError, TypeError, NameError):
...     pass
``` 

Sedangkan untuk kelas yang berada didalam klausa *except* yang kompatible dengan *exception if* itu adalah ketika berada kelas yang sama atau kelas dasar *thereof*. Berikut bentuk implementasinya pada interpreter Python :

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Note :
Jika klausa *except* dibalik penempatannya dengan yang berada pada baris pertama, maka program akan dicetak sesuai dengan pencocokan pada klausa pertama yakni *except*. 

Semua jenis *exception* mewarisi turunan dari *BaseException*, sehingga dapat digunakan sebagai karakter pengganti. Walaupun begitu, pengunaan *exception* ini sangat rawan sehingga harus hati hati, berikut ini contoh implementasi pada interpreter Python :

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

Note :
Sebagai alternatif, klausa exception terakhir pada baris program dapat menghilangkan nama exception, namun untuk pengambilan nilainya harus diambil dengan menggunakan perintah sys.exception().

Pernyataan *try .... except* juga memiliki opsi klausa *else*, yang, jika ada, dan semuanya haruslah mengikuti klausa *except*. Jika klausa *try* tidak memunculkan ekspresi maka perintah sebelumnya dapat berguna sebagai kode yang dapat dijalankan. Berikut ini merupakan contoh implementasinya :

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

Penggunaan klausa *else* lebih baik daripada menambahkan kode tambahan kedalam klausa *try* karena dapat menghindari ketidaksengajaan penangkapan *exception* yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan *try ... except*.

Klausa *except* juga dapat menentukan variabel yang berada setelah nama *exception*. Variabel yang terikat ke *exception instance* yang disertai dengan argumen yang tersimpan didalam instance.args. 

Berikut ini merupakan implementasi penggunaan instance.args didalam interpreter Python :

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses    
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Note :
Jika sebuah exception memiliki argumen, maka argumen tersebut akan dicetak sebagai bagian terakhir atau sebagai detail dari pesan untuk exception yang tidak ditangani. 

*Exception Handler* tidak hanya untuk menangani eksepsi yang sedang terjadi di klausa *try*, tetapi juga jika hal yang sama terjadi didalam fungsi yang dipanggil di klausa *try*. Berikut ini merupakan contoh penerapannya :

```python
>>> def this_fails():
...     x = 1/0
... 
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
... 
Handling run-time error: division by zero
```

### 4. Raising Exceptions
Pernyataan *Raise* pada Python memungkinkan seorang pengembang untuk memaksa penggunaan *exception* didalam program. Contoh :

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Pada potongan kode program diatas dapat dilihat bahwa, satu satunya argumen untuk *raise* menunjukkan *exception* yang akan diajukan. Haruslah berupa *Exception Instance* atau kelas *exception*. Jika kelas *exception* dilewatkan, itu akan secara implisit dipakai dengan memanggil konstruktornya tanpa disertai sebuah argumen.

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

Berikut ini merupakan contoh dari implementasi pernyataan *raise* untuk menentukan apakah *exception* telah dimunculkan namun tidak bermaksud untuk menangani errornya :

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
... 
An exception flew by!
Traceback (most recent call last):   
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

### 5. Exception Chaining
Pernyataan *raise* pada Python memungkinkan penggunaan sebuah opsi *from* yang menunjukan kemungkinan *chaining exceptions*. Misal :

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

```python
>>> def func():
...     raise ConnectionError
... 
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
... 
Traceback (most recent call last):   
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Note :
Chaining exception akan muncul secara otomatis ketika exception dinaikan di dalam bagian except atau finally. Hal ini dapat dinonaktifkan dengan menggunakan idiom "from none".

Contoh implementasi menonaktifkan *chaining exception* pada program didalam interpreter Python :
```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
... 
Traceback (most recent call last):   
  File "<stdin>", line 4, in <module>
RuntimeError
```

### 6. User-defined Exceptions
Pada Python program dapat memberi nama *exception* nya sendiri dengan membuatkan sebuah kelas *exception* baru. *Exception* biasanya harus diturunkan dari kelas *exception*, baik secara langsung maupun tidak langsung.

Kelas *exception* dapat didefinisikan sebagai kelas yang dapat melakukan apa saja yang dilakukan oleh kelas lainnya dalam bentuk sederhana dan seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh *handler* untuk sebuah *exception*.

Hal ini terjadi karena sebagian besar *exception* didefenisikan dengan nama yang diakhiri dengan error/kesalahan, yang mirip dengan penamaan *standard exceptions*.


### 7. Defining Clean-up Actions
Pernyataan *try* pada Python memiliki opsi klausa lain yang dimaksudkan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam keadaan apapun. Contoh :

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
... 
Goodbye, world!
Traceback (most recent call last):   
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

Note :
Jika didalam sebuah program terdapat klausa finally, klausa tersebut akan mengeksekusi task terakhir sebelum pernyataan try selesai. Ketika klausa finally berjalan maka pernyataan try akan di periksa, apakah pernyataan tersebut menghasilkan sebuah exception atau tidak. 

Poin poin yang kerap terjadi ketika pada sebuah program muncul *exception* yang lebih kompleks :
- Jika *exception* terjadi selama proses eksekusi klausa *try*, *exception* dapat langsung ditangani oleh klausa *except*. Jika eksepsi tidak ditangani oleh klausa *except*, maka eksepsi akan dimunculkan kembali setelah klausa *finally* selesai dieksekusi. 
- Jika klausa *finally* mengeksekusi sebuah *break*, *continue*, atau pernyataan *return*. *Exception* tidak akan dimunculkan kembali.
- Jika pernyataan *try* mencapai *break*, *continue* atau pernyataan *return*, klausa *finally* akan dieksekusi tepat sebelum *break*, *continue* atau pernyataan *return* di eksekusi.
- Jika klausa *finally* menyertakan sebuah pernyataan *return*, maka nilai yang dikembalikan akan menjadi nilai dari pernyataan *finally* klausa *return*, bukan nilai dari pernyataan *try* klausa *return*.

Contoh sederhana untuk implementasi klausa *finally* didalam interpreter Python :

```python
>>> def bool_return():
...     try:
...             return True
...     finally:
...             return False
... 
>>> bool_return()
False
```

Contoh lainnya dalam tingkat yang lebih rumit :

```python
>>> def divide(x, y):
...     try:
...          result = x / y
...     except ZeroDivisionError:
...          print("division by zero!")
...     else:
...          print("result is", result)
...     finally:
...          print("executing finally clause")
... 
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0) 
division by zero!       
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

### 8. Predefined Clean-Up Actions
Pada Python beberapa objek dapat menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan oleh program, terlepas dari apakah operasi menggunakan objek tersebut berhasil atau gagal.

Berikut ini merupakan contoh dari implementasi percobaan untuk membuka file dan mencetak isinya :

```python
for line in open("myfile.txt"):
    print(line, end="")
```

Masalah yang ditimbulkan oleh kode ini adalah membiarkan file terbuka untuk waktu yang lama dan tidak ditentukan setelah bagian potongan kode program diatas selesai dieksekusi. Hal ini bukan saja dapat menjadi masalah didalam sebuah skrip kode sederhana namun dapat juga menjadi masalah untuk sebuah aplikasi yang lebih besar. Pernyataan *with* memungkinkan objek seperti file untuk digunakan dengan cara yang memastikan mereka selalu dibersihkan dengan cepat dan benar. 

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah pernyataan untuk membuka file selesai dieksekusi pada potongan kode program diatas, maka untuk file f akan ditutup,  bahkan jika terdapat masalah saat memproses baris.


### 9. Raising and Handling Multiple Unrelated Exceptions
Python juga memiliki fasilitas berupa *ExceptionGroup* yang dapat digunakan untuk membungkus daftar *Exception instance* sehingga dapat dimunculkan bersama. 

Berikut ini merupakan implementasi dari penggunaan *ExceptionGroup* didalam interpreter Python :

```python
>>> def f():
...     excs = [OSError('error 1'), SystemError('error 2')]
...     raise ExceptionGroup('there were problems', excs)
... 
>>> f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |   File "<stdin>", line 3, in f
  | ExceptionGroup: there were problems  
  +-+---------------- 1 ---------------- 
    | OSError: error 1
    +---------------- 2 ---------------- 
    | SystemError: error 2
    +------------------------------------
>>> try:
...     f()
... except Exception as e:
...     print(f'caught {type(e)}: e')
... 
caught <class 'ExceptionGroup'>: e
```

Penggunaan *Except* yang disertai tanda * dapat secara selektif hanya menangani *exception* dalam grup yang cocok dengan tipe tertentu. Setiap klausa except* mengekstrak *exception* grup dari tipe tertentu sembari membiarkan semua *exception* lain menyebar ke seluruh klausa lain dan akhirnya dinaikkan lagi. 

```python
>>> def f():
...     raise ExceptionGroup("group1",
...                             [OSError(1),
...                              SystemError(2),
...                              ExceptionGroup("group2",
...                                             [OSError(3), RecursionError(4)])])
... 
>>> try:
...     f()
... except* OSError as e:
...     print("There were OSErrors")
... except* SystemError as e:
...     print("There were SystemErrors")
... 
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |   File "<stdin>", line 2, in f
  | ExceptionGroup: group1
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
```

Note :
Exceptions nested dalam grup exception haruslah berupa instance dan bukan tipe. Ini karena dalam praktiknya exception yang telah dimunculkan dan ditangkap oleh program.

Berikut ini merupakan pola yang dapat dilakukan untuk praktik *Exception nested* :

```python
>>> excs = []
... for test in tests: 
...     try:
...          test.run()
...     except Exception as e:
...          excs.append(e)
...
>>> if excs:
...     raise ExceptionGroup("Test Failures", excs)
...
```

## D. Kesimpulan
*error* (Kesalahan) merupakan masalah dalam suatu program yang menyebabkan program akan menghentikan eksekusi. Adapun *exception* (Pengecualian) akan dimunculkan ketika beberapa peristiwa internal yang terjadi mengubah aliran normal program. 

Pada Python terdapat dua jenis error, yakni :
- *Syntax Errors* (Kesalahan Sintaks)
- *Logical Errors* (Kesalahan Logis/Pengecualian)

1. Syntax Errors
*Syntax errors* atau kesalahan sintaks yang juga dikenal sebagai kesalahan dalam penguraian dan mungkin merupakan jenis keluhan paling umum yang dapat didapatkan pada bahasa Python. 

*Parser* atau pengurai akan mengulangi baris yang bersinggungan dan yang menampilkan tanda panah kecil yang menunjuk pada titik paling awal di baris tempat error/kesalahan terdeteksi.

2. Exceptions
Error yang terdeteksi selama eksekusi disebut sebagai *exception* (Pengecualian) yang keberadaannya tidak fatal dengan syarat: pengembang mengetahui cara penanganannya pada Python. Selain itu, sebagian besar *exception* tidak dapat ditangani oleh program sehingga menghasilkan output berupa pesan kesalahan.

