# JUPYTER (Pertemuan 12)
## A. Dasar Teori
JupyterLab adalah sebuah *environment*/lingkungan pengembangan interaktif berbasis web terbaru untuk *notebook*, *code*, dan data. Interface milik JupyterLab ini bersifat fleksibel sehingga memungkinkan penggunanya untuk mengonfigurasikan serta mengatur alur kerja dalam *data science*, komputasi ilmiah, jurnalisme komputasi dan *machine learning*. JupyterLab juga dirancang dengan desain modular yang mengundang ekstensi untuk memperluas dan memperkaya fungsionalitasnya. 

## B. Jupyter
### a. Instalasi Jupyter
1. JupyterLab
Instalasi JupyterLab menggunakan perintah pip :
```
(base) C:\Users\Riska>pip install jupyterlab
```

Menjalankan JupyterLab :
```
(base) C:\Users\Riska>jupyter-lab
```

Tampilan output ketika JupyterLab dijalankan :
```
[I 2022-05-24 08:28:46.584 ServerApp] jupyterlab | extension was successfully linked.
[I 2022-05-24 08:28:46.709 ServerApp] Writing notebook server cookie secret to C:\Users\Riska\AppData\Roaming\jupyter\runtime\jupyter_cookie_secret
[W 2022-05-24 08:28:46.975 ServerApp] The 'min_open_files_limit' trait of a ServerApp instance expected an int, not the NoneType None.
[I 2022-05-24 08:28:48.678 LabApp] JupyterLab extension loaded from C:\Users\Riska\anaconda3\lib\site-packages\jupyterlab
[I 2022-05-24 08:28:48.678 LabApp] JupyterLab application directory is C:\Users\Riska\anaconda3\share\jupyter\lab
[I 2022-05-24 08:28:48.709 ServerApp] jupyterlab | extension was successfully loaded.
[I 2022-05-24 08:29:00.431 ServerApp] nbclassic | extension was successfully loaded.
[I 2022-05-24 08:29:00.431 ServerApp] Serving notebooks from local directory: C:\Users\Riska
[I 2022-05-24 08:29:00.431 ServerApp] Jupyter Server 1.4.1 is running at:
[I 2022-05-24 08:29:00.431 ServerApp] http://localhost:8888/lab?token=38411926f5ccc54425539a2c47659c3040c2615c40713ead
[I 2022-05-24 08:29:00.431 ServerApp]  or http://127.0.0.1:8888/lab?token=38411926f5ccc54425539a2c47659c3040c2615c40713ead
[I 2022-05-24 08:29:00.431 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2022-05-24 08:29:00.697 ServerApp]

    To access the server, open this file in a browser:
        file:///C:/Users/Riska/AppData/Roaming/jupyter/runtime/jpserver-3084-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/lab?token=38411926f5ccc54425539a2c47659c3040c2615c40713ead
     or http://127.0.0.1:8888/lab?token=38411926f5ccc54425539a2c47659c3040c2615c40713ead
[E 2022-05-24 08:29:26.777 ServerApp] Uncaught exception GET /lab/api/settings/@jupyterlab/shortcuts-extension:shortcuts?1653355766075 (::1)
    HTTPServerRequest(protocol='http', host='localhost:8888', method='GET', uri='/lab/api/settings/@jupyterlab/shortcuts-extension:shortcuts?1653355766075', version='HTTP/1.1', remote_ip='::1')
    Traceback (most recent call last):
      File "C:\Users\Riska\anaconda3\lib\site-packages\tornado\web.py", line 1704, in _execute
        result = await result
    tornado.iostream.StreamClosedError: Stream is closed
[E 2022-05-24 08:29:41.345 ServerApp] Uncaught exception GET /lab/api/settings/@jupyterlab/docmanager-extension:plugin?1653355766080 (::1)
    HTTPServerRequest(protocol='http', host='localhost:8888', method='GET', uri='/lab/api/settings/@jupyterlab/docmanager-extension:plugin?1653355766080', version='HTTP/1.1', remote_ip='::1')
    Traceback (most recent call last):
      File "C:\Users\Riska\anaconda3\lib\site-packages\tornado\web.py", line 1704, in _execute
        result = await result
    tornado.iostream.StreamClosedError: Stream is closed
[I 2022-05-24 08:29:41.388 LabApp] Build is up to date
[I 2022-05-24 08:29:50.765 LabApp] Build is up to date
```

2. Jupyter Notebook
Instalasi Jupyter Notebook tipe klasik dengan perintah pip :
```
(base) C:\Users\Riska>pip install notebook
```

Menjalankan Jupyter Notebook :
```
(base) C:\Users\Riska>jupyter notebook
```

