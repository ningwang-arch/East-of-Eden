import java.util.Scanner;
public class Tower {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int num=sc.nextInt();
        int half=num/2+1;
        for(int i=1;i<=(num%2==0?(half-1):half);i++)
        {
            for(int j=1;j<=half-i;j++)
            {
                System.out.print(" ");
            }
            for(int j=1;j<=2*i-1;j++)
            {
                System.out.print("*");
            }
            System.out.println();
        }
        for(int i=1;i<=half-1;i++)
        {
            for(int j=1;j<=i;j++)
            {
                System.out.print(" ");
            }
            for(int j=1;j<=2*(half-i)-1;j++)
            {
                System.out.print("*");
            }
            System.out.println();
        }
        sc.close();
    }
}