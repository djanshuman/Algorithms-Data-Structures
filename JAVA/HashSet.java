import java.util.HashSet;
import java.util.Iterator;

public class HashSet1 {

    public static void main(String args[]){

        HashSet <String> h = new HashSet<String>();
        h.add("Dj Babu");
        h.add("Anshuman");
        h.add("Hello Rocky");

        Iterator <String> i = h.iterator();
            while(i.hasNext()){
                System.out.println(i.next());
        }
            for (String s : h){
                System.out.println(s);
            }
        System.out.println(h.contains("egg"));
        System.out.println(h.size());
        System.out.println(h.isEmpty());
        h.remove("Anshuman");
        System.out.println(h.size());
    }

}
