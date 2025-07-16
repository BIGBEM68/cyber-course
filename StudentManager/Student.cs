public class Student : IPerson
{
    protected string studentName;
    protected int studentID;
    protected int age;

    public Student(string studentName, int studentID, int age)
    {
        this.studentName = studentName;
        this.studentID = studentID;
        this.age = age;
    }
    public void SetStudentName(string studentName)
    {
        this.studentName = studentName;
    }
    public string GetStudentName()
    {
        return this.studentName;
    }
    public void SetStudentID(int studentID)
    {
        this.studentID = studentID;
    }
    public int GetStudentID()
    {
        return this.studentID;
    }
    public void SetAge(int age)
    {
        this.age = age;
    }
    public int GetAge()
    {
        return this.age;
    }
    public virtual void DisplayInformation()
    {
        Console.WriteLine($"Name: {this.studentName}, ID: {this.studentID}, Age: {this.age}");
    }
    public (string,int,int) GetStudentInfo()
    {
        return (this.studentName, this.studentID, this.age);
    }
}
