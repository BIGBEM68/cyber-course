// See https://aka.ms/new-console-template for more information
Student s1 = new Student("Yuval", 311, 17);
s1.DisplayInformation();
CollegeStudent s2 = new CollegeStudent("Noam", 502, 20, "biology", 92);
s2.DisplayInformation();
s1.SetStudentName("Shaked");
s2.SetStudentID(927);
s1.DisplayInformation();
s2.DisplayInformation();