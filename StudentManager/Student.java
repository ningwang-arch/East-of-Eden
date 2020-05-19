package StudentManager;

public class Student {
    private String sid;
    private String name;
    private String age;
    private String addr;
    public Student(){

    }
    public Student(String sid,String name,String age,String addr){
        this.sid=sid;
        this.name=name;
        this.age=age;
        this.addr=addr;
    }
    public void setSid(String sid)
    {
        this.sid=sid;
    }
    public String getSid(){
        return sid;
    }
    public void setName(String name){
        this.name=name;
    }
    public String getName(){
        return name;
    }
    public void setAge(String age){
        this.age=age;
    }
    public String getAge(){
        return age;
    }
    public void setAddr(String addr){
        this.addr=addr;
    }
    public String getAddr(){
        return addr;
    }

}
