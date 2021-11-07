class player():
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def get_age(self):
        s = self.age
        return '{} is {} old'.format(self.name,s)

    def get_height(self):
        s = self.height
        return '{} is {} cm'.format(self.name,s)
    def get_weight(self):
        s = self.weight
        return '{} is {} weight'.format(self.name,s)
    
p1 = player("David Jones", 25, 175, 75)

s = p1.get_age()
print(s) 
print(p1.get_height()) 
print(p1.get_weight()) 
