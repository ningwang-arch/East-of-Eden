import java.util.Scanner;
public class hello{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int num=sc.nextInt();
		if(num%2==0)
		{
			System.out.println(num+"��ż��");
		}else{
			System.out.println(num+"������");
		}
		sc.close();
	}	
}