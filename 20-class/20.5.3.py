"""
Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: 
arms and legs. Create an instance method called limbs that, when called, returns the total number of limbs the animal has. 
To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. Call the limbs method on the spider 
instance and save the result to the variable name spidlimbs.

"""


class Animal():
    def __init__(self, arms, legs):
        self.arms=arms
        self.legs=legs
    def limbs(self):
        ls = self.arms+self.legs
        print(ls)
        return ls

spider = Animal(4,4)
spidlimbs = spider.limbs()



#RICORDA che quando dichiari una funzione in una classe devi SEMPRE mettere self come parametro (anche se non prende argomenti)
#ecco come sarebbe in java:

public class Animal
{
    private int arms = 0;
    private int legs = 0;
    Animal(int arms, int legs){
        this.arms=arms;
        this.legs=legs;
    }

    int limbs(){
        return this.arms+this.legs;
    }
    
    @Override
    public String toString(){
        return " "+ this.arms+" "+ this.legs;
    }

    public static void main(String[] args) {
        System.out.println("Welcome to Online IDE!! Happy Coding :)");
        Animal spider = new Animal(4,4);
        int ls = spider.limbs();
        System.out.println(ls);
    }
}

