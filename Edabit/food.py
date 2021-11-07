class Food():
    #like = ["apple","orage","banana"]
    #hate = ["fish","chicken","mutton"]
    def __init__(self,name,like,hate):
        self.name = name
        self.hate = hate
        self.like = like

    def tase(self,given_food):
        if given_food in self.like:
            return "{} eats the {} and loves it".format(self.name,given_food)
        elif given_food in self.hate:
            return "{} eats the {} and hates it".format(self.name,given_food)
        else:
            return "{} eats the {} !".format(self.name,given_food)

a = Food("vetri",["chicken"],["carrot"]) 
print(a.tase("chips"))
