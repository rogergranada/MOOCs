#pragma once
#include "Person.h"
#include <string>

class Teacher : public Person {
    public:
        Teacher();
        Teacher(std::string fName, std::string lName, int age, std::string typeRace, int nPhone);
        ~Teacher();

        virtual void OutputIdentity() const;  // Overrideable function.   
        virtual void OutputAge() const;
};

