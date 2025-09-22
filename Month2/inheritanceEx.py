class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname =lname
    def printFullname(self):
        print(self.fname + ""+ self.lname)
        
        
        
me = person("Chiemerie", "Okeke")
me.printFullname()


class Student(person):
    def printLname(self):
        print(self.lname)


me = Person("Chiemerie", "Okeke")
me.printFullname()
sanctus = Student ("Sanctus", "Cisco")
sanctus.printLname()
sanctus.printFullname()