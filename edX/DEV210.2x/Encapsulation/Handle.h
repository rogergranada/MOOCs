#include "Body.h"

class Handle {
    private:
        Body * body;   // The "handle" class typically maintains an internal instance of the "body" class.

    public:
        Handle();
        ~Handle();

        void someOperationOnBody();
        void ShowChange();
};
