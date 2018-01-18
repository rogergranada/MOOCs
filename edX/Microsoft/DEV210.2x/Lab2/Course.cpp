#include "Course.h"
#include "Student.h"
#include "Teacher.h"
#include <iostream>

Course::Course(){
}

Course::Course(std::string name, int numberStudents){
    courseName = name;
    index = 0;
    nbStudents = numberStudents;
    students[numberStudents]; 
}

void Course::AddStudent(Student st){
    this->students[this->index] = st;
    this->index++;
}

void Course::AddTeacher(Teacher teacher){
    this->teacher = teacher;
}

Teacher Course::getTeacher(){
    return this->teacher;
}

std::string Course::getCourseName(){
    return this->courseName;
}

void Course::showStats(){
    std::cout << this->courseName << std::endl;
    std::cout << this->nbStudents << std::endl;
    std::cout << this->index << std::endl;
    std::cout << this->students << std::endl;
}

Course::~Course(){
}

