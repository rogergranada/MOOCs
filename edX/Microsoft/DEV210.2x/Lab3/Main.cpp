#include <iostream>
#include "Teacher.h"
#include "Student.h"

using namespace std;

int main()
{
    // create three students
    Student *stu = new Student("Student", "1", 20, "white", 123456789);
    Teacher *tea = new Teacher("Teacher", "1", 30, "black", 123456799);
    
    stu->OutputIdentity();
    stu->OutputAge();

    std::cout << "" << std::endl;

    tea->OutputIdentity();
    tea->OutputAge();

    std::cout << "" << std::endl;
    stu->ChangeObject();

    delete stu;
    delete tea;

    return 0;
}
