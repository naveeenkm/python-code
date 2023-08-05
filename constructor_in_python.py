class apple:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor
    def __str__(self):
        return ("color is {} flavor is {}".format(self.color,self.flavor))
        
person=apple("red","sweet")
'''print(person.color)
print(person.flavor) '''       
print(person)        
help(apple)       