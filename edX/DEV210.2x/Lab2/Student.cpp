#include "Student.h"
#include <iostream>

Student::Student(){
}

Student::Student(std::string fName, std::string lName, int age, std::string addr, std::string city, int number){
    firstName = fName;
    lastName = lName;
    age = age;
    address = addr;
    city = city;
    phone = number;
}

void Student::SetFirstName(std::string fName){
    this->firstName = fName;
}

std::string Student::GetFirstName(){
    return this->firstName;
}

void Student::SetLastName(std::string lName){
    this->lastName = lName;
}

std::string Student::GetLastName(){
    return this->lastName;
}

void Student::SetAge(int age){
    if (age > 0){
        this->age = age;
    }else{
        std::cout << "Please enter a valid age" << std::endl;
    }
}

int Student::GetAge(){
    return this->age;
}

void Student::SetAddress(std::string addr){
    this->address = addr;
}
        
std::string Student::GetAddress(){
    return this->address;
}

void Student::SetCity(std::string city){
    this->city = city;
}
        
std::string Student::GetCity(){
    return this->city;
}

void Student::SetPhone(int number){
    this->phone = number;
}
        
int Student::GetPhone(){
    return this->phone;
}

void Student::SitInClass(){
    std::cout << "Sitting in main theater" << std::endl;
}

Student::~Student(){
}
