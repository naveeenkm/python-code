class Animal:
    sound=""
    def __init__(self,name):
       self.name=name
    def speak(self):
        print("name {}, sound {}".format(self.name,self.sound))
class Lion(Animal):
    sound="hhhhhh" 
    
lion=Lion("LION")
lion.speak()
                