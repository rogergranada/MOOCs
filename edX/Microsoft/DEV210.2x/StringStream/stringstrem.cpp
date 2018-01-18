#include <sstream>// For std::stringstream
#include <string> // For std::string
#include <iostream>   // For std::cout etc.
    
void divideString(){
    // Create a stringstream object.
    std::stringstream stream;
    
    // Set the string content for a stringstream.
    stream.str("Jane 42 15000");
    
    // Get the content from a stringstream.
    std::cout << "Content of string stream: " << stream.str() << std::endl;
    
    // We can still use the stringstream as stream of formatted data.
    std::string name;
    int age;
    double salary;
    stream >> name >> age >> salary;
    
    std::cout
        << "Name: " << name << std::endl
        << "Age: " << age << std::endl
        << "Salary:" << salary << std::endl; 
}

void reWrittingString(){
    // Create a stringstream object to write to an existing string.
    std::string str = "********************";
    std::stringstream stream(str);
    
    // Do some output.
    stream << "Jane" << " " << 42 << " " << 15000;
        
    // See the effect.
    std::cout << stream.str() << std::endl;
}

void readingFormattedString(){
    // Create a stringstream object to read from an existing string.
    std::string str = "Jane 42 15000";
    std::stringstream stream(str);
    
    // Read formatted data from stringstream.
    std::string name;
    int age;
    double salary;
    stream >> name >> age >> salary;
    
    std::cout
        << "Name: " << name << std::endl
        << "Age: " << age << std::endl
        << "Salary:" << salary << std::endl;

}

void readOnlyString(){
    // Create an ostringstream object, which supports write-only operations.
    std::ostringstream stream1;
    
    stream1 << "Jane" << " " << 42 << " " << 15000 << std::endl;
    
    // Create an istringstream object, which supports read-only operations.
    std::istringstream stream2(stream1.str());
    
    // Read formatted data from istringstream.
    std::string name;
    int age;
    double salary;
    stream2 >> name >> age >> salary;
    
    std::cout
        << "Name: " << name << std::endl
        << "Age: " << age << std::endl
        << "Salary:" << salary << std::endl; 
}

// Wide Characters
//- std::wstring represents a string of wide characters.
//- std::wistream, std::wostream, and std::wstream allow you to input and output wide characters. std::wcin and std::wcout are predefined instances of std::wistream and std::wostream respectively.
//- std::wistringstream, std::wostringstream, and std::wstringstream allow you to input and output wide characters to/from a string.
    
void wideCharacters(){
    std::wstringstream stream;
    
    stream << "Jane" << " " << 42 << " " << 15000 << std::endl;
    
    std::wstring formattedString = stream.str();
    std::wcout << formattedString;
    
    std::wstring name;
    int age;
    double salary;
    stream >> name >> age >> salary;
    
    std::wcout
        << "Name: " << name << std::endl
        << "Age: " << age << std::endl
        << "Salary:" << salary << std::endl;
}


int main(){
    wideCharacters();
}
