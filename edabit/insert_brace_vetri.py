
class Menu:
    to_right_count = 0

    def __init__(self,list):
        self.list = list

    def to_right(self):
        to_right_list = self.list
        if len(to_right_list) - 1 == self.to_right_count:
            self.to_right_count = 0
        if type(to_right_list[self.to_right_count]) is list:
            to_right_list[self.to_right_count] = to_right_list[self.to_right_count][0]
        self.to_right_count = self.to_right_count + 1
        to_right_list[self.to_right_count] = [to_right_list[self.to_right_count]]
       

p = Menu([2,3,4])
p.to_right()
print(p.list)
p.to_right()
print(p.list)
p.to_right()
print(p.list)
