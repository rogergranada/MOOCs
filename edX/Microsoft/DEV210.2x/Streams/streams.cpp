#include <string>
#include <iomanip>// Necessary for parameterized manipulators.
#include <iostream>   // Necessary for general stream I/O definitions.

void calculate(){
    double unitPrice;
    int quantity;

    std::cout << "What is the unit price? ";
    std::cin >> unitPrice;

    std::cout << "How many do you want? ";
    std::cin >> quantity;

    std::cout << "Total cost is " << unitPrice * quantity << std::endl;
}

void getSentence(){
    std::string name;
    std::cout << "Full name: ";
    std::getline(std::cin, name);
    
    std::string address;
    std::cout << "Full address: ";
    std::getline(std::cin, address);
    
    std::cout 
        << name << std::endl
        << address << std::endl;
}

class point {
    public:
        int x, y;    
};

std::istream & operator >> (std::istream & is, point & p){
    is >> p.x >> p.y;
    return is;
}

std::ostream & operator << (std::ostream & os, const point & p) {
    os << "[" << p.x << "," << p.y << "]";
    return os;
}

void runPoint(){
    point p1, p2;
    std::cout << "Please enter two points: ";
    std::cin >> p1 >> p2;
    std::cout
    << "Here are your points..." << std::endl
    << p1 << std::endl
    << p2 << std::endl;
}

void formating(){
    //std::cout << std::setw(30) << -123.45 << std::endl; // set minimum width in console
    const char * message = "wibble";
    std::cout << "[" << std::setw(30) << message << "]" << std::endl;

    // control the justification of the text
    std::cout << std::left << "[" <<std::setw(40) << "hello" << "world" << "]" << std::endl;
     std::cout << "[" <<std::setw(10) << "hello" << "world" << "]" << std::endl;
    std::cout << std::right << "[" <<std::setw(10) << "hello" << "world" << "]" << std::endl;

    std::cout << std::internal << std::setw(10) << -123.45 << std::endl;

    double pi = 3.14159265358979;
    std::cout << std::fixed << pi << std::endl;
    std::cout << std::scientific << pi << std::endl;

    // reset 
    std::cout.unsetf(std::ios::fixed | std::ios::scientific);

}

int main{

    return 0;
}
