import java.util.Scanner;
public class User {
    
    public void userName(){
        Scanner sc=new Scanner(System.in);
        String name="a";
        while(!name.equals("N"))
        {
            System.out.println("����:");
            name=sc.next();
        }
        System.out.println("ע�����!");
        return;
    }
    public static void main(String[] args) {
        User a=new User();
        a.userName();
    }
}