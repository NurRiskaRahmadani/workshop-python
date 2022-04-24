# Virtual Environments and Package Manager (Modul 12) 
## A. Latar Belakang
Virtual environment adalah sebuah ruang lingkup virtual yang terisolasi dari dependencies utama yang sangat berguna ketika user atau pengguna membutuhkaan dependencies yang berbeda-beda antara *project* satu dengan lainnya yang berjalan pada satu system operasi yang sama. 

Virtual environment pada Python memungkinkan seorang pengguna ataupun pengembang untuk membuat system Python yang berbeda dengan Python yang sudah ada di sistem, virtual Python ini mempunyai versi yang berbeda dengan Python di system, begitu juga dengan modul-modulnya. 

Berdasarkan uraian diatas, maka akan dibuat sebuah ringkasan mengenai apa itu virtual environment Python, bagaimana cara menggunakan, implementasi dan menjalankannya melalui conda (Distributor bahasa pemrograman pada Python dan R untuk komputasi ilmiah yang bertujuan untuk menyederhanakan manajemen dan penerapan paket).

## B. Dasar Teori
Aplikasi Python seringkali menggunakan paket ataupun modul yang bukan berasal dari *library standard* nya sendiri. Sedangkan sebuah aplikasi terkadang memerlukan versi perpustakaan tertentu, karena harus memperbaiki bug tertentu atau harus ditulis menggunakan versi interface yang tidak sesuai/tidak memenuhi standar aplikasi tersebut.

Walaupun begitu, bukan berarti satu instalasi Python harus dapat memenuhi setiap standar/persyaratan dari setiap aplikasi yang ada. Contoh, jika aplikasi A membutuhkan versi 1.0 dari modul tertentu pada Python tetapi aplikasi B malah membutuhkan versi 2.0, maka tentu saja persyaratan untuk kedua aplikasi ini akan berbeda dan saling bertentangan sehingga dapat menyebabkan beberapa masalah salah satunya aplikasi tidak dapat dijalankan/digunakan.

Untuk itu, Python menyediakan sebuah alternatif berupa *Virtual environment*/lingkungan virtual yang berisi instalasi Python untuk versi Python tertentu dengan tambahan sejumlah *package* tambahan.

Seperti yang kita ketahui berdasarkan paparan diatas, dapat ditarik kesimpulan bahwa *virtual environment* merupakan teknik yang dapat membantu seorang pengembang dalam mengembangkan programnya menggunakan Python.

Salah satu *tools* yang kerap kali digunakan oleh seorang pengembang dalam membuat *virtual environment* nya adalah Anaconda.

Anaconda merupakan paket *Integrated Development Environment* (IDE) berbasis Python yang sangat membantu seorang pengembang dalam menggunakan bahasa Python.

Secara harfiah, Anaconda adalah distributor bahasa pemrograman Python dan R untuk komputasi ilmiah seperti *data science*, *machine learning*, pemrosesan data berskala besar, analisis deskriptif dan lain sebagainya yang bertujuan untuk menyederhanakan manajemen dan penerapan paket. 

## C. Virtual Environment
### 1. Creating/Membuat Virtual Environment
Modul yang digunakan untuk membuat dan mengelola *virtual environment* pada Python dikenal dengan sebutan **venv**. **venv** biasanya akan melakukan instalasi sendiri versi Python yang dimiliki pengembang. 

Berikut ini merupakan contoh implementasi pembuatan *virtual environment* dengan menjalankan modul **venv** sebagai *script* melalui directori :

```
python -m venv tutorial-env
```

Agar *virtual environment* dapat diakses cukup dengan menjalankan perintah berikut ini :

```
tutorial-env\Scripts\activate.bat
```

Mengaktifkan *virtual environment* akan mengubah *prompt shell* yang digunakan sebelumnya dengan menunjukkan *virtual enviroment* yang berhasil dibuat sebelumnya. 

