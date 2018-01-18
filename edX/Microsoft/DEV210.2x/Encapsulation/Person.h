 #pragma once
    
#include <string>

class Person {
    private:
        std::string name;

    protected:
        int age;

    public:
        Person();
        Person(std::string fName, int age);
        virtual ~Person();

        void SayHello(); 
        virtual void display() const;  // Overrideable function.   

        // Classes that MUST be implemented in virtual classes
        virtual void show() const = 0;
};
