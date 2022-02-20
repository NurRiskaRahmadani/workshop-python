def fib(n):    # Menulis fibonacci
    """ Mencetak nilai fibonacci ."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Memanggil fungsi yang telah didefenisikan:
fib(2000)

fib

f = fib
f(100)

fib(0)
print(fib(0))



def fib2(n):  # Memanggil ulang fibonacci
    """Memanggil ulang fibonacci."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # lihat perubahan
        a, b = b, a+b
    return result

f100 = fib2(100)    # memanggil
f100                # menulis hasil