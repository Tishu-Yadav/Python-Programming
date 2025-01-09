class Fruit:
    def __init__(self,name,season):
        self.__name= name
        self.season = season
    def get_name(self):
        return self.__name
    def set_name(self,value):
         self.__name = value
fruit = Fruit("Mango","Summer")
#print(fruit.name,fruit.season)
print(fruit.get_name(), fruit.season)
#fruit.name("Banana")
fruit.set_name("Banana")
print(fruit.get_name(), fruit.season)