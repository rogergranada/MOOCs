class Handle;  // Forward reference of the "handle" class, so the compiler knows about it.

class Body {
    friend class Handle;

    private:
        int someData;
};
