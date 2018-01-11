#include "Person.h"
#include <iostream>

Person::Person() : name("No Name"), age(0){
}

Person::Person(std::string fName, int pAge){
    name = fName;
    age = pAge;
}

Person::~Person(){
    std::cout << "Destructor of class Person" << std::endl;
}

void Person::SayHello(){
    std::cout << "Hello" << std::endl;
}

void Person::display() const {
    std::cout << "Name: " << this->name << std::endl;
    std::cout << "Age: " << this->age << std::endl;
}
