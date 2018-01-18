#include <iostream>
using namespace std;

class Rectangle {
    private:
    int _width;
    int _height;

    public:
    // Constructor
    Rectangle()
        : _width{}, _height{}
    {}

    Rectangle(int w, int h)
        : _width{w}, _height{h}
    {}

    void set_width(int v){
        _width = v;
    }

    void set_height(int v){
        _height = v;
    }

    int get_area(){
        return _width * _height;
    }
};

class Rectangle_new {
public:
    int _width;
    int _height;
};


int main() {
    Rectangle outer{2,2};
    Rectangle inner{};     

    //outer.set_width(10);
    //outer.set_height(10);
    /*
    inner._width = 5;
    inner._height = 5;*/
    cout << outer.get_area(); cout << endl;

    return 0;
}