Tampilan output ketika Jupyter Notebook dijalankan :
```
[I 2022-05-24 08:34:22.406 LabApp] JupyterLab extension loaded from C:\Users\Riska\anaconda3\lib\site-packages\jupyterlab
[I 2022-05-24 08:34:22.407 LabApp] JupyterLab application directory is C:\Users\Riska\anaconda3\share\jupyter\lab
[I 08:34:24.678 NotebookApp] Serving notebooks from local directory: C:\Users\Riska
[I 08:34:24.678 NotebookApp] Jupyter Notebook 6.4.5 is running at:
[I 08:34:24.678 NotebookApp] http://localhost:8888/?token=18b4f1ce6844755562a519fb588fcc8473ce79500cb41b9c
[I 08:34:24.678 NotebookApp]  or http://127.0.0.1:8888/?token=18b4f1ce6844755562a519fb588fcc8473ce79500cb41b9c
[I 08:34:24.678 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 08:34:24.990 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///C:/Users/Riska/AppData/Roaming/jupyter/runtime/nbserver-5164-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=18b4f1ce6844755562a519fb588fcc8473ce79500cb41b9c
     or http://127.0.0.1:8888/?token=18b4f1ce6844755562a519fb588fcc8473ce79500cb41b9c
[I 08:34:43.297 NotebookApp] Creating new notebook in
[I 08:35:35.040 NotebookApp] Creating new notebook in
[I 08:35:49.727 NotebookApp] Kernel started: 67dd12b1-9d55-4ec4-b9ab-eeca9e668b71, name: python3
[I 08:37:53.600 NotebookApp] Saving file at /Workshop-Python.ipynb
```
3. Voila
Melakukan instalasi modul voila menggunakan perintah pip :
```
(base) C:\Users\Riska>pip install voila
```

### b. Mengerjakan praktikum minggu ketiga (Struktur Data) menggunakan Jupyter


#### 1. List
Menjalankan beberapa fungsi milik list pada struktur data :
* .count()
```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
```

* .index()
```python
fruits.index('banana')
3
fruits.index('banana', 4) 
6
```

* .reverse()
```python
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
```

* .append()
```python
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
```

* .sort()
```python
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
```

* .pop()
```python
fruits.pop()
'pear'
```


##### a) List sebagai Stack
Membuat list sebagai sebuah stack menggunakan jupyter notebook :
```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

##### b) List sebagai Queue
Membuat list sebagai sebuah queue menggunakan jupyter notebook
```python
>>> from collections import deque
>>> queue = deque(["Mamo", "David", "Travis"])
>>> queue.append("Cio")
>>> queue.append("Ajun")
>>> queue.popleft()
'Mamo'
>>> queue.popleft()
'David'
>>> queue
deque(['Travis', 'Cio', 'Ajun'])
```

##### C) List comprehensions
Membuat list yang comprehensif menggunakan jupyter notebook :
```python
>>> squares = []
>>> for x in range(5):
...     squares.append(x**3)
...    
squares
>>> squares = list(map(lambda x: x**3, range(5)))
>>> squares = [x**3 for x in range(5)]
>>> [(x, y) for x in [5,3,1] for y in [2,9,4] if x != y]
[(5, 2), (5, 9), (5, 4), (3, 2), (3, 9), (3, 4), (1, 2), (1, 9), (1, 4)]
>>> combs = []
>>> for x in [5,3,1]:
...    for y in [2,9,4]:
...        if x != y:
...            combs.append((x, y))

>>> combs
[(5, 2), (5, 9), (5, 4), (3, 2), (3, 9), (3, 4), (1, 2), (1, 9), (1, 4)]
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> [x, x**2 for x in range(6)]
  File "C:\Users\Riska\AppData\Local\Temp/ipykernel_5952/2204300083.py", line 1
    [x, x**2 for x in range(6)]
             ^
SyntaxError: invalid syntax
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

##### d) Perulangan List comperehensions
Membuat perulangan menggunakan list komprehensif menggunakan jupyter notebook :
```python
>>> matrix = [
...    [6, 1, 2, 4], 
...    [4, 8, 5, 3], 
...    [2, 3, 4, 1],
... ]
...
>>> [[row[i] for row in matrix] for i in range(3)]
[[6, 4, 2], [1, 8, 3], [2, 5, 4]]
>>> transposed = []
>>> for i in range(3):
...    transposed.append([row[i] for row in matrix])
...
>>> transposed
[[6, 4, 2], [1, 8, 3], [2, 5, 4]]
>>> transposed = []
>>> for i in range(4):
...    transposed_row = []
...   for row in matrix:
...        transposed_row.append(row[i])
...    transposed.append(transposed_row)
...
>>> transposed
[[6, 4, 2], [1, 8, 3], [2, 5, 4], [4, 3, 1]]
>>> list(zip(*matrix))
[(6, 4, 2), (1, 8, 3), (2, 5, 4), (4, 3, 1)]
```