```
C:\Windows\system32>tutorial-env\Scripts\activate.bat

(tutorial-env) C:\Windows\system32>python
Python 3.11.0a7 (main, Apr  5 2022, 21:27:39) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_3.11.167.0_x64__qbz5n2kfra8p0\\python311.zip', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_3.11.167.0_x64__qbz5n2kfra8p0\\Lib', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_3.11.167.0_x64__qbz5n2kfra8p0\\DLLs', 'C:\\Windows\\system32\\tutorial-env', 'C:\\Windows\\system32\\tutorial-env\\Lib\\site-packages']
>>> exit()
```

Adapun untuk menonaktifkan *virtual environment* yang digunakan, dapat dilakukan dengan menginputkan perintah berikut ini ke terminal/shell :

```
deactive
```


### 2. Managing/Manajemen Paket Dengan PIP
Dengan Python seorang pengembang dapat menginstal, meng-*upgrade*, dan memindahkan *package* yang digunakan dengan memanggilnya melalui perintah **pip**. Perintah **pip** secara default akan menginstall *package* dari *Python Package Index*.

Perintah **pip** memiliki beberapa sub-perintah seperti **install**, **uninstall**, **freeze** dll. 

Untuk menginstal sebuah paket dengan versi terbaru dengan menentukan nama *package* dapat dilakukan seperti contoh berikut ini :

```
(tutorial-env) C:\Windows\system32>python -m pip install Beautifulsoup4
Collecting Beautifulsoup4
  Downloading beautifulsoup4-4.11.1-py3-none-any.whl (128 kB)
     --------------------------------------- 128.2/128.2 KB 117.9 kB/s eta 0:00:00
Collecting soupsieve>1.2
  Downloading soupsieve-2.3.2.post1-py3-none-any.whl (37 kB)
Installing collected packages: soupsieve, Beautifulsoup4
Successfully installed Beautifulsoup4-4.11.1 soupsieve-2.3.2.post1
```

Atau bisa juga dengan memberi nama *package* yang diikuti oleh tanda == beserta nomor versinya, seperti contoh berikut ini :

```
(tutorial-env) C:\Windows\system32>python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Downloading requests-2.6.0-py2.py3-none-any.whl (469 kB)
     --------------------------------------- 469.8/469.8 KB 201.5 kB/s eta 0:00:00
Installing collected packages: requests
Successfully installed requests-2.6.0
```

Jika perintah sebelumnya hendak dijalankan kembali, maka **pip** akan melihat bahwa versi yang diminta sudah terinstal sehingga perintah penginstalan tidak akan dijalankan kembali. Adapun jika ingin meng-*update* versi yang digunakan dapat dilakukan dengan menjalankan perintah **python -m pip install --upgrade** seperti yang tampak pada contoh implementasi dibawah ini :

```
(tutorial-env) C:\Windows\system32>python -m pip install --upgrade requests
Requirement already satisfied: requests in c:\windows\system32\tutorial-env\lib\site-packages (2.6.0)
Collecting requests
  Using cached requests-2.27.1-py2.py3-none-any.whl (63 kB)
Requirement already satisfied: idna<4,>=2.5 in c:\windows\system32\tutorial-env\lib\site-packages (from requests) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\windows\system32\tutorial-env\lib\site-packages (from requests) (2.0.12)
Requirement already satisfied: certifi>=2017.4.17 in c:\windows\system32\tutorial-env\lib\site-packages (from requests) (2021.10.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\windows\system32\tutorial-env\lib\site-packages (from requests) (1.26.9)
Installing collected packages: requests
  Attempting uninstall: requests
    Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.27.1
```

Perintah diatas akan diikuti perintah **python -m pip uninstall** yang diperuntukkan untuk menghapus *package* dari *virtual environment* yang dibuat. Sedangkan untuk menampilkan informasi dari *package* tertentu pada *library* dapat dilakukan dengan menjalankan beberapa perintah, seperti perintah yang diterapkan pada program dibawah ini : 

```
(tutorial-env) C:\Windows\system32>python -m pip show requests
Name: requests
Version: 2.27.1
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: c:\windows\system32\tutorial-env\lib\site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by:
```

Menjalankan perintah **python -m pip list** untuk menampilkan semua *package* yang diinstal di *virtual environment*. 

