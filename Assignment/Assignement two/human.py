"""
This code defines a Human class that represents basic human attributes and behaviors.
The class stores physical characteristics like number of eyes, hair color, number of legs,
gender, and height as instance attributes. It also includes three methods that simulate
basic human actions: walking, speaking, and breathing.
The code then creates two Human objects (person1 and person2) with different attributes,
displays their characteristics, and demonstrates their behaviors by calling the methods.
"""

class Human:
    def _init_(self, no_of_eyes, hair_color, no_of_legs, gender, height):
        self.no_of_eyes = no_of_eyes
        self.hair_color = hair_color
        self.no_of_legs = no_of_legs
        self.gender = gender
        self.height = height
    
    def walking(self):
        print("I am walking")
    
    def speaking(self):
        print("I am talking") 
    
    def breathing(self):
        print("I am breathing")


person1 = Human(2, "brown", 2, "female", "5'6\"")

print(person1.no_of_eyes)
print(person1.hair_color)
print(person1.no_of_legs)
print(person1.gender)
print(person1.height)

person1.walking()
person1.speaking()
person1.breathing()

person2 = Human(2, "black", 2, "male", "6'0\"")

print(person2.hair_color)
print(person2.height)
person2.walking()
person2.speaking()
person2.breathing()