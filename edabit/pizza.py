class Pizza:
    ingredients = []
    order_number = 0

    order_number = 0

    def __init__(self,ingredients):
        self.ingredients = ingredients
        Pizza.order_number=+1

    @classmethod
    def hawaiian(class_object):
        ingredients = []
        ingredients.append("ham")
        ingredients.append("pineapple")
        order_number = +1
        return class_object(ingredients,order_number)

    @classmethod
    def meat_festival(class_object):
        ingredients =[]
        ingredients.append("beef")
        ingredients.append("meatball")
        ingredients.append("bacon")
        order_number = +1
        return class_object(ingredients,order_number)

    @classmethod
    def garden_feast(class_object):
        ingredients = []
        ingredients.append("spinach")
        ingredients.append( "olives")
        ingredients.append("mushroom")
        order_number =+1
        return class_object(ingredients,order_number)


p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()  
p3 = Pizza.hawaiian()
print(p1.ingredients) # ["bacon", "parmesan", "ham"]

print(p2.ingredients) # ["spinach", "olives", "mushroom"]

print(p1.order_number) # 1

print(p2.order_number) # 2   # order 2