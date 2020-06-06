import java.util.*;
public class HashMap {


    public static void main(String [] args){

        java.util.HashMap<String,Integer> m = new java.util.HashMap<String, Integer>();
        m.put("Anshuman",10);
        m.put("Dj",20);
        m.put("Vijay",30);

        for (Map.Entry<String,Integer> x : m.entrySet()){
            System.out.println(x.getKey() + " " + x.getValue());

        }

        if(m.containsKey("Dj")){
            System.out.println("Key is present");
        }
        else{
            System.out.println("key is not present");
        }

        System.out.println(m.size());
        int x=m.remove("Dj");
        System.out.print(m + "---> " + x);
        //System.out.println(m.size());
    }

}
