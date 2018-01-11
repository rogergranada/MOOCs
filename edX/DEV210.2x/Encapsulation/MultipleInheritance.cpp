#include "MultipleInheritance.h"
#include <iostream>

MultipleInheritance::MultipleInheritance(){
}

MultipleInheritance::~MultipleInheritance(){
    std::cout << "Destructor of MultipleInheritance class" << std::endl;
}

bool MultipleInheritance::myOwn(){
    std::cout << "myOwn()" << std::endl;
}

void MultipleInheritance::freeze(){
    std::cout << "freeze()" << std::endl;
}

void MultipleInheritance::unfreeze(){
    std::cout << "unfreeze()" << std::endl;
}

void MultipleInheritance::login(){
    std::cout << "login()" << std::endl;
}

void MultipleInheritance::logout(){
    std::cout << "logout()" << std::endl;
}
