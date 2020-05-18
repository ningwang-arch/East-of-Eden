import java.util.ArrayList;

public class ArrayListTest {
    public static void main(String[] args) {
        ArrayList<String> array= new ArrayList<String>();
        System.out.println(array.add("hello"));
        array.add(" world");
        array.add(" worlda");
        array.add(" worldb");
        array.add(" worldc");
        array.add(" worldd");
        array.add(1, "test");
        System.out.println("array:"+array);
        System.out.println(array.remove("hello"));
        System.out.println("array:"+array);
        array.remove(3);
        System.out.println("array:"+array);
        array.set(2, "nothing");
        System.out.println("array:"+array);
        System.out.println(array.get(2));
    }
}