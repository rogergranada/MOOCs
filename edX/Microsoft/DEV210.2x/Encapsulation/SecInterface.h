#pragma once

// Pure virtual class
class SecInterface {
    public:
        virtual void login() = 0;
        virtual void logout() = 0;
};
