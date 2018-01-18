 #pragma once
    
#include <string>

class Person {
    private:
        int age;

    protected:
        int phone;

    public:
        std::string firstName;
        std::string lastName;
        std::string race;

        Person();
        Person(std::string fName, std::string lName, int pAge, std::string typeRace, int nPhone);
        virtual ~Person();

        virtual void OutputIdentity() const;  // Overrideable function.   
        virtual void OutputAge() const;
};
