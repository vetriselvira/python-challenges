class Employee():
    dict = {}

    def __init__(self,fullname, **kwargs):
        self.name,self.lastname = fullname.split(" ")
        for key,value in kwargs.items():
            #self.dict[key] = value 
            self.__setattr__(key, value)
        #print(self.dict)
            
 
        
        
john = Employee("John Doe")
#print(john.lastname)

mary = Employee("Mary Major", salary=120000)
print(mary.salary)
richard = Employee("Richard Roe", salary=110000, height=178)
print(richard.height)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
print(giancarlo.nationality)