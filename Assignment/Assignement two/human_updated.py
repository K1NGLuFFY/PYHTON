"""
This code defines a Human class that represents basic human attributes and behaviors.
The class stores physical characteristics like the five sense organs (eyes, ears, nose, tongue, skin),
skin color, limbs, and height as instance attributes. It also includes three methods that simulate
basic human actions: walking, speaking, and breathing.
The code then creates two Human objects (person1 and person2) with different attributes,
displays their characteristics, and demonstrates their behaviors by calling the methods.
"""

class Human:
    def __init__(self, eyes, ears, nose, tongue, skin, skin_color, limbs, height):
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.tongue = tongue
        self.skin = skin
        self.skin_color = skin_color
        self.limbs = limbs
        self.height = height
    
    def walking(self):
        print("I am walking")
    
    def speaking(self):
        print("I am talking")
    

person1 = Human("two eyes", "two ears", "one nose", "one tongue", "skin for touch", "fair", 4, "5'6\"")

print(person1.eyes)
print(person1.ears)
print(person1.nose)
print(person1.tongue)
print(person1.skin)
print(person1.skin_color)
print(person1.limbs)
print(person1.height)

person1.walking()
person1.speaking()

person2 = Human("two eyes", "two ears", "one nose", "one tongue", "skin for touch", "dark", 4, "6'0\"")

print(person2.eyes)
print(person2.ears)
print(person2.nose)
print(person2.tongue)
print(person2.skin)
print(person2.skin_color)
print(person2.limbs)
print(person2.height)
person2.walking()
person2.speaking()
person2.breathing()
