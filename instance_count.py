# class User():
# def __init__(self,username):
# self.username = username
# class UserBuilder():
# count = 0
# def buildUser(self, name):
# self.count = self.count + 1
# return User(name)
# builder = UserBuilder()
# p = builder.buildUser("vetri")
# print(builder.count)
# q = builder.buildUser("Kiruba")
# r = builder.buildUser("dev")
# print(builder.count)

class User():
    count = 0

    def __init__(self,name):
        self.name = name
        User.count += 1


p = User("vetri")
# print(p.count)
q = User("vetri")
# print(q.count)
l = User("vetri")
print(p.count)


