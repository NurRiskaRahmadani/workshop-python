import math
print('The value of pi is approximately %5.3f.' % math.pi)

f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed

f.close()
f.read()

f.read()

f.read()

f.readline()
f.readline()
f.readline()

for line in f:
    print(line, end='')

f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)