```
(tutorial-env) C:\Windows\system32>python -m pip list
Package            Version
------------------ -----------
beautifulsoup4     4.11.1
certifi            2021.10.8
charset-normalizer 2.0.12
idna               3.3
pip                22.0.4
requests           2.27.1
setuptools         58.1.0
soupsieve          2.3.2.post1
urllib3            1.26.9
```

Menjalankan kembali perintah untuk menampilkan daftar paket yang diinstal namun dengan output menggunakan format yang berbeda. 

```
(tutorial-env) C:\Windows\system32>python -m pip freeze > requirements.txt

(tutorial-env) C:\Windows\system32>requirements.txt
```

Ketika perintah requirements.txt dijalankan, maka prompt shell akan membuka file tersebut dan menampilkan isinnya.

Adapun untuk melakukan commit pada file requirements.txt dapat dilakukan dengan menginstall perintah **install -r**, seperti pada contoh implementasi dibawah ini. 

```
(tutorial-env) C:\Windows\system32>python -m pip install -r requirements.txt
Requirement already satisfied: beautifulsoup4==4.11.1 in c:\windows\system32\tutorial-env\lib\site-packages (from -r requirements.txt (line 1)) (4.11.1)
Requirement already satisfied: certifi==2021.10.8 in c:\windows\system32\tutorial-env\lib\site-packages (from -r requirements.txt (line 2)) (2021.10.8)
Requirement already satisfied: charset-normalizer==2.0.12 in c:\windows\system32\tutorial-env\lib\site-packages (from -r requirements.txt (line 3)) (2.0.12)
Requirement already satisfied: idna==3.3 in c:\windows\system32\tutorial-env\lib\site-packages (from -r requirements.txt (line 4)) (3.3)
Requirement already satisfied: requests==2.27.1 in c:\windows\system32\tutorial-env\lib\site-packages (from -r requirements.txt (line 5)) (2.27.1)
Requirement already satisfied: soupsieve==2.3.2.post1 in c:\windows\system32\tutorial-env\lib\site-packages (from -r requirements.txt (line 6)) (2.3.2.post1)
Requirement already satisfied: urllib3==1.26.9 in c:\windows\system32\tutorial-env\lib\site-packages (from -r requirements.txt (line 7)) (1.26.9)
```
## D. Conda Practices
Membuat *package manager* dan *virtual enviroment* dengan conda menggunakan *command line* miliki Anaconda prompt untuk Windows. Referensi ([Your Link](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)).

1. Menginstal Anaconda di komputer lokal
2. Konfigurasi Anaconda
3. Membuka Anaconda Prompt dari komputer lokal
4. Managing Conda 
Untuk membuktikan bahwa conda berhasil diinstal dan dapat berjalan pada sistem komputer lokal, hal yang dapat dilakukan adalah dengan menjalankan perintah **conda --version**

input :
```
(base) C:\Users\Riska>conda --version
```

output :
```
conda 4.10.3
```

> Jika mendapatkan *error message* saat perintah dijalankan, pastikan bahwa jendela terminal untuk instalasi telah ditutup sebelumnya. Sehingga perintah pengecekan dapat dijalankan dengan membuka jendela terminal yang baru 


Melakukan peng-update an conda menjadi versi terbaru, dapat dilakukan dengan menjalankan perintah **conda update conda**

input :
```
(base) C:\Users\Riska>conda update conda
```

output :
```
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\Riska\anaconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-4.12.0               |   py39haa95532_0        14.5 MB
    conda-package-handling-1.8.1|   py39h8cc25b3_0         729 KB
    ------------------------------------------------------------
                                           Total:        15.2 MB

The following packages will be UPDATED:

  conda                               4.10.3-py39haa95532_0 --> 4.12.0-py39haa95532_0
  conda-package-han~                   1.7.3-py39h8cc25b3_1 --> 1.8.1-py39h8cc25b3_0

Proceed ([y]/n)?
```

Program yang berjalan akan membandingkan versi conda yang digunakan dengan yang akan di update, lalu menampilkan versi yang tersedia untuk diinstal, jika versi terbaru tersedia maka cukup dengan mengetikan y untuk memperbaharuinya. :

