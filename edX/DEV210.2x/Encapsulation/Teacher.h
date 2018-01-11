#pragma once
    
#include <string>

class Teacher {
    private:
        std::string firstName;
        std::string lastName;
        int age;
        std::string address;
        std::string city;
        int phone;

    public:
        Teacher();

        Teacher(std::string fName, std::string lName, int age, std::string addr, std::string city, int number);

        ~Teacher();

        void SetFirstName(std::string fName);
        std::string GetFirstName();
        
        void SetLastName(std::string lName);
        std::string GetLastName();

        void SetAge(int age);
        int GetAge();

        void SetAddress(std::string addr);
        std::string GetAddress();

        void SetCity(std::string city);
        std::string GetCity();

        void SetPhone(int number);
        int GetPhone();

        void GradeStudent();

        void SitInClass();
};

