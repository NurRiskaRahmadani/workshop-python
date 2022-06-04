# PYTHON UNTUK DATA ANALYTICS (Petemuan 13)
## A. Latar Belakang
Library python merupakan kumpulan modul yang saling terkait yang tersusun atas kumpulan kode yang dapat digunakan berulang kali dalam program berbeda. Adanya *library* pada bahasa pemrograman Python ini memudahkan programmer untuk menulis kode agar lebih sederhana dan tidak berulang sehingga dapat digunakan oleh program yang berbeda. Hal tersebut memberi kesan lebih nyaman dalam penggunaannya. 

Berdasarkan uraian tersebut, pada pertemuan kali ini pembahasan yang akan diulas adalah seputar salah satu *library* Python yang banyak dipakai, yaitu pandas. 

## B. Dasar Teori
Pandas adalah sebuah *library* di Python yang berlisensi BSD dan open source yang menyediakan struktur data dan analisis data yang mudah digunakan. Pandas biasa digunakan untuk membuat tabel, mengubah dimensi data, mengecek data, dan lain sebagainya. 

Struktur data dasar pada Pandas dinamakan DataFrame, yang memudahkan kita untuk membaca sebuah file dengan banyak jenis format seperti file .txt, .csv, dan .tsv. Fitur ini akan menjadikannya *table* dan juga dapat mengolah suatu data dengan menggunakan operasi seperti *join, distinct, group by*, agregasi, dan teknik lainnya yang terdapat pada SQL. 

*Library* Pandas memiliki dua tipe struktur data untuk versi terbaru yaitu Series dan *Data Frame* serta satu *deprecated* struktur data yaitu Panel (*deprecated*). Series diibaratkan sebagai array satu dimensi sama halnya dengan numpy array, hanya bedanya mempunyai index dan kita dapat mengontrol index dari setiap elemen tersebut. Sedangkan data frame merupakan array dua dimensi dengan baris dan kolom. Struktur data ini merupakan cara paling standar untuk menyimpan data dalam bentuk tabel/data tabular. 


## C. Pandas
### a. Installation
1. Download Anaconda/Miniconda untuk mengoperasikan system berdasarkan versi Python nya.
2. Memulai JupyterLab pada terminal Anaconda prompt
3. Membuat notebook Python baru pada JupyterLab
4. Pada cell pertama di notebook yang telah di *create*, tuliskan perintah untuk import *library* serta perintah untuk mengecek versi *library* yang digunakan.

```python
>>> import pandas
>>> pandas.__version__
'1.3.4'
```

5. Library siap digunakan.

### b. 10 Minutes to Pandas
Mengimport *library* :
```python
import numpy as np

import pandas as pd
```
### c. Objek creation
Membuat sebuah series dengan melewatkan value pada list, lalu membiarkan *library* pandas untuk membuat indeks integer secara default :