output lanjutan :
```
Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-package-handli | 729 KB    | ####################################### | 100%
conda-4.12.0         | 14.5 MB   | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```


5. Managing Environments
Conda memungkinkan penggunanya untuk membuat *environment* terpisah yang berisi file, paket serta dependensi yang tidak dapat berinteraksi dengan *environment* lain. 

Saat mulai menggunakan conda, maka *environment* yang akan menjadi default-nya akan diberi nama *base*. Agar program yang dibuat tidak masuk ke *environment* dasar maka diperlukan untuk membuat *environment* terpisah yang dinamai *virtual environment*. 

* Membuat *environment* baru dan menginstal paket di dalamnya

input :
```
(base) C:\Users\Riska>conda create --name condaPractice biopython
```

output :
```
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\Riska\anaconda3\envs\condaPractice

  added / updated specs:
    - biopython


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    biopython-1.78             |   py39h2bbff1b_0         2.1 MB
    ca-certificates-2022.3.29  |       haa95532_1         122 KB
    certifi-2021.10.8          |   py39haa95532_2         152 KB
    numpy-1.21.5               |   py39h7a0a035_1          25 KB
    numpy-base-1.21.5          |   py39hca35cd5_1         4.4 MB
    openssl-1.1.1n             |       h2bbff1b_0         4.8 MB
    python-3.9.12              |       h6244533_0        17.1 MB
    setuptools-61.2.0          |   py39haa95532_0         1.0 MB
    six-1.16.0                 |     pyhd3eb1b0_1          18 KB
    sqlite-3.38.2              |       h2bbff1b_0         807 KB
    tzdata-2022a               |       hda174b7_0         109 KB
    wheel-0.37.1               |     pyhd3eb1b0_0          33 KB
    ------------------------------------------------------------
                                           Total:        30.7 MB

The following NEW packages will be INSTALLED:

  biopython          pkgs/main/win-64::biopython-1.78-py39h2bbff1b_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_1
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  numpy              pkgs/main/win-64::numpy-1.21.5-py39h7a0a035_1
  numpy-base         pkgs/main/win-64::numpy-base-1.21.5-py39hca35cd5_1
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
six-1.16.0           | 18 KB     | ####################################### | 100%
sqlite-3.38.2        | 807 KB    | ####################################### | 100%
biopython-1.78       | 2.1 MB    | ####################################### | 100%
ca-certificates-2022 | 122 KB    | ####################################### | 100%
setuptools-61.2.0    | 1.0 MB    | ####################################### | 100%
python-3.9.12        | 17.1 MB   | ####################################### | 100%
numpy-base-1.21.5    | 4.4 MB    | ####################################### | 100%
numpy-1.21.5         | 25 KB     | ####################################### | 100%
tzdata-2022a         | 109 KB    | ####################################### | 100%
certifi-2021.10.8    | 152 KB    | ####################################### | 100%
wheel-0.37.1         | 33 KB     | ####################################### | 100%
openssl-1.1.1n       | 4.8 MB    | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate condaPractice
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```

* Mengaktifkan *environment* baru 
Perintah yang diinputkan :
```
(base) C:\Users\Riska>conda activate condaPractice
```

Jika *environment* berhasil diaktifkan, maka tampilan jendela terminal akan seperti ini :
```
(condaPractice) C:\Users\Riska>
```

* Melihat daftar pada *environment* yang dibuat
input :
```
conda info --envs
```

output :
```
# conda environments:
#
base                  *  C:\Users\Riska\anaconda3
condaPractice            C:\Users\Riska\anaconda3\envs\condaPractice
```

> *Environment* yang aktif akan ditandai dengan tanda (*)

* Mengubah kembali *environment* yang digunakan dengan menjalankan perintah **conda activate**


6. Managing Python
Ketika sebuah *environment* baru dibuat, conda akan secara otomatis menginstal versi Python yang sama dengan versi yang digunakan ketika mengunduh/menginstal Anaconda. Walaupun begitu, pembuatan *environment* baru dengan versi Python tetap bisa dilakukan dengan membuat dan menentukan sendiri versi yang diinginkan. 

