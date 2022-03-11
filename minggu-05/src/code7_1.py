import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Ondu': 4001, 'Sabeom': 1321, 'Bangjeon': 5214, 'Jokwon': 3920}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


animals = 'Quokka'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')