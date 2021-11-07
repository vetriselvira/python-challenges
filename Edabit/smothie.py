class smoothie():
    ingredient = []
    price = 0
    cost = {
    "Strawberries": 1.50,
    "Banana":0.50,
    "Mango" :2.50,
    "Blueberries": 1.00,
    "Raspberries":1.00,
    "Apple"	:1.75,
    "Pineapple":3.50}
    total = 0 
    def __init__(self,ingredient):
        self.ingredient = ingredient

    
    def get_cost(self):
        t = 0
        for i in self.ingredient:
            t += self.cost[i]
        return t
            
    def get_price(self):
        p =self.get_cost()
        return p *1.5
        #return float(p.va) * 1.5
   
    def get_name(self):
        str = (sorted(self.ingredient))
        if len(str) > 1:
            str.append("Fusion")
        else:
            str.append("smoothie")
        return str

s1 = smoothie(["Banana"])
s2 = smoothie(["Apple","Mango"])
#print(s1.ingredient )  # ["Banana"]

#print(s1.price() )# "$0.50"

print(s1.get_cost() ) # "$1.25"
print(s1.get_price())
print(s2.get_cost())

#print(s1.get_name()) # "Banana Smoothie"

