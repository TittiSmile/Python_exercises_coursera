class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")  
for f in sorted(L, key=Fruit.sort_priority):  #da notare che quando si chiama il metodo con la classe (tipo statico in java) NON si mettono le () al metodo 
    print(f.name)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):    #quando si accede al metodo con un'istanza della classe si mettono le ()
    print(f.name)   
