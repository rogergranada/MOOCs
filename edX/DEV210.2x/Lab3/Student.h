#pragma once
#include "Person.h"
#include <string>

class Student : public Person {
    public:
        Student();
        Student(std::string fName, std::string lName, int age, std::string typeRace, int nPhone);
        ~Student();

        //virtual void OutputIdentity() const;  // Overrideable function.   
        virtual void OutputAge() const;

        void ChangeObject();
};
