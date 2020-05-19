package StudentManager;

import java.util.ArrayList;
import java.util.Scanner;

public class StudentManager {
    public static void main(String[] args) {
        final Scanner sc = new Scanner(System.in);
        //创建学生集合,存储学生对象
        ArrayList<Student> array=new ArrayList<Student>();
        while (true) {
            showMenu();
            String choice = sc.nextLine();
            System.out.println();
            switch (choice) {
                case "1":
                    //System.out.println("添加学生");
                    addStudent(array);
                    break;
                case "2":
                    //System.out.println("删除学生");
                    delStudent(array);
                    break;
                case "3":
                    //System.out.println("修改学生");
                    updateStudent(array);
                    break;
                case "4":
                    //System.out.println("查看所有学生");
                    showAllStudent(array);
                    break;
                case "0":
                    sc.close();
                    System.exit(0);
                    break;

                default:
                    break;
            }
            System.out.println();
        }
    }
    //显示功能菜单
    public static void showMenu(){
        //功能界面输出
        System.out.println("----------欢迎使用学生管理系统----------");
        System.out.println("              1.添加学生              ");
        System.out.println("              2.删除学生              ");
        System.out.println("              3.修改学生              ");
        System.out.println("              4.查看所有学生           ");
        System.out.println("              0.退出系统              ");
        System.out.println("-------------------------------------");
        System.out.println("请输入你的选择:");
    }
    //添加学生信息
    public static void addStudent(ArrayList<Student> array){
        Scanner sc=new Scanner(System.in);
        //键盘录入学生对象所需要的数据,显示提示输入何种信息
        System.out.println("请输入学生学号:");
        String sid=sc.nextLine();
        //判断学号是否已使用
        if(!idISExist(array,sid)) {
            System.out.println("学号已存在,添加失败");
            sc.close();
            return;
        }


        System.out.println("请输入学生姓名:");
        String name=sc.nextLine();
        System.out.println("请输入学生年龄:");
        String age=sc.nextLine();
        System.out.println("请输入学生居住地:");
        String addr=sc.nextLine();
        //创建学生对象,将录入的数据赋值给学生对象
        Student s=new Student();
        s.setSid(sid);
        s.setName(name);
        s.setAge(age);
        s.setAddr(addr);
        //将学生对象添加到集合中
        array.add(s);
        System.out.println("添加成功!");
        sc.close();
    }
    //显示所有学生信息
    public static void showAllStudent(ArrayList<Student> array){
        if(array.size()==0){
            System.out.println("暂无信息,请在添加后查看");
            return;
        }
        //显示表头信息
        System.out.println("学号\t\t\t姓名\t\t年龄\t\t居住地");
        //将集合中数据取出,按照对应格式显示
        for (int i=0;i<array.size();i++){
            Student s=array.get(i);
            System.out.println(s.getSid()+"\t\t\t"+s.getName()+"\t"+s.getAge()+"岁\t"+s.getAddr());
        }
    }
    //删除学生
    public static void delStudent(ArrayList<Student> array){
        Scanner sc=new Scanner(System.in);
        System.out.println("请输入你要删除的学生的学号:");
        String sid=sc.nextLine();
        for (int i=0;i<array.size();i++){
            Student s=array.get(i);
            if (s.getSid().equals(sid)){
                array.remove(i);
                System.out.println("删除成功");
                sc.close();
                return;
            }
        }
        System.out.println("信息不存在,删除失败");
        sc.close();
    }
    //修改学生信息
    public static void updateStudent(ArrayList<Student> array){
        Scanner sc=new Scanner(System.in);
        System.out.println("请输入你要修改的学生学号:");
        String sid=sc.nextLine();
        //判断学号是否存在  不存在则返回失败
        if(idISExist(array,sid)){
            System.out.println("学号不存在,修改失败");
            sc.close();
            return;
        }


        System.out.println("请输入学生新姓名:");
        String name=sc.nextLine();
        System.out.println("请输入学生新年龄:");
        String age=sc.nextLine();
        System.out.println("请输入学生新居住地:");
        String addr=sc.nextLine();
        Student s=new Student();
        s.setSid(sid);
        s.setName(name);
        s.setAge(age);
        s.setAddr(addr);
        for(int i=0;i<array.size();i++){
            Student student=array.get(i);
            if(student.getSid().equals(sid)){
                array.set(i,s);
                System.out.println("修改成功");
                break;
            }
        }
        sc.close();
    }
    //判断学号是否存在  存在false 不存在true
    public static boolean idISExist(ArrayList<Student> array,String id){
        for (int i=0;i<array.size();i++){
            Student s=array.get(i);
            if(s.getSid().equals(id)){
                return false;
            }
        }
        return true;
    }
}
