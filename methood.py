class Calc_age():
    age=0
    def age_update(self):
        return self.age*18
    
person=Calc_age()
print(person.age_update())    
person.age=int(input("enter the age please"))   
print(person.age_update())