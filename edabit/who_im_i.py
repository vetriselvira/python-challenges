class Memories:
    dict = {}

    def __init__(self):
        pass
    
    def add(self, **kwargs):
        for key,value in kwargs.items():
            self.dict[key] = value
 
    def remember(self, value):
        if value in self.dict:
            return self.dict[value]
        else:
            return False
            

memories = Memories()
memories.add(name="Shane", gender="M", catch_phrase="bazinga")

memories.add(work="None", love_life=0)

memories.add(adress="car")

print(memories.remember("address"))
print(memories.remember("catch_phrase"))

# If memory was not added, return False
print(memories.remember("lover"))
        

