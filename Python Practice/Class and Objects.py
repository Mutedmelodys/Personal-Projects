print("Hello World")
#Prints the words, Hello World
''' thid is a comment
of multiple lines
now eat it
'''
'''
class User:
    pass
user1 = User()
user1.first_name = 'Dave'
user1.last_name = 'Bowman'

print(user1.first_name)
print(user1.last_name)

first_name = 'Arthur'
last_name = 'Clarke'

print(first_name, last_name)
        

user2 = User()
user2.first_name = 'Frank'
user2.last_name = 'Poole'

print(user1, user2)
'''
import datetime

class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        #extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    def age(self):
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
        



user = User('Dave Bowman', "19710315")
print(user.name)
print(user.birthday)

print(user.first_name)
print(user.last_name)
print(user.birthday)

print(user.age())
