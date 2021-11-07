class Programmer:
    def __init__(self,salary,work_hour):
        self.salary = salary
        self.work_hour = work_hour

    def __del__(self):
        print("oof, " + str(self.salary) + ", " + str(self.work_hour))

    def compare(self,other):
        if self.sallary == other.sallary:
            if self.work_hours < other.work_hour:
                return self
            else:
                return other
        elif self.salary < other.salary:
            return self
        elif self.salary > other.salary:
            return other


prog = Programmer(25000, 5)

print(prog.salary)

print(prog.work_hour)

del prog 
# print(prog.salary)