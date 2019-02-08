
# defining classes in python
class MyClass:
    y=4

number = MyClass()
print (number.y)

class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

# object created
user1= Person('Edith', '27', '55')
print (user1.name)
print (user1.age)
print (user1.weight)
print (f'my name is {user1.name} and I am {user1.age} years old')

user2= Person ('Prossy', '30', '40')
print (user2.name)
print (user2.age)
print (user2.weight)
print (f'my name is {user1.name} and I am {user1.age} years old')

# Animal class defined
class Animal:
    def __init__(self, name, sound, gender):
        self.name = name
        self.sound= sound
        self.gender = gender

# object created
animal1= Animal('Dog', 'bark', 'male')
print (animal1.name)
print (animal1.sound)
print (animal1.gender)
print (f'I am a {animal1.name} and always {animal1.sound} at strangers')


animal2= Animal('Lion', 'tiger', 'male')
print (animal2.name)
print (animal2.sound)
print (animal2.gender)
print (f'Being a {animal2.name} and that I {animal2.sound} scares away many people')


animal3= Animal('Goat', 'bleat', 'male')
print (animal3.name)
print (animal3.sound)
print (animal3.gender)
print (f'I {animal3.sound} because I am a {animal2.name}')


animal4= Animal('Monkey', 'screech', 'male')
print (animal4.name)
print (animal4.sound)
print (animal4.gender)
print (f'A {animal4.name} {animal2.sound} and it is so friendly')


animal5= Animal('Cat', 'meow', 'female')
print (animal5.name)
print (animal5.sound)
print (animal5.gender)
print (f'Being a {animal2.name} is the best nature I am proud of and also my {animal2.sound}')








