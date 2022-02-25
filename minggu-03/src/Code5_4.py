squares = []
for x in range(4):
    squares.append(x**2)

squares

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]

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