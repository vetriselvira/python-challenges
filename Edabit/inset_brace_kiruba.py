class menu():
    to_right_count = -1
    def __init__(self,list):
        self.list = list      

    def to_right(self):
        to_right_list = self.list


        #print(f'length of to_right_list:{len(to_right_list)}')
        #print(f'self.to_right_count:{self.to_right_count}')
        if len(to_right_list) - 1 == self.to_right_count:
            self.to_right_count = -1

        #print(f'type(to_right_list[self.to_right_count]) is :{type(to_right_list[self.to_right_count])}')
        if type(to_right_list[self.to_right_count]) is list:
            to_right_list[self.to_right_count] = to_right_list[self.to_right_count][0] 

        self.to_right_count = self.to_right_count + 1
        to_right_list[self.to_right_count] = [to_right_list[self.to_right_count]]

    
p = menu([2,3,4])
p.to_right()
print(p.list)

p.to_right()
print(p.list)

p.to_right()
print(p.list)

p.to_right()
print(p.list)

