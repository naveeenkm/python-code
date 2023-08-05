class fruit():
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor
        pass
class apple(fruit):
    pass
class grapes(fruit):
    pass
apple=apple("red","testy")
grapes=grapes("green","litteleteasty")
print("apple color={},apple flavor = {},grapes color={} ,grapes flavor={}".format(apple.color,apple.flavor,grapes.color,grapes.flavor))

