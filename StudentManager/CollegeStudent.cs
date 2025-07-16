public class CollegeStudent : Student
{
    protected string subject;
    protected int avgGrades;

    public CollegeStudent(string studentName, int studentID, int age, string subject, int avgGrades) : base(studentName, studentID, age)
    {
        this.subject = subject;
        this.avgGrades = avgGrades;
    }
    public override void DisplayInformation()
    {
        Console.WriteLine($"Name: {this.studentName}, ID: {this.studentID}, Age: {this.age}, Subject: {subject}, Average Grade: {avgGrades}");
    }
}