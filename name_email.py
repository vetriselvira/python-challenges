class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def fullname(self):
        return "full name is {}".format(self.fname + " " + self.lname)
    
    def email(self):
        return "email is {}".format(self.fname + "." + self.lname + "@company.com")


p1 = Employee("vetri","rajangam")
print(p1.fullname())
print(p1.email())