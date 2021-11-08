from os import name


class Numbers:
    def __init__(self, n):
        self.ones = n
        self.threes = n // 3
        self.nines = n // 9
        self.answer = 'nines:{}, threes:{}, ones:{}'.format(self.nines, self.threes,self.ones)
    
    # def find_divider(self):
    #  ones = self.ones
    #   threes = self.threes
    #   nines = self.nines
    #   return"nines :{} threes :{} ones: {},".format(self.nines,self.threes,self.ones)


n = Numbers(10)
print(n.answer)
