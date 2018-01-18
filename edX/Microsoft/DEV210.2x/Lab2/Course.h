#pragma once
    
#include <string>
#include "Student.h"
#include "Teacher.h"

class Course {
    private:
        std::string courseName;
        int nbStudents;
        int index;
        Student students[];
        Teacher teacher;

    public:
        Course();

        Course(std::string name, int numberStudents);

        ~Course();

        void AddStudent(Student st);

        void AddTeacher(Teacher te);

        Teacher getTeacher();

        std::string getCourseName();

        void showStats();
};
