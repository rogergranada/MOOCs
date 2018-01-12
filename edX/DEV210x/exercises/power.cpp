#include <iostream>
using namespace std;


int power_of(int base, int exponent){
    int total = 1;
    for (int i=0; i<exponent; i++)
        total *= base;
    cout << total << endl;
    return total;
}

int switcher(char ch){
    switch (ch){
       case 'y':
       case 'Y':
            cout << "You chose y or Y" << endl;
            break;
       case 'n':
       case 'N':
            cout << "You chose n or N" << endl;
            break;
        default:
            cout << "You didn't choose a valid option" << endl;
            break;
    }
    return 0;
}