Berikut ini contoh implementasi pembuatan *Environment* baru dengan versi Python yang berbeda dengan versi default yang dimiliki :

* Membuat *environment* baru dengan nama "snake" yang berisi versi 3.9

input :
```
(base) C:\Users\Riska>conda create --name snakes python=3.9
```

output :
```
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\Riska\anaconda3\envs\snakes

  added / updated specs:
    - python=3.9


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_1
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

* Mengaktifkan *environment*

input :
```
(base) C:\Users\Riska>conda activate snakes
```

output :
```
(snakes) C:\Users\Riska>python
Python 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Users\\Riska\\anaconda3\\envs\\snakes\\python39.zip', 'C:\\Users\\Riska\\anaconda3\\envs\\snakes\\DLLs', 'C:\\Users\\Riska\\anaconda3\\envs\\snakes\\lib', 'C:\\Users\\Riska\\anaconda3\\envs\\snakes', 'C:\\Users\\Riska\\anaconda3\\envs\\snakes\\lib\\site-packages']
>>> exit()
```


* Melakukan verifikasi untuk mengetahui bahwa *snake environment* telah ditambahkan dan aktif

input :
```
(snakes) C:\Users\Riska>conda info --envs
```

output :
```
# conda environments:
#
base                     C:\Users\Riska\anaconda3
condaPractice            C:\Users\Riska\anaconda3\envs\condaPractice
snakes                *  C:\Users\Riska\anaconda3\envs\snakes
```

* Melakukan verifikasi terhadap versi Python yang digunakan pada *environment* saat ini

input :
```
(snakes) C:\Users\Riska>python --version
```

output :
```
Python 3.9.12
```

* Menonaktifkan *snake environment* dan kembali menggunakan *base environment* 

input :
```
(snakes) C:\Users\Riska>conda activate
```

output :
```
(base) C:\Users\Riska>
```

7. Managing Package
Melakukan pemeriksaan paket untuk paket yang telah diinstal serta memeriksa paket yang telah tersedia sehingga dapat diinstal. 

* Menemukan paket yang telah terinstal lalu mengaktifkan *environment* yang akan digunakan. 

input :
```
(base) C:\Users\Riska>conda activate snakes
```

output :
```
(snakes) C:\Users\Riska>
```

* Memeriksa apakah paket **beautifulsoup4** telah terinstal dan tersedia di repositori Anaconda

input :
```
(snakes) C:\Users\Riska>conda search beautifulsoup4
```

output :
```
Loading channels: done
# Name                       Version           Build  Channel
beautifulsoup4                 4.6.0          py27_1  pkgs/main
beautifulsoup4                 4.6.0  py27hc287451_1  pkgs/main
beautifulsoup4                 4.6.0          py35_1  pkgs/main
beautifulsoup4                 4.6.0  py35h61fcdcc_1  pkgs/main
beautifulsoup4                 4.6.0          py36_1  pkgs/main
beautifulsoup4                 4.6.0  py36hd4cc5e8_1  pkgs/main
beautifulsoup4                 4.6.0          py37_1  pkgs/main
beautifulsoup4                 4.6.1          py27_0  pkgs/main
beautifulsoup4                 4.6.1          py35_0  pkgs/main
beautifulsoup4                 4.6.1          py36_0  pkgs/main
beautifulsoup4                 4.6.1          py37_0  pkgs/main
beautifulsoup4                 4.6.3          py27_0  pkgs/main
beautifulsoup4                 4.6.3          py35_0  pkgs/main
beautifulsoup4                 4.6.3          py36_0  pkgs/main
beautifulsoup4                 4.6.3          py37_0  pkgs/main
beautifulsoup4                 4.7.1          py27_1  pkgs/main
beautifulsoup4                 4.7.1          py36_1  pkgs/main
beautifulsoup4                 4.7.1          py37_1  pkgs/main
beautifulsoup4                 4.8.0          py27_0  pkgs/main
beautifulsoup4                 4.8.0          py36_0  pkgs/main
beautifulsoup4                 4.8.0          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py27_0  pkgs/main
beautifulsoup4                 4.8.1          py36_0  pkgs/main
beautifulsoup4                 4.8.1          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py38_0  pkgs/main
beautifulsoup4                 4.8.2          py27_0  pkgs/main
beautifulsoup4                 4.8.2          py36_0  pkgs/main
beautifulsoup4                 4.8.2          py37_0  pkgs/main
beautifulsoup4                 4.8.2          py38_0  pkgs/main
beautifulsoup4                 4.9.0          py36_0  pkgs/main
beautifulsoup4                 4.9.0          py37_0  pkgs/main
beautifulsoup4                 4.9.0          py38_0  pkgs/main
beautifulsoup4                 4.9.1          py36_0  pkgs/main
beautifulsoup4                 4.9.1  py36haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py37_0  pkgs/main
beautifulsoup4                 4.9.1  py37haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py38_0  pkgs/main
beautifulsoup4                 4.9.1  py38haa95532_0  pkgs/main
beautifulsoup4                 4.9.1  py39haa95532_0  pkgs/main
beautifulsoup4                 4.9.3    pyha847dfd_0  pkgs/main
beautifulsoup4                 4.9.3    pyhb0f4dca_0  pkgs/main
beautifulsoup4                4.10.0    pyh06a4308_0  pkgs/main
beautifulsoup4                4.11.1 py310haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py37haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py38haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py39haa95532_0  pkgs/main
```

* Menginstal paket untuk *environment* yang digunakan saat ini :

input :
```
(snakes) C:\Users\Riska>conda install beautifulsoup4
```

output:
```
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\Riska\anaconda3\envs\snakes

  added / updated specs:
    - beautifulsoup4


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    beautifulsoup4-4.11.1      |   py39haa95532_0         190 KB
    soupsieve-2.3.1            |     pyhd3eb1b0_0          34 KB
    ------------------------------------------------------------
                                           Total:         224 KB

