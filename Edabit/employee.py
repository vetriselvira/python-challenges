class Employee():
    def __init__(self,firstname,lastname,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_str(class_object, date_str):
        '''Call as
           d = Date.from_str('2013-12-30')
        '''
        print(class_object)
        firstname, lastname, salary =  date_str.split('-')
        return class_object(firstname, lastname, salary)
        
       

emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_str("John-Smith-55000")
print(emp1.firstname)
print(emp2.firstname)