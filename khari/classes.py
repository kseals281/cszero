#Classes

class Animal(object):
    def __init__(self, species, lifespan, color, food, sound):
	self.species = species
	self.lifespan = lifespan
	self.color = color
	self.food = food
	self.sound = sound
	
    def Die(self, age):
	if age > self.lifespan:
	    print 'Bye cruel world'
	else:
	    print 'I get to live!'

class Elephant(Animal):
    
    def __init__(self, name):
	super(self, Elephant).__init__('elephant', 90, 'gray', 'peanuts', 'brrrr')
	
elephant = Elephant()

print elephant.food
