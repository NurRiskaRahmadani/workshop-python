# PYTHON UNTUK MACHINE LEARNING (Pertemuan 14)
## A. Latar Belakang
Kecerdasan buatan (AI) merupakan simulasi dari kecerdasan yang dimiliki oleh manusia yang kemudian dimodelkan ke dalam mesin dan di program agar dapat berpikir seperti manusia. 

Dengan demikian AI dapat dikatakan sebagai sistem komputer yang bisa melakukan pekerjaan umum yang memerlukan tenaga/kecerdasan manusia dalam penyelesaiannya. 

AI sendiri memiliki banyak cabang ilmu, seperti *deep learning*, *natural language processing (NLP)*, *computer vision*, *machine learning*, dan masih banyak lagi. 

Saat ini, cabang Ai yang akan diulas adalah tentang *machine learning*. Tentang apa itu *machine learning*, bagaimana penggunaan dan penerapannya serta bagaimana implementasinya untuk menyelesaikan sebuah permasalahan. 

## B. Dasar Teori
*Machine learning*/Pembelajaran mesin merupakan mesin yang dikembangkan untuk dapat belajar mandiri tanpa memerlukan arahan dari penggunanya. *Machine learning* ini dikembangkan bersama disiplin ilmu lainnya, seperti statistika, matematika, dan *data mining* sehingga mesin dapat belajar dengan menganalisa data tanpa perlu melakukan program ulang dan tanpa diperintah. 

*Machine learning* memiliki kemampuan untuk memperoleh data yang ada dengan perintah yang dimilikinya sehingga dapat mempelajari sendiri data diperolehnya dan dapat menyelesaikan tugas tertentu. 

Istilah *machine learning* pertama kali diperkenalkan oleh beberapa ilmuwan matematika, yakni Adrien Marie Legendre, Thomas Bayes dan Andrey Markov di tahun 1920. Sejak itu *machine learning* terus dikembangkan hingga saat ini. Salah satu contoh penerapan *machine learning* adalah *deep blue* yang dibuat oleh IBM pada 1996. 

Secara umum, *machine learning* akan mempertimbangkan masalah pada suatu kasus lalu mempelajarinya sehingga kemudian dapat diprediksi sifat datanya. 

Pada *machine learning* terdapat beberapa teknik dasar belajar yang sering diterapkan, dua diantaranya ialah *supervised* dan *unsupervised*.

*Supervised learning* merupakan teknik yang dapat diterapkan pada *machine learning* yang bisa menerima informasi yang sudah ada pada data dengan memberikan label tertentu. Pada teknik ini,mesin diharapkan dapat memberikan target terhadap output dengan membandingkannya dengan data yang sudah diolah sebelumnya. Atribut tambahan yang digunakan pada teknik ini juga merupakan pelengkap untuk pemecahan masalah untuk masalah-masalah yang memerlukan proses klasifikasi ataupun regresi. 

*unsupervised learning* merupakan teknik yang dapat diterapkan pada *machine learning* yang dapat digunakan pada data yang tidak memiliki informasi yang tidak bisa diterapkan secara langsung. Pada teknik ini, mesin diharapkan dapat membantu menemukan struktur atau pola tersembunyi pada data yang tidak memiliki label. 

Perbedaan *supervised learning* dan *unsupervised learning* terletak pada data acuan yang ada, jika pada *supervised learning* terdapat data yang dapat dijadikan sebagai acuan pembelajaran, maka pada *unsupervised learning* tidak akan ditemukan data yang dapat dijadikan sebagai acuan pembelajaran atau dalam kata lain pada teknik ini mesin hanya akan melakukan proses sendiri tanpa perlu tahu model output seperti apa yang akan dihasilkan. 

*Machine learning* adalah tentang mempelajari suatu/beberapa properti dari kumpulan data dan kemudian di uji terhadap kumpulan data lainnya. Praktik umum pada *machine learning* adalah mengevaluasi algoritma masalah dengan membagi kumpulan data menjadi dua bagian yang disebut dengan *training test* dan *testing test*.  

## C. Machine Learning With Scikit-Learn
### 1. Loading an example dataset
Memulai *interpreter* Python melalui shell lalu memuat perintah untuk set data yakni, **iris** dan **digits** :
```python
$ python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
```

Dataset adalah objek menyerupai kamus yang menyimpan semua data dan beberapa metadata tentang data tersebut. Data tersebut tersimpan dalam **.data** yang merupakan anggota dalam bentuk array. Untuk mengakses data yang berada didalamnya, cukup jalankan beberapa perintah, contoh jalankan perintah **digits.data** untuk meminta akses ke fitur untuk melakukan klasifikasi sampel digit pada data,serta jalankan juga perintah **digits.target** untuk memberikan kebenaran dasar untuk kumpulan data digit :
```python
>>> print(digits.data)
[[ 0.  0.  5. ...  0.  0.  0.]
 [ 0.  0.  0. ... 10.  0.  0.]
 [ 0.  0.  0. ... 16.  9.  0.]
 ...
 [ 0.  0.  1. ...  6.  0.  0.]
 [ 0.  0.  2. ... 12.  0.  0.]
 [ 0.  0. 10. ... 12.  1.  0.]]
 >>> digits.target
array([0, 1, 2, ..., 8, 9, 8])
```

