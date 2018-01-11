#pragma once
#include "Interface.h"
#include "SecInterface.h"

class MultipleInheritance : public Interface, public SecInterface {
    private:
        bool log; 
    public:
        MultipleInheritance();
        virtual ~MultipleInheritance();

        bool myOwn();

        //Implement from Interface.h
        virtual void freeze();
        virtual void unfreeze();

        //Implement from SecInterface.h
        virtual void login();
        virtual void logout();
};