The following NEW packages will be INSTALLED:

  beautifulsoup4     pkgs/main/win-64::beautifulsoup4-4.11.1-py39haa95532_0
  soupsieve          pkgs/main/noarch::soupsieve-2.3.1-pyhd3eb1b0_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
beautifulsoup4-4.11. | 190 KB    | ####################################### | 100%
soupsieve-2.3.1      | 34 KB     | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

* Memeriksa apakah paket yang diinstal telah ada di *environment* saat ini

input:
```
(snakes) C:\Users\Riska>conda list
```

output :
```
# packages in environment at C:\Users\Riska\anaconda3\envs\snakes:
#
# Name                    Version                   Build  Channel
beautifulsoup4            4.11.1           py39haa95532_0
ca-certificates           2022.3.29            haa95532_1
certifi                   2021.10.8        py39haa95532_2
openssl                   1.1.1n               h2bbff1b_0
pip                       21.2.4           py39haa95532_0
python                    3.9.12               h6244533_0
setuptools                61.2.0           py39haa95532_0
soupsieve                 2.3.1              pyhd3eb1b0_0
sqlite                    3.38.2               h2bbff1b_0
tzdata                    2022a                hda174b7_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
wheel                     0.37.1             pyhd3eb1b0_0
wincertstore              0.2              py39haa95532_2
```


## E. Kesimpulan
*Virtual environment* adalah sebuah wadah yang dapat membantu  seorang pengembang untuk membuat *environment* baru yang berisi ragam modul serta pustakanya agar pekerjaan yang dibuat dapat terisolasi dalam satu tempat. 

*Virtual environment* juga dapat disebut sebagai ruang lingkup virtual yang terisolasi dan sangat berguna ketika dependencies yang berbeda-beda antara project satu dengan yang lainnya berjalan dalam satu system operasi yang sama dibutuhkan. 

Python juga memiliki hal serupa, yang diberi nama **virtualenv**.

Seperti namanya, virtualenv dapat diartikan sebagai sebuah tools untuk membuat suatu *virtual environment untuk suatu project Python yang terisolasi dari project lainya. 