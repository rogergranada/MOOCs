#include <iostream>
#include "Course.h"
#include "Teacher.h"
#include "Student.h"

using namespace std;

int main()
{

    // create three students
    Student *st1 = new Student("Student1", "St1", 20, "Rua 1", "POA", 123456789);
    Student *st2 = new Student("Student2", "St2", 20, "Rua 1", "POA", 123456789);
    Student *st3 = new Student("Student3", "St3", 20, "Rua 1", "POA", 123456789);
    
    // create the course
    Course *c1 = new Course("Intermediate C++", 3);

    // add students to the course
    //c1->AddStudent(*st1);
    //c1->AddStudent(*st2);
    //c1->AddStudent(*st3);

    // create a teacher
    Teacher *t = new Teacher("Teacher1", "Tch1", 40, "Rua 2", "POA", 123456543);

    // add teacher to the course
    c1->AddTeacher(*t);

    // output the name of the course
    std::cout << "Course name: " << c1->getCourseName() << std::endl;
    
    //Call the GradeStudent() method on the Teacher object
    c1->getTeacher().GradeStudent();

    // delete objects, releasing memory
    delete st1;
    delete st2;
    delete st3;
    delete c1;
    delete t;

    return 0;
}
