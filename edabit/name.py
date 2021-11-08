class Name:
    def __init__(self,fname,lname):
        self.fname = fname.title()
        self.lname = lname.title()
        self.fullname = "{} {}".format(self.fname,self.lname)
        self.initials = "{}.{}".format(self.fname[0],self.lname[0])


p1 = Name("vetri", "selvi")
print(p1.fname)
print(p1.lname)
print(p1.fullname)
print(p1.initials)


        