```python
>>> s = pd.Series([1, 3, 5, np.nan, 6, 8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

Membuat sebuah DataFrame dengan melewatkan Numpy array dengan indeks *datetime* serta kolum yang memiliki label :

```python
>>> dates = pd.date_range("20130101", periods=6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
>>> df
	                A	        B	        C	        D
2013-01-01	 0.592906	-1.373777	-0.476581	-0.244752
2013-01-02	 1.461727	-0.896770	-0.287464	 0.542393
2013-01-03	 0.323090	 0.111268	 1.270370	-0.078373
2013-01-04	 0.029617	-1.159389	-0.344211	-0.186690
2013-01-05	 0.879345	 0.723307	-0.691894	 0.907711
2013-01-06	-1.108614	 0.848174	 0.149078	-1.744671
```

Membuat sebuah DataFrame dengan melewatkan kamus oobjek yang dapat diubah menjadi struktur seperti series :

```python
>>> df2 = pd.DataFrame(
...    {
...        "A": 1.0,
...        "B": pd.Timestamp("20130102"),
...        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
...        "D": np.array([3] * 4, dtype="int32"),
...        "E": pd.Categorical(["test", "train", "test", "train"]),
...        "F": "foo",
...    }
... )
...
>>> df2

     A	         B	 C	D	    E	  F
0	1.0	2013-01-02	1.0	3	 test	foo
1	1.0	2013-01-02	1.0	3	train	foo
2	1.0	2013-01-02	1.0	3	 test	foo
3	1.0	2013-01-02	1.0	3	train	foo
```

Membuat kolom dengan hasil dari penggunaan DataFrame yang memiliki dtypes berbeda. 

```python
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```


### d. Viewing data
Melihat baris dari bagian atas hingga paling bawah data :
```python
>>> df.head()
                      A	        B   	   C	        D
2013-01-01	0.592906	-1.373777	-0.476581	-0.244752
2013-01-02	1.461727	-0.896770	-0.287464	 0.542393
2013-01-03	0.323090	 0.111268	 1.270370	-0.078373
2013-01-04	0.029617	-1.159389	-0.344211	-0.186690
2013-01-05	0.879345	 0.723307	-0.691894	 0.907711
>>> df.tail(3)
	                 A	        B	        C	        D
2013-01-04	 0.029617	-1.159389	-0.344211	-0.186690
2013-01-05	 0.879345	 0.723307	-0.691894	 0.907711
2013-01-06	-1.108614	 0.848174	 0.149078	-1.744671
```

Menampilkan indeks dari kolom :
```python
>>> df.index 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

>>> df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')
```

Baris perintah **DataFrame.to_numpy()** memberikan representasi Numpy dari data yang mendasarinya. Numpy arrat memiliki salah satu dtype untuk seluruh array, sedangkan pandas DataFrames memiliki satu dtype per column. Untuk itu df (DataFrame) dari semua nilai floating-point, **DataFrame.to_numpy()** akan lebih cepat penggunaannya karena tidak memerlukan penyalinan data. 

```python
>>> df.to_numpy()
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])

>>> df2.to_numpy()
array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
      dtype=object)
```

Perintah **.describe()** menunjukkan ringkasan statistik cepat dari data yang dimiliki. Berikut ini contoh penerapannya :

```python
>>> array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
      dtype=object)

  A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.073711 -0.431125 -0.687758 -0.233103
std    0.843157  0.922818  0.779887  0.973118
min   -0.861849 -2.104569 -1.509059 -1.135632
25%   -0.611510 -0.600794 -1.368714 -1.076610
50%    0.022070 -0.228039 -0.767252 -0.386188
75%    0.658444  0.041933 -0.034326  0.461706
max    1.212112  0.567020  0.276232  1.071804
```

Perintah untuk melakukan transpos data :
```python
>>> df.T
     2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A      0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
B     -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
C     -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
D     -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
```

Menambahkan perintah **.sort** untuk menyortir data pada kolom berdasarkan sebuah **axis** :
```python
>>> df.sort_index(axis=1, ascending=False)
                   D         C         B         A
2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
2013-01-02 -1.044236  0.119209 -0.173215  1.212112
2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
2013-01-04  0.271860 -1.039575 -0.706771  0.721555
2013-01-05 -1.087401  0.276232  0.567020 -0.424972
2013-01-06  0.524988 -1.478427  0.113648 -0.673690
```

Menambahkan perintah **.sort** untuk menyortir data pada kolom berdasarkan nilai/value :
```python
>>> df.sort_values(by="B")
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
```


### e. Selection
#### 1. Getting 
Menuliskan perintah untuk memanggil data dengan memilih satu kolom yang dapat menampilkan data serias a :
```python
>>> df["A"]
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555
2013-01-05   -0.424972
2013-01-06   -0.673690
Freq: D, Name: A, dtype: float64
```

Menuliskan perintah untuk memanggil data dengan memilih melalui [], yang dapat mengiris baris :
```python
>>> df[0:3]
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804

>>> df["20130102":"20130104"]
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```

#### 2. Selection By Label
Menuliskan perintah untuk mendapatkan *cross section* menggunakan label :
```python
>>> df.loc[dates[0]]
A    0.469112
B   -0.282863
C   -1.509059
D   -1.135632
Name: 2013-01-01 00:00:00, dtype: float64
```

Menuliskan perintah untuk melakukan seleksi pada *multi-axis* berdasarkan labelnya :
```python
>>> df.loc[:, ["A", "B"]]
                   A         B
2013-01-01  0.469112 -0.282863
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
2013-01-06 -0.673690  0.113648
```

Menampilkan pemotongan label, kedua titik akhir :
```python
>>> df.loc["20130102":"20130104", ["A", "B"]]
                   A         B
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
```

Pengurangan dimensi objek yang dikembalikan :
```python
>>> df.loc["20130102", ["A", "B"]]
A    1.212112
B   -0.173215
Name: 2013-01-02 00:00:00, dtype: float64
```

Perintah untuk mendapatkan nilai skalar :
```python 
>>> df.loc[dates[0], "A"]
0.4691122999071863
```

Perintah untuk mendapatkan akses cepat ke skalar :
```python
>>> df.at[dates[0], "A"]
0.4691122999071863
```

#### 3. Selection By Position
Memilih data melalui posisi bilangan bulat yang diteruskan :
```python
>>> df.iloc[3]
A    0.721555
B   -0.706771
C   -1.039575
D    0.271860
Name: 2013-01-04 00:00:00, dtype: float64
```

Dengan irisan bilangan bulat, pengoperasian ini memiliki kesamaan dengan yang ada pada *library* NumPy/Python :
```python
>>> df.iloc[3:5, 0:2]
                   A         B
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
```

Daftar lokasi posisi bilangan bulat :
```python
>>> df.iloc[[1, 2, 4], [0, 2]]
                   A         C
2013-01-02  1.212112  0.119209
2013-01-03 -0.861849 -0.494929
2013-01-05 -0.424972  0.276232
```

Mengiris baris secara eksplisit :
```python
>>> df.iloc[1:3, :]
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
```

Mengiris kolom secara eksplisit :
```python
>>> df.iloc[:, 1:3]
                   B         C
2013-01-01 -0.282863 -1.509059
2013-01-02 -0.173215  0.119209
2013-01-03 -2.104569 -0.494929
2013-01-04 -0.706771 -1.039575
2013-01-05  0.567020  0.276232
2013-01-06  0.113648 -1.478427
```

Menulis perintah untuk mendapat nilai secara eksplisit :
```python
>>> df.iloc[1, 1]
-0.17321464905330858
```

Menulis perintah untuk mendapat akses cepat ke skalar :
```python
>>> df.iat[1, 1]
-0.17321464905330858
```

#### 4. Boolean Indexing 
Menulis perintah untuk menggunakan nilai kolom tunggal agar dapat memilih data :
```python
>>> df[df["A"] > 0] 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```

Menulis perintah untuk memilih nilai dari DataFrame tempat kondisi boolean terpenuhi :
```python
>>> df[df > 0] 
                   A         B         C         D
2013-01-01  0.469112       NaN       NaN       NaN
2013-01-02  1.212112       NaN  0.119209       NaN
2013-01-03       NaN       NaN       NaN  1.071804
2013-01-04  0.721555       NaN       NaN  0.271860
2013-01-05       NaN  0.567020  0.276232       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
```

Menggunakan metode **.isin()** untuk melakukan *filtering* :
```python 
>>> df2 = df.copy()

>>> df2["E"] = ["one", "one", "two", "three", "four", "three"]

>>> df2
                   A         B         C         D      E
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three

>>> [df2["E"].isin(["two", "four"])]
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
```

#### 5. Setting
Menulis perintah untuk menyetel kolom baru secara otomatis yang dapat selaras dengan data pada indeks :
```python
>>> s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

>>> s1
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64

>>> df["F"] = s1
```

Menulis perintah untuk menetapkan nilai menurut label :
```python
>>> df.at[dates[0], "A"] = 0
```

Menulis perintah untuk menetapkan nilai menurut posisi :
```python
>>> df.iat[0, 1] = 0
```

Menulis perintah yang berupa pengaturan yang dapat menetapkan value data dengan array NumPy :
```python
>>> df.loc[:, "D"] = np.array([5] * len(df))
```

Melihat hasil dari operasi yang diinputkan pada pengaturan sebelumnya :
```python
>>> df
                  A         B         C   D    F
2013-01-01  0.000000  0.000000 -1.509059  5  NaN
2013-01-02  1.212112 -0.173215  0.119209  5  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0
2013-01-05 -0.424972  0.567020  0.276232  5  4.0
2013-01-06 -0.673690  0.113648 -1.478427  5  5.0
```

Operasi **where** dengan pengaturan :
```python
>>> df2 = df.copy()

>>> df2[df2 > 0] = -df2

>>> df2 
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 -1.509059 -5  NaN
2013-01-02 -1.212112 -0.173215 -0.119209 -5 -1.0
2013-01-03 -0.861849 -2.104569 -0.494929 -5 -2.0
2013-01-04 -0.721555 -0.706771 -1.039575 -5 -3.0
2013-01-05 -0.424972 -0.567020 -0.276232 -5 -4.0
2013-01-06 -0.673690 -0.113648 -1.478427 -5 -5.0
```

### f. Missing data
```python
>>> df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])

>>> df1.loc[dates[0] : dates[1], "E"] = 1

>>> df1
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  NaN  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  NaN
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  NaN

>>> df1.dropna(how="any")
                   A         B         C  D    F    E
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0

>>> df1.fillna(value=5)
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  5.0  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  5.0
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  5.0

>>> pd.isna(df1)
                A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
```

### g. Operations
#### 1. Stats
Statistik deskriptif :
```python 
>>> df.mean()
A   -0.004474
B   -0.383981
C   -0.687758
D    5.000000
F    3.000000
dtype: float64
```

Operasi yang sama pada sumbu yang lain :
```python 
>>> df.mean(1)
2013-01-01    0.872735
2013-01-02    1.431621
2013-01-03    0.707731
2013-01-04    1.395042
2013-01-05    1.883656
2013-01-06    1.592306
Freq: D, dtype: float64
```

Beroperasi dengan objek yang memiliki dimensi berbeda dan membutuhkan penyelarasan. 
```python
>>> s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

>>> s
2013-01-01    NaN
2013-01-02    NaN
2013-01-03    1.0
2013-01-04    3.0
2013-01-05    5.0
2013-01-06    NaN
Freq: D, dtype: float64

>>> df.sub(s, axis="index")
                   A         B         C    D    F
2013-01-01       NaN       NaN       NaN  NaN  NaN
2013-01-02       NaN       NaN       NaN  NaN  NaN
2013-01-03 -1.861849 -3.104569 -1.494929  4.0  1.0
2013-01-04 -2.278445 -3.706771 -4.039575  2.0  0.0
2013-01-05 -5.424972 -4.432980 -4.723768  0.0 -1.0
2013-01-06       NaN       NaN       NaN  NaN  NaN

```

#### 2. Apply
```python
>>> df.apply(np.cumsum) 
                   A         B         C   D     F
2013-01-01  0.000000  0.000000 -1.509059   5   NaN
2013-01-02  1.212112 -0.173215 -1.389850  10   1.0
2013-01-03  0.350263 -2.277784 -1.884779  15   3.0
2013-01-04  1.071818 -2.984555 -2.924354  20   6.0
2013-01-05  0.646846 -2.417535 -2.648122  25  10.0
2013-01-06 -0.026844 -2.303886 -4.126549  30  15.0

>>> df.apply(lambda x: x.max() - x.min()) 
A    2.073961
B    2.671590
C    1.785291
D    0.000000
F    4.000000
dtype: float64
```

#### 3. Histogramming
```python
>>> s = pd.Series(np.random.randint(0, 7, size=10))

>>> s 
0    4
1    2
2    1
3    2
4    6
5    4
6    4
7    6
8    4
9    4
dtype: int64

>>> s.value_counts() 
4    5
2    2
6    2
1    1
dtype: int64
```

#### 4. String Methods
Series dilengkapi dengan sekumpulan metode pemrosesan string didalam atribut str, yang dapat memudahkan pengoperasian pada setiap elemen larik, seperti pada contoh penerapan dibawah ini :
```python
>>> s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

>>> s.str.lower() 
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object
```

### h. Merge
#### 1. Concat 
```python
>>> df = pd.DataFrame(np.random.randn(10, 4))

>>> df
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495

# break it into pieces
>>> pieces = [df[:3], df[3:7], df[7:]]

>>> pd.concat(pieces)
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495
```

#### 2. Join
```python
>>> left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

>>> right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

>>> left
   key  lval
0  foo     1
1  foo     2

>>> right
   key  rval
0  foo     4
1  foo     5

>>> pd.merge(left, right, on="key")
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5

>>> left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})

>>> right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})

>>> left 
   key  lval
0  foo     1
1  bar     2

>>> right 
   key  rval
0  foo     4
1  bar     5

>>> pd.merge(left, right, on="key")
   key  lval  rval
0  foo     1     4
1  bar     2     5
```

### i. Grouping
```python
>>> df = pd.DataFrame(
...    {
...        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
...        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
...        "C": np.random.randn(8),
...        "D": np.random.randn(8),
...    }
... )

>>> df 
     A      B         C         D
0  foo    one  1.346061 -1.577585
1  bar    one  1.511763  0.396823
2  foo    two  1.627081 -0.105381
3  bar  three -0.990582 -0.532532
4  foo    two -0.441652  1.453749
5  bar    two  1.211526  1.208843
6  foo    one  0.268520 -0.080952
7  foo  three  0.024580 -0.264610

>>> df.groupby("A").sum()
            C         D
A                      
bar  1.732707  1.073134
foo  2.824590 -0.574779

>>> df.groupby(["A", "B"]).sum()
                  C         D
A   B                        
bar one    1.511763  0.396823
    three -0.990582 -0.532532
    two    1.211526  1.208843
foo one    1.614581 -1.658537
    three  0.024580 -0.264610
    two    1.185429  1.348368
```

### j. Reshaping
#### 1. Stack
```python
>>> tuples = list(
...    zip(
...        *[
...            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
...            ["one", "two", "one", "two", "one", "two", "one", "two"],
...        ]
...    )
... )

>>> index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

>>> df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

>>> df2 = df[:4]

>>> df2 
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431

>>> stacked = df2.stack()

>>> stacked
first  second   
bar    one     A   -0.727965
               B   -0.589346
       two     A    0.339969
               B   -0.693205
baz    one     A   -0.339355
               B    0.593616
       two     A    0.884345
               B    1.591431
dtype: float64
```

Dengan DataFrame atau seri *stack* yang memiliki **MultiIndex** sebagai **index**, daam dapat menjalankan operasi **.stack()** serta **.unstack()**, yang secara default dapat membongkar level terakhir :
```python
>>> stacked.unstack()
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431

>>> stacked.unstack(1) 
second        one       two
first                      
bar   A -0.727965  0.339969
      B -0.589346 -0.693205
baz   A -0.339355  0.884345
      B  0.593616  1.591431

>>> stacked.unstack(0) 
first          bar       baz
second                      
one    A -0.727965 -0.339355
       B -0.589346  0.593616
two    A  0.339969  0.884345
       B -0.693205  1.591431
```


#### 2. Pivot tables
```python
>>> df = pd.DataFrame(
...    {
...        "A": ["one", "one", "two", "three"] * 3,
...        "B": ["A", "B", "C"] * 4,
...        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
...        "D": np.random.randn(12),
...        "E": np.random.randn(12),
...    }
... )

>>> df
        A  B    C         D         E
0     one  A  foo -1.202872  0.047609
1     one  B  foo -1.814470 -0.136473
2     two  C  foo  1.018601 -0.561757
3   three  A  bar -0.595447 -1.623033
4     one  B  bar  1.395433  0.029399
5     one  C  bar -0.392670 -0.542108
6     two  A  foo  0.007207  0.282696
7   three  B  foo  1.928123 -0.087302
8     one  C  foo -0.055224 -1.575170
9     one  A  bar  2.395985  1.771208
10    two  B  bar  1.552825  0.816482
11  three  C  bar  0.166599  1.100230

>>> pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
C             bar       foo
A     B                    
one   A  2.395985 -1.202872
      B  1.395433 -1.814470
      C -0.392670 -0.055224
three A -0.595447       NaN
      B       NaN  1.928123
      C  0.166599       NaN
two   A       NaN  0.007207
      B  1.552825       NaN
      C       NaN  1.018601
```

### k. Time series
Pandas memiliki fungsionalitas yang sederhana, kuat, dan efesien untuk melakukan operasi resampling selama konversi frekuensi.

Berikut contoh penerapan *time series* pada pandas :
```python
>>> rng = pd.date_range("1/1/2012", periods=100, freq="S")

