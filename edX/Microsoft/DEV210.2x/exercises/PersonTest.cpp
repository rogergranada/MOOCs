#include <iostream>
#include "Person.h"

using namespace std;

int main()
{

    // create a Person instance using default constructor
    Person *pOne = new Person();
    
    // Create a Person instance using 2 argument constructor
    Person *pTwo = new Person("Tom", "Thumb");

    // Create a Person instance using 3 argument constructor
    Person *pThree = new Person("Tom", "Thumb", 15);

    //cout << pTwo->GetFirstName() << endl;
    pTwo->SayHello();

    // delete object, releasing memory
    delete pOne;
    //delete pTwo;
    delete pThree;

    // Create an object without "new" -- set the Person() constructor
    Person p;
    // Access functions by dot instead of arrow
    p.SayHello();

return 0;
}
