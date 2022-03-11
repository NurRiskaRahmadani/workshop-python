print('Find your {} Hi we are "{}!"'.format('Treasure', 'Treasure'))

print('{0} and {1}'.format('merch', 'lightstic'))

print('{1} and {0}'.format('merch', 'lightstic'))

print('This {food} is {adjective}.'.format( 
      food='spam', adjective='absolutely horrible'))

print('Once upon {0} in the {1}, world must be {other}.'.format('fish', 'sky', other='weird'))

table = {'Ondu': 4001, 'Sabeom': 1321, 'Bangjeon': 5214, 'Jokwon': 3920}
print('Bangjeon: {0[Bangjeon]:d}; Jokwon: {0[Jokwon]:d}; ' 
    'Ondu: {0[Ondu]:d}; Sabeom: {0[Sabeom]:d}'.format(table))

table = {'Ondu': 4001, 'Sabeom': 1321, 'Bangjeon': 5214, 'Jokwon': 3920}
print('Bangjeon: {Bangjeon:d}; Jokwon: {Jokwon:d}; Ondu: {Ondu:d}; Sabeom: {Sabeom:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))