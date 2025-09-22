class User:
    # Firstname = "K1ng"
    # Lastname = "chiemerie"
    # age = 19
    # Gender = "male"
    # Nationality = "nigerian"
    # Email = "fake@gmail.com"
    # Phone = "09060495111"
    
    def __init__(self, firstname, lastname, age, gender, nationality, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.email = email
        self.phone = phone

"""
method to return fristname
"""
def print_firstname(self):
    return self.firstname

#obejct of the class user
userChiemerie = User("chiemerire" , "okafor" , "19" , "male" ,"nigerian" , "fake@gmail.com" , "09060495111")
print(userChiemerie.firstname)

# user2 = User()

# user1.Lastname = "Okafor"
# print(user1.Lastname)
# print(user1.Firstname)
# print(user1.Lastname)
# print(user1.age)
# print(user1.Gender)
# print(user1.Nationality)
# print(user1.Email)
# print(user1.Phone)
