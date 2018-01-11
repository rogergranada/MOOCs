#include "Student.h"
#include "Person.h"
#include <iostream>

Student::Student(){
}

Student::Student(std::string fName, std::string lName, int age, std::string typeRace, int nPhone) : Person(fName, lName, age, typeRace, nPhone){
}

Student::~Student(){
}

//void Student::OutputIdentity() const{
//    std::cout << "I am a student" << std::endl;
//}   

void Student::OutputAge() const{
    std::cout << "I am a student and "; // << std::endl;
    Person::OutputAge();
}

void Student::ChangeObject() {
    std::cout << ">>: " << this->lastName << std::endl;
    this->lastName = "John";
    std::cout << ">>: " << this->lastName << std::endl;
}
