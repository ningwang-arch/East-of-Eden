import java.util.Scanner;
public class User {
    
    public void userName(){
        Scanner sc=new Scanner(System.in);
        String name="a";
        while(!name.equals("N"))
        {
            System.out.println("ĞÕÃû:");
            name=sc.next();
        }
        System.out.println("×¢²á½áÊø!");
        return;
    }
    public static void main(String[] args) {
        User a=new User();
        a.userName();
    }
}