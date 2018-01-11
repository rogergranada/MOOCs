//standard includes
#include <iostream>

using namespace std;

class Person {
    private:
        string name;
        int age;
        int height;
        int weight;
    public:
        Person();
        Person(string pName, int pAge, int pHeight, int pWeight);
        ~Person();

        void setName(string pName);
        string getName(void);
        void setPerson(string pName, int pAge, int pHeight, int pWeight);
} person;

Person::Person(){
    name = "No name";
    age = 0;
    height = 0;
    weight = 0;
}

Person::Person(string pName, int pAge, int pHeight, int pWeight){
    name = pName;
    age = pAge;
    height = pHeight;
    weight = pWeight;
}

Person::~Person(){
    cout << "Destroy class" << endl;
}

void Person::setName(string pName) {
    this->name = pName;
}

string Person::getName(){
    return this->name;
}

void Person::setPerson(string pName, int pAge, int pHeight, int pWeight){
    this->name = pName;
    this->age = pAge;
    this->height = pHeight;
    this->weight = pWeight;
}

// Methods
void ModifyPerson(Person *person){
    cout << person->getName() << endl;
    person->setName("Roger Granada");
}

void PassByValue(int n){
    cout << "Function: PassByValue()" << endl;
    n++;
    cout << "New value: " << n << endl;
}

void PassByRef(int &n){
    cout << "Function: PassByRef()" << endl;
    n = 50;
    cout << "New value: " << n << endl;
}

int main(){
    
    int num1 = 3;
    int *pNum = new int;
    *pNum = 5; 
    
    cout << "Value of num1: " << num1 << endl;
    PassByValue(num1);
    cout << "After PassByValue: " << num1 << endl;

    PassByRef(*pNum);
    cout << "After PassByRef: " << *pNum << endl;

    PassByValue(*pNum);
    cout << "After PassByValue: " << *pNum << endl;

    double *pDouble = new double; 
    *pDouble = 5.0;
    cout << *pDouble << endl;
    delete pDouble;
    cout << pDouble << endl;
    
    Person *p = new Person("Roger", 37, 190, 86);
    ModifyPerson(p);
    cout << p->getName() << endl;
    
    return 0;
}
