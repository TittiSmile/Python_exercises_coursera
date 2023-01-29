city_names = ["Detroit", "Ann Arbor", "Pittsburgh", "Mars", "New York"]
populations = [680250, 117070, 304391, 1683, 8406000]
states=["MI", "MI", "PA", "PA", "NY"]

city_tuples = list(zip(city_names, populations, states))	#metto tutte le info delle liste in un'unica tupla


class City:				#creo la classe città
    def __init__(self, name, pop,state):
        self.name=name
        self.pop=pop
        self.state=state
    def __str__(self):		#è l'equivalente di toString. quando stampo un'entità della città non mi escono cose strane.
        return self.name+" "+str(self.pop)+" "+self.state
        #return "{}, {} (pop: {})".format(self.name, self.state, self.pop)



my_city = City("aa", 123, "bb") #creo una nuova istanza di city
#print(my_city)

#inserisco TUTTE le città, popolazioni e stati in delle nuove entità di città
cities=[]
for i in city_tuples:
    name, population, state = i #in questo modo "divido" la tupla in singole stringhe/interi
    #print(name,population,state) # li stampa tutti sulla stessa linea NON come tupla
    new_city = City(name, population,state) #nuova istanza
    cities.append(new_city)

print(cities)   #è una lista di città (esce solo il tipo, ci vuole il corrispettivo di toString)


lst_cities = [City(name,population,state) for (name,population, state) in city_tuples]
#lst_cities = [City(*t) for t in city_tuples] #funziona come la riga di sopra solo che *t ti prende tutte le entità della tupla (nome, popolazione e staticmethod)

print("\n\n",lst_cities)


    







