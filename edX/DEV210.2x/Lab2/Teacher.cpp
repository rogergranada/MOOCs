#include "Teacher.h"
#include <iostream>

Teacher::Teacher(){
}

Teacher::Teacher(std::string fName, std::string lName, int age, std::string addr, std::string city, int number){
    firstName = fName;
    lastName = lName;
    age = age;
    address = addr;
    city = city;
    phone = number;
}

void Teacher::SetFirstName(std::string fName){
    this->firstName = fName;
}

std::string Teacher::GetFirstName(){
    return this->firstName;
}

void Teacher::SetLastName(std::string lName){
    this->lastName = lName;
}

std::string Teacher::GetLastName(){
    return this->lastName;
}

void Teacher::SetAge(int age){
    if (age > 0){
        this->age = age;
    }else{
        std::cout << "Please enter a valid age" << std::endl;
    }
}

int Teacher::GetAge(){
    return this->age;
}

void Teacher::SetAddress(std::string addr){
    this->address = addr;
}
        
std::string Teacher::GetAddress(){
    return this->address;
}

void Teacher::SetCity(std::string city){
    this->city = city;
}
        
std::string Teacher::GetCity(){
    return this->city;
}

void Teacher::SetPhone(int number){
    this->phone = number;
}
        
int Teacher::GetPhone(){
    return this->phone;
}

void Teacher::GradeStudent(){
    std::cout << "Student graded" << std::endl;
}

void Teacher::SitInClass(){
    std::cout << "Sitting at front of class" << std::endl;
}

Teacher::~Teacher(){
}
