#include <iostream>
#include "Person.h"
#include "Student.h"

using namespace std;

void demoFunction(Person * ptr){
    ptr->display();
}

void demoFunctionRef(Person & ptr){
    ptr.display();
}

int main(){
    Student *st1 = new Student("Tom", 25, "C++11");
    //st1->setAge(30);
    //st1->setCourse("C++");
    st1->display();

    
    demoFunction(st1);
    demoFunctionRef(*st1);

    
    delete st1;

    return 0;
}
