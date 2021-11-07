class Countries():
    
    def __init__(self,country,population,area):
        self.population = population
        self.area = area
        self.country = country
        self.is_big = population>250*10**6 or area>3*10**6

    def compare(self,country):
        if self.population < country.population:
            return f'{self.country} has a  larger population density than {country.country}'
        
australia = Countries("Australia", 23545500, 7692024)
andorra = Countries("Andorra", 76098, 468)
print(australia.is_big)
print(andorra.is_big)
print(andorra.compare(australia))
