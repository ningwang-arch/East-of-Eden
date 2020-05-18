package StudentManager;

import java.util.Scanner;

public class StudentManager {
    public static void main(String[] args) {
        final Scanner sc = new Scanner(System.in);
        while (true) {
            showMenu();
            String choice = sc.nextLine();
            switch (choice) {
                case "1":
                    System.out.println("添加学生");
                    break;
                case "2":
                    System.out.println("删除学生");
                    break;
                case "3":
                    System.out.println("修改学生");
                    break;
                case "4":
                    System.out.println("查看所有学生");
                    break;
                case "0":
                    sc.close();
                    System.exit(0);
                    break;
            
                default:
                    break;
            }
        }
    }
    public static void showMenu(){
        //功能界面输出
        System.out.println("----------欢迎使用学生管理系统----------");
        System.out.println("              1.添加学生              ");
        System.out.println("              2.删除学生              ");
        System.out.println("              3.修改学生              ");
        System.out.println("              4.查看所有学生           ");
        System.out.println("              0.退出系统              ");
        System.out.println("请输入你的选择:");
    }
}