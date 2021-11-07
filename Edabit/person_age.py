#class Person():
#    def __init__(self, name, age):
#        self.name = name
 #       self.age = age
 #   def compare_age(self, other):
#        if other.age < self.age:
#            s = 'younger than'
#        elif other.age > self.age:
#            s = 'older than'
 #       elif other.age == self.age:
 #           s = 'the same age as' 
#        return '{} is {} me.'.format(other.name,s)
#p1 = Person("Samuel", 24)
#p2 = Person("Joel", 36)
#p3 = Person("Lily", 24)
#print(p1.compare_age(p2))
#print(p2.compare_age(p1))


class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def compare_age(self,other):
        if self.age > other.age:
            s = "elder"
        elif self.age < other.age:
            s = "younger"
        elif self.age == other.age:
            s = "same"
        return "{} is {} than {}".format(self.name,s,other.name)
p1 = Person("kiruba",35)
p2 = Person("vetri",32)
print(p1.compare_age(p2))
        