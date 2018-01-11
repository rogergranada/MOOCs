#include <iostream>
#include "MultipleInheritance.h"

using namespace std;

int main(){
    MultipleInheritance *st1 = new MultipleInheritance();
    st1->myOwn();
    st1->freeze();
    st1->unfreeze();
    
    delete st1;

    return 0;
}
