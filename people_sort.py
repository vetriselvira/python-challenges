class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    #def __repr__(self):
    #    return '{' + self.firstname + ', ' + self.lastname + ', ' + str(self.age) + '}'


persons = []

def peoples_sort(persons, key):
    if key == "firstname":
    # sort list by `name` in the natural order
        persons.sort(key=lambda x: x.firstname)
 
    # output: [{Joe, Finance, 25}, {John, IT, 28}, {Sam, Banking, 20}]
        return persons
 
    # sort list by `name` in reverse order
    elif key == "age":
        persons.sort(key=lambda x: x.age)
        return persons

    elif key == "lastname":
        persons.sort(key = lambda x:x.lastname)
        return persons
 
    # output: [{Sam, Banking, 20}, {John, IT, 28}, {Joe, Finance, 25}]
        #print(persons)

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
persons.append(p1)

persons.append(p2)
persons.append(p3)
print(f'persons_list{persons}')
print(peoples_sort(persons, "firstname") )
print(peoples_sort(persons, "age") )

# Alice, Michael, Zoey

#print(persons([p1, p2, p3], "lastname")) 
# Jones, Smith, Waters

#print(persons([p1, p2, p3], "age") )
# 21, 29, 40
