"""
human class
constructor - name, eyes, ears, nose, tongue, skin
methods - walking, talking
"""

class Human:
    def __init__(self, name ,eyes, ears, nose, tongue, skin, skin_tone, limbs, height):
        self.name = name
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.tongue = tongue
        self.skin = skin
        self.skin_color = skin_tone
        self.limbs = limbs
        self.height = height
    
    def walking(self):
        print(f"{self.name} is walking")
    
    def talking(self):
        print(f"{self.name} is talking")
    

Miracle = Human("chiemerie", 2, 2, 1, 1, "feeling", "chocolate", 4, "5'11")


Miracle.walking()
Miracle.talking()

