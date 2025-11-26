import java.util.*;
class Employ{
    String name;
    int id;

    public Employ(String name, int id){
        this.name = name;
        this.id = id;

    }
    public void display(){
        System.out.println("name : " + name + "ID :" + id),
    }
}
public class Main{
    public static void main(String[] args){
        Employ ob = new Employ[5];
        
        ob[0] = new Employ("maaty", 100);
        ob[1] = new Employ("sami", 70);
        ob[2] = new Employ("bety", 50)
        ob[3] = new Employ("chala", 200);
        ob[4] = new Employ("kidus", 10);

    for(int i = 0; i<ob.lenght && ob[i] != null; i++){
    ob[i].display();
    
}
}
}