#### 2. Statement Del
Menjalankan *statement del* menggunakan jupyter notebook :
```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

#### 3. Tuple and Sequence
Membuat tuple dan sequence menggunakan jupyter notebook :
```python
>>> t = 1004, 13120, 'Annyeong!'
>>> t[0]
1004
>>> t
(1004, 13120, 'Annyeong!')
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((1004, 13120, 'Annyeong!'), (1, 2, 3, 4, 5))
>>> t[0] = 88888
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_5952/16871866.py in <module>
----> 1 t[0] = 88888

TypeError: 'tuple' object does not support item assignment
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

#### 4. Set
Membuat set pada python menggunakan jupyter notebook :
```python
>>> treasure = {'Choi Hyunsuk', 'Park Jihoon', 'Yoshi', 'Kim Junkyu',  'Mashiho', 'Yoon Jaehyuk', 'Asahi', 'Bang Yedam', 
...            'Kim Doyoung', 'Haruto', 'Park Jeongwoo', 'So Junhwan'}
>>> print(treasure) 
{'Kim Junkyu', 'So Junhwan', 'Park Jeongwoo', 'Asahi', 'Bang Yedam', 'Kim Doyoung', 'Haruto', 'Yoon Jaehyuk', 'Yoshi', 'Choi Hyunsuk', 'Mashiho', 'Park Jihoon'}
>>> 'Mashiho' in treasure
True
>>> 'Ben' in treasure
False
>>> a = set('Lumos')
>>> b = set('Expecto Patronum')
>>> a
{'L', 'm', 'o', 's', 'u'}
>>> a - b
{'L', 's'}
>>> a | b
{' ',
 'E',
 'L',
 'P',
 'a',
 'c',
 'e',
 'm',
 'n',
 'o',
 'p',
 'r',
 's',
 't',
 'u',
 'x'}
>>> a & b
{'m', 'o', 'u'}
>>> a ^ b
{' ', 'E', 'L', 'P', 'a', 'c', 'e', 'n', 'p', 'r', 's', 't', 'x'}
>>> a = {x for x in 'lumos' if x not in 'abc'}
>>> a
{'l', 'm', 'o', 's', 'u'}
```

#### 5. Dictionary
Menerapkan fungsi *dictionary* pada struktur data Python kedalam sebuah program menggunakan jupyter notebook :
```python 
>>> truz = {'hikun': 404, 'ruru': 500}
>>> truz['yochi'] = 127
>>> truz
{'hikun': 404, 'ruru': 500, 'yochi': 127}
>>> truz['hikun']
404
>>> del truz['ruru']
>>> truz['lawoo'] = 340
>>> truz
{'hikun': 404, 'yochi': 127, 'lawoo': 340}
>>> list(truz)
['hikun', 'yochi', 'lawoo']
>>> sorted(truz)
['hikun', 'lawoo', 'yochi']
>>> 'yochi' in truz
True
>>> 'hikun' not in truz
False
>>> dict([('yochi', 127), ('lawoo', 340), ('hikun', 404)])
{'yochi': 127, 'lawoo': 340, 'hikun': 404}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(yochi=127, lawoo=340, hikun=404)
{'yochi': 127, 'lawoo': 340, 'hikun': 404}
```

#### 6. Teknik Looping
Menerapkan teknik looping pada struktur data Python kedalam terminal jupyter notebook :
```python 
>>> beast = {'Raib': 'Si Putri Bulan', 'Ali': 'Si Ceros Kerdil', 
...         'Seli': 'Si Prajurit Cahaya'}
>>> for k, v in beast.items():
...    print(k, v)
Raib Si Putri Bulan
Ali Si Ceros Kerdil
Seli Si Prajurit Cahaya
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...    print(i, v)
0 tic
1 tac
2 toe
>>> questions = ['Main Character', 'Book Title', 'gender']
>>> answers = ['Sokhe Bathera', 'Hujan', 'Men']
>>> for q, a in zip(questions, answers):
...    print('What is your {0}?  {1}'.format(q, a))
What is your Main Character?  Sokhe Bathera
What is your Book Title?  Hujan
What is your gender?  Men
>>> for i in reversed(range(1, 10, 2)):
...    print(i)
9
7
5
3
1
>>> treasure = {'Choi Hyunsuk', 'Park Jihoon', 'Yoshi', 'Kim Junkyu',  'Mashiho', 'Yoon Jaehyuk', 'Asahi', 'Bang Yedam', 
...            'Kim Doyoung', 'Haruto', 'Park Jeongwoo', 'So Junhwan'}
>>> for i in sorted(treasure):
...    print(i) 
Asahi
Bang Yedam
Choi Hyunsuk
Haruto
Kim Doyoung
Kim Junkyu
Mashiho
Park Jeongwoo
Park Jihoon
So Junhwan
Yoon Jaehyuk
Yoshi
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...    if not math.isnan(value):
...        filtered_data.append(value)

>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

#### 7. Lebih banyak kondisi
Menerapkan struktur data Python yang telah di pelajari sebelumnya dengan menggunakan lebih banyak kondisi :
```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```
