#include <iostream>
#include "power_header.h"
using namespace std;



int main() {
    int base;
    int exponent;
    int total = 1;
    
    cout << "Enter your base number: " << endl;
    cin >> base;
    cout << "Enter your exponent number: " << endl;
    cin >> exponent;

    total = power_of(base, exponent);
    cout << "Total: " << total << endl;

    return 0;
}