>>> ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

>>> ts.resample("5Min").sum()
 
2012-01-01    24182
Freq: 5T, dtype: int64
```

Menampilkan representasi zona waktu :
```python
>>> rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

>>> ts = pd.Series(np.random.randn(len(rng)), rng)

>>> ts 
2012-03-06    1.857704
2012-03-07   -1.193545
2012-03-08    0.677510
2012-03-09   -0.153931
2012-03-10    0.520091
Freq: D, dtype: float64

>>> ts_utc = ts.tz_localize("UTC")

>>> ts_utc
2012-03-06 00:00:00+00:00    1.857704
2012-03-07 00:00:00+00:00   -1.193545
2012-03-08 00:00:00+00:00    0.677510
2012-03-09 00:00:00+00:00   -0.153931
2012-03-10 00:00:00+00:00    0.520091
Freq: D, dtype: float64
```

Mengonversi waktu ke zona waktu lain :
```python
>>> ts_utc.tz_convert("US/Eastern")
2012-03-05 19:00:00-05:00    1.857704
2012-03-06 19:00:00-05:00   -1.193545
2012-03-07 19:00:00-05:00    0.677510
2012-03-08 19:00:00-05:00   -0.153931
2012-03-09 19:00:00-05:00    0.520091
Freq: D, dtype: float64
```

Mengonversi antara representasi rentang waktu :
```python 
>>> rng = pd.date_range("1/1/2012", periods=5, freq="M")

>>> ts = pd.Series(np.random.randn(len(rng)), index=rng)

>>> ts 
2012-01-31   -1.475051
2012-02-29    0.722570
2012-03-31   -0.322646
2012-04-30   -1.601631
2012-05-31    0.778033
Freq: M, dtype: float64

>>> ps = ts.to_period()

>>> ps 
2012-01   -1.475051
2012-02    0.722570
2012-03   -0.322646
2012-04   -1.601631
2012-05    0.778033
Freq: M, dtype: float64

>>> ps.to_timestamp() 
2012-01-01   -1.475051
2012-02-01    0.722570
2012-03-01   -0.322646
2012-04-01   -1.601631
2012-05-01    0.778033
Freq: MS, dtype: float64
```

Konversi antara periode dan stempel waktu memungkinkan beberapa fungsi aritmatika yang nyaman untuk digunakan. Contoh penggunaan :
```python
>>> prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")

>>> ts = pd.Series(np.random.randn(len(prng)), prng)

>>> ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9

>>> ts.head() 
1990-03-01 09:00   -0.289342
1990-06-01 09:00    0.233141
1990-09-01 09:00   -0.223540
1990-12-01 09:00    0.542054
1991-03-01 09:00   -0.688585
Freq: H, dtype: float64
```

### l. Categoricals
Pandas dapat melakukan penyertaan data melalui DataFram.
```python
>>> df = pd.DataFrame(
...    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", .... "a", "a", "e"]}
... )

```

Mengkonversikan *raw grade* menjadi type data kategorikal :
```python
>>> f["grade"] = df["raw_grade"].astype("category")

>>> df["grade"]
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): ['a', 'b', 'e']
```

Mengganti nama kategori menjadi nama yang lebih bermakna :
```python
>>> df["grade"].cat.categories = ["very good", "good", "very bad"]
>>> df["grade"] = df["grade"].cat.set_categories(
...    ["very bad", "bad", "medium", "good", "very good"]
... )

>>> df["grade"]
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (5, object): ['very bad', 'bad', 'medium', 'good', 'very good']
```

Penyortiran adalah mengurutkan value data dalam kategori dan bukan urutan yang leksikal :
```python
>>> df.sort_values(by="grade")
   id raw_grade      grade
5   6         e   very bad
1   2         b       good
2   3         b       good
0   1         a  very good
3   4         a  very good
4   5         a  very good
```

Pengelompokkan data menurut kolom kategoris yang juga menyertakan data yang termasuk kategori kosong :
```python
>>> df.groupby("grade").size()
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
```

### m. Plotting
Penggunaan API matplotlib dalam membuat sebuah plot merupakan konvensi standar yang dapat digunakan sebagai *reference* :
```python
>>> import matplotlib.pyplot as plt