Bentuk array data selalu berupa larik 2D, walaupun pada awalnya mempunyai bentuk asli yang berbeda. Pada akhirnya bentuk data yang disimpan adalah array. 
```python
>>> digits.images[0]
array([[ 0.,  0.,  5., 13.,  9.,  1.,  0.,  0.],
       [ 0.,  0., 13., 15., 10., 15.,  5.,  0.],
       [ 0.,  3., 15.,  2.,  0., 11.,  8.,  0.],
       [ 0.,  4., 12.,  0.,  0.,  8.,  8.,  0.],
       [ 0.,  5.,  8.,  0.,  0.,  9.,  8.,  0.],
       [ 0.,  4., 11.,  0.,  1., 12.,  7.,  0.],
       [ 0.,  2., 14.,  5., 10., 12.,  0.,  0.],
       [ 0.,  0.,  6., 13., 10.,  0.,  0.,  0.]])
```

### 2. Learning and predicting
Pada kasus ini, kumpulan data digit bertuga untuk memprediksi data melalui gambar sehingga didapat digit yang dapat mewakili data. Dalam scikit-learn, estimator untuk klasifikasi adalah objek Python yang mengimplementasikan metode serta perintah **.fit(X, y) predict(T)**. Berikut ini contoh implementasinya :
```python
>>> from sklearn import svm
>>> clf = svm.SVC(gamma=0.001, C=100.)
```

*Instance estimator* ini akan dipasang kedalam model agar dapat meneruskan proses set *training*. Set ini dipilih karena dapat menghasilkan array baru yang berisi semua item terakhir dari **digits.data** :
```python
>>> clf.fit(digits.data[:-1], digits.target[:-1])
SVC(C=100.0, gamma=0.001)
```

Setelah nilai didapat, maka tahap selanjutnya yang dilakukan adalah memprediksi nilai baru pada data tersebut. 
```python
>>> clf.predict(digits.data[-1:])
array([8])
```

### 3. Conventions
Scikit-learn estimator mengikuti aturan tertentu untuk membuat perilaku mereka lebih prediktif. 
#### a. Type casting
```python
>>> import numpy as np
>>> from sklearn import kernel_approximation
>>> rng = np.random.RandomState(0)
>>> X = rng.rand(10, 2000)
>>> X = np.array(X, dtype='float32')
>>> X.dtype
dtype('float32')
>>>
>>> transformer = kernel_approximation.RBFSampler()
>>> X_new = transformer.fit_transform(X)
>>> X_new.dtype
dtype('float64')
```

Pada contoh diatas, **X** adalah **float32** yang dilemparkan oleh ***float64*** melalui **fit_transform(X)**. Target regresi yang diberikan oleh **float64** dan target klasifikasi dipertahankan :
```python
>>> from sklearn import datasets
>>> from sklearn.svm import SVC
>>> iris = datasets.load_iris()
>>> clf = SVC()
>>> clf.fit(iris.data, iris.target)
SVC()
>>> list(clf.predict(iris.data[:3]))
[0, 0, 0]
>>> clf.fit(iris.data, iris.target_names[iris.target])
SVC()
>>> list(clf.predict(iris.data[:3]))
['setosa', 'setosa', 'setosa']
```

Dapat dilihat pada contoh diatas, tugas dari perintah **predict()** adalah mengembalikan nilai array integer, hal ini terjadi karena **iris.target** (array integer) digunakan berada didalam **.fit()**. Sedangkan **.predict()** kedua akan mengulang string array, karena fungsi dari **iris.target_names** adalah untuk pemasangan. 

#### b. Refitting and updating parameters
Hyper-parameter estimator dapat diperbaharui setelah selesai di *build* melalui metode **set_params()**. parameter tadi akan dipanggil melalui perintah **fit()** dan akan dipanggil lebih dari sekali sehingga akan menimpa perintah **fit()** sebelumnya. 
```python
>>> import numpy as np
>>> from sklearn.datasets import load_iris
>>> from sklearn.svm import SVC
>>> X, y = load_iris(return_X_y=True)
>>> clf = SVC()
>>> clf.set_params(kernel='linear').fit(X,y)
SVC(kernel='linear')
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])
>>> clf.set_params(kernel='rbf').fit(X,y)
SVC()
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])
```

#### c. Multiclass vs multilabel fitting
Ketika menggunakan **multiclass classifiers**, tugas *learning* dan *predicting* akan bergantung pada format data target yang sesuai. Contoh penerapan :
```python
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer
>>>
>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]
>>>
>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0)
... )
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])
```

Pada contoh diatas, dapat dilihat bahwa pengklasifikasian cocok digunakan pada larik 1d dari label *multiclass* dan oleh **predict()**, karena itu metode yang digunakan ini menyediakan prediksi multikelas yang sesuai. Sehingga dimungkinkan untuk menyesuaikan juga pada array 2d indikator label biner. 
```python
>>> y = LabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 0],
       [0, 0, 0]])
```

Pada contoh program diatas dapat dilihat bahwa, pengklasifikasian berada di **fit()** pada representasi label biner 2d dari **y** menggunakan **LabelBinarizer**. Dengan output multilabel, sebuah *instance* juga dapat diberi beberapa label, contohnya :
```python
>>> from sklearn.preprocessing import MultiLabelBinarizer
>>> y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
>>> y = MultiLabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 1, 0, 0]])
```

## D. Kesimpulan
*Machine learning*/Pembelajaran mesin merupakan mesin yang dikembangkan untuk dapat belajar mandiri tanpa memerlukan arahan dari penggunanya. *Machine learning* ini dikembangkan bersama disiplin ilmu lainnya, seperti statistika, matematika, dan *data mining* sehingga mesin dapat belajar dengan menganalisa data tanpa perlu melakukan program ulang dan tanpa diperintah. 

*Machine learning* memiliki kemampuan untuk memperoleh data yang ada dengan perintah yang dimilikinya sehingga dapat mempelajari sendiri data diperolehnya dan dapat menyelesaikan tugas tertentu.