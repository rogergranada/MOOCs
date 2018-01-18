//#include "stdafx.h"
#include <iostream>

using namespace std;

void explaination(){
    int num = 3;

    //alias to the num variable
    int &refNum = num;
    
    //a pointer holding the address of num
    int *pNum = &num;

    //a pointer to int and allocate space for it
    int *pInt = new int; 
    //store the value 3 in the memory location
    *pInt = 3; 
    //remove from memory
    delete pInt;
}

int intropointer(){
    int num = 3;
    int* pNum = &num;
    cout << pNum << endl;
    return 0;
}

int dereference(){
    int num = 3;
    int *pNum = &num;
    cout << pNum << endl;
    cout << *pNum << endl;

    *pNum = 45;
    cout << *pNum << endl;
    cout << num << endl;
    return 0;
}

int refnum(){
    int num = 3;
    int &refNum = num;

    cout << "num contains " << num << endl;
    cout << "refNum contains " << refNum << endl;

    refNum++;    // increment refNum by 1

    cout << "num contains " << num << endl;
    cout << "refNum contains " << refNum << endl;
    cout << "refNum is located at " << &refNum << " and num is located at " << &num << endl;
    return 0;
}

int main()
{
    //intropointer();
    //dereference();
    refnum();
    return 0;
}