>>> plt.close("all")

>>> ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

>>> ts = ts.cumsum()

>>> ts.plot();
```

Jika proses *code running* dilakukan melalui jupyter notebook, maka plot akan menyediakan perintah **.plot()**.

```python
>>> plt.show();
>>> df = pd.DataFrame(
...    np.random.randn(1000, 4), index=ts.index, columns=["A", .... "B", "C", "D"]
... )
...

>>> df = df.cumsum()

>>> plt.figure();

>>> df.plot();

>>> plt.legend(loc='best');
```

### n. Getting data in/out
#### 1. CVS
Menulis perintah yang dapat memanggil file csv :
```python
>>> df.to_csv("foo.csv")
```

Menulis perintah yang dapat membaca isi dari file csv yang berhasil dipanggil sebelumnya :
```python
>>> pd.read_csv("foo.csv")
     Unnamed: 0          A          B          C          D
0    2000-01-01   0.350262   0.843315   1.798556   0.782234
1    2000-01-02  -0.586873   0.034907   1.923792  -0.562651
2    2000-01-03  -1.245477  -0.963406   2.269575  -1.612566
3    2000-01-04  -0.252830  -0.498066   3.176886  -1.275581
4    2000-01-05  -1.044057   0.118042   2.768571   0.386039
..          ...        ...        ...        ...        ...
995  2002-09-22 -48.017654  31.474551  69.146374 -47.541670
996  2002-09-23 -47.207912  32.627390  68.505254 -48.828331
997  2002-09-24 -48.907133  31.990402  67.310924 -49.391051
998  2002-09-25 -50.146062  33.716770  67.717434 -49.037577
999  2002-09-26 -49.724318  33.479952  68.108014 -48.822030

[1000 rows x 5 columns]
```

#### 2. HDF5
Menulis perintah yang dapat digunakan untuk menulis dan membaca file dari HDF5stores :
```python
>>> df.to_hdf("foo.h5", "df")
 A          B          C          D
2000-01-01   0.350262   0.843315   1.798556   0.782234
2000-01-02  -0.586873   0.034907   1.923792  -0.562651
2000-01-03  -1.245477  -0.963406   2.269575  -1.612566
2000-01-04  -0.252830  -0.498066   3.176886  -1.275581
2000-01-05  -1.044057   0.118042   2.768571   0.386039
...               ...        ...        ...        ...
2002-09-22 -48.017654  31.474551  69.146374 -47.541670
2002-09-23 -47.207912  32.627390  68.505254 -48.828331
2002-09-24 -48.907133  31.990402  67.310924 -49.391051
2002-09-25 -50.146062  33.716770  67.717434 -49.037577
2002-09-26 -49.724318  33.479952  68.108014 -48.822030

[1000 rows x 4 columns]
```

#### 3. EXCEL 
Menulis perintah yang dapat digunakan untuk menulis dan membaca file excel :
```python
>>> pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])
    Unnamed: 0          A          B          C          D
0   2000-01-01   0.350262   0.843315   1.798556   0.782234
1   2000-01-02  -0.586873   0.034907   1.923792  -0.562651
2   2000-01-03  -1.245477  -0.963406   2.269575  -1.612566
3   2000-01-04  -0.252830  -0.498066   3.176886  -1.275581
4   2000-01-05  -1.044057   0.118042   2.768571   0.386039
..         ...        ...        ...        ...        ...
995 2002-09-22 -48.017654  31.474551  69.146374 -47.541670
996 2002-09-23 -47.207912  32.627390  68.505254 -48.828331
997 2002-09-24 -48.907133  31.990402  67.310924 -49.391051
998 2002-09-25 -50.146062  33.716770  67.717434 -49.037577
999 2002-09-26 -49.724318  33.479952  68.108014 -48.822030

[1000 rows x 5 columns]
```

### o. Gotchas 
Jika seorang pengembang mencoba untuk melakukan operasi, maka penampilan output yang dihasilkan bisa saja akan seperti ini :
```python
>>> if pd.Series([False, True, False]):
...    print("I was true")
Traceback
    ...
ValueError: The truth value of an array is ambiguous. Use a.empty, a.any() or a.all().
```

## D. Kesimpulan