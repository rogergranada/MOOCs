#include "Student.h"
#include <iostream>

Student::Student(){
}

Student::Student(std::string name, int age, std::string course) : Person(name, age), course(course){
}

Student::~Student(){
    std::cout << "Destructor of Student class" << std::endl;
}

void Student::setAge(int age){
    if (age < 5){
        std::cout << "Student age needs to at least 5 years old." << std::endl;
    }else{
        this->age = age;
    }
}

int Student::getAge(){
    return this->age;
}

void Student::setCourse(std::string course){
    this->course = course;
}

void Student::SayHello(){
    std::cout << "Hey, how's it goin'?" << std::endl;
}

void Student::display() const {
    // Call base-class version of display(), to display person-related info.
    Person::display();

    // Now display the student-related info.
    std::cout << course << std::endl;
}

void Student::show() const {
    //This function must be implemented when inherit Person
}
