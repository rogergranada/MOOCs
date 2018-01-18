#include "Teacher.h"
#include "Person.h"
#include <iostream>

Teacher::Teacher(){
}

Teacher::Teacher(std::string fName, std::string lName, int age, std::string typeRace, int nPhone) : Person(fName, lName, age, typeRace, nPhone){
}

Teacher::~Teacher(){
}

void Teacher::OutputIdentity() const{
    std::cout << "I am a teacher" << std::endl;
}   

void Teacher::OutputAge() const{
    std::cout << "I am a teacher and ";
    Person::OutputAge();
}
