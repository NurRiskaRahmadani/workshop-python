from collections import deque
queue = deque(["David Kim", "Mama Takata", "Travis Watanabe"])
queue.append("Daniel Choi")           # Memasukkan Daniel kedalam antrian
queue.append("Kyle Bang")          # Memasukkan Kyle kedalam antrian
queue.popleft()                 # Memindahkan data pertama

queue.popleft()                 # Memindahkan data kedua

queue                           # Menyusun kembali antrian berdasarkan data yang dimasukkan 