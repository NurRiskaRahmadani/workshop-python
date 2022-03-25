class Cat:        
     kind = 'persians'
     kind1 = 'ragdoll'
     def __init__(self, name):
             self.name = name

d = Cat('Coco')
e = Cat('Pinky')
d.kind

e.kind1

d.name

e.name


class Cat:

    tricks = []             

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Cat('Coco')
e = Cat('Pinky')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks


class Cat:
           
    def __init__(self, name):
        self.name = name
        self.tricks = []  

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Cat('Coco')
e = Cat('Pinky')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks

e.tricks