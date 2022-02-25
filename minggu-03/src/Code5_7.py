basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)          # Menampilkan duplikat setelah dipindahkan

'orange' in basket     # Menguji kecepatan membership

'crabgrass' in basket


# Mendemonstrasikan operasi set dengan unique letter dari dua kata

a = set('abracadabra')
b = set('alacazam')
a          # unique letters in a

a - b      # letters in a but not in b

a | b      # letters in a or b or both

a & b      # letters in both a and b

a ^ b      # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a