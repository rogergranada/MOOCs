#pragma once

// Pure virtual class
class Interface {
    public:
        virtual void freeze() = 0;
        virtual void unfreeze() = 0;
};
