#include <iostream>
using namespace std;

union numericUnion { 
    int intValue; 
    long longValue; 
    double doubleValue; 
};

struct structure {
    int intValue;
    long longValue; 
    double doubleValue; 
}; 

int main() {
    structure myStruct;
    myStruct.intValue = 3;
    cout << myStruct.intValue; cout << endl;
    myStruct.doubleValue = 4.5; 
    cout << myStruct.doubleValue << endl;
    cout << myStruct.intValue; cout << endl;

    numericUnion myUnion; 
    myUnion.intValue = 3;
    cout << myUnion.intValue << endl; 
    myUnion.doubleValue = 4.5; 
    cout << myUnion.doubleValue << endl; 
    // Cannot keep the 3 value in intValue
    // union keeps only one value at time
    cout << myUnion.intValue; cout << endl;
    
    return 0;
}
