#include "Person.h"
#include <iostream>

Person::Person(){
}

Person::Person(std::string fName, std::string lName, int pAge, std::string typeRace, int nPhone){
    firstName = fName;
    lastName = lName;
    age = pAge;
    race = typeRace;
    phone = nPhone;
}

Person::~Person(){
    std::cout << "Destructor of class Person" << std::endl;
}

void Person::OutputAge() const{
    std::cout << "I am " << this->age << " years old" << std::endl;
}

void Person::OutputIdentity() const{
     std::cout << "OutputIdentity() from Person::" << std::endl;
}

