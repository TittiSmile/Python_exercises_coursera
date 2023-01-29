"""
in questo esercizio, voglio sommare i valori della coordinata x e y tra due punti (p1 e p2).
normalmente, non potrei fare p1+p2 perchè python non capisce che ci sono dentro due interi da sommare.
come fare?
si dichiara il metodo add.

il metodo prende 2 parametri. self (parametro che ci vuole SEMPRE) e un altro parametro che rappresenta un altro punto.
il return di questo metodo sarà un nuovo punto che avrà, come parametri nel costruttore () la somma tra i due punti x e y.
il primo ci faccio accesso con self e il secondo con other point. semplice semplice.

discorso simile anche per la sottrazione.


"""


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return "Point: ("+ str(self.x)+", " + str(self.y)+") "
        #return "Point: ({}, {})".format(self.x, self.y)
    def __add__(self, otherPoint):  #sto dichiarando la somma tra due punti
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)
    def __sub__(self, otherPoint):  #sto dichiarando la sottrazione tra due punti
        return Point(self.x - otherPoint.x, self.y - otherPoint.y)
    

p1 = Point(5,10)
p2 = Point(10,15)
p3=(p1+p2)
p4=(p1-p2)
print(p4)



#####VARIANTE con attributi nella classe. 

class Point:
    x=0
    y=0
    
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "Point: ("+ str(self.x)+", " + str(self.y)+") "
        #return "Point: ({}, {})".format(self.x, self.y)
    def __add__(self, otherPoint):  #sto dichiarando la somma tra due punti
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)
    def __sub__(self, otherPoint):  #sto dichiarando la sottrazione tra due punti
        return Point(self.x - otherPoint.x, self.y - otherPoint.y)
    

p1 = Point(5,10)
p2 = Point(10,15)
p3 = Point(p1.x+p2.x, p2.x+p2.y)
p4 = (p1+p2)
print(p3)
print(p4)
#p3 e p4 riconducono alla stessa cosa (somma tra punti)

"""
in questo esempio, dichiaro esplicitamente le variabili della classe point (x ed y).
normalmente, non sarebbe necessario. nel senso che quando dichiaro init e i suoi attributi (al di fuori di self), sto dicendo
che quei parametri (in questo caso x e y) sono attributi della classe.
infatti posso accedere tranquillamente ad x attraverso un'istanza di point. cioè posso fare:
p1.x e mi stamperà 5
p1.y e mi stamperà 10
"""
















#IN JAVA SAREBBE COSì:
"""
public class Main
{
    private int x;
    private int y;
    Main(int x, int y){
        this.x=x;
        this.y=y;
    }
    
    @Override
    public String toString(){
        return this.x + " " + this.y;
    }
    
    
    public static void main(String[] args) {
        System.out.println("Hello World");
        Main m = new Main(1,2);
        Main m2 = new Main(5,8);
        Main m3 = new Main(m.x+m2.x, m.y+m2.y);
        System.out.println(m);
        System.out.println(m2);
        System.out.println(m3);
    }
}



"""
