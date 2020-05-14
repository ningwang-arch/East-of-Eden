import java.util.Scanner;
import java.util.Random;
public class Guessnumber {
    public static void main(String[] args) {
        Random r=new Random();
        Scanner sc=new Scanner(System.in);
        int num=r.nextInt(100)+1;
        while(true)
        {
            System.out.println("请输入你要猜的数字:");
            int guess=sc.nextInt();
            if(guess<num)
            {
                System.out.println("你猜的数字 "+guess+" 过小");
            }else if(guess>num)
            {
                System.out.println("你猜的数字"+guess+"过大");
            }else{
                System.out.println("恭喜你猜对了");
                break;
            }
            System.out.println("==============================");
        }
        sc.close();
    }
}