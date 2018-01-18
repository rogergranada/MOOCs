#include <iostream>
using namespace std;

int main() {
    int y = 0;
    int x = 0;
    char response;
    cout << "Enter menu choice " << endl << "More" << endl << "Quit" << endl;
    cin >> response;

    while (response != 'Q'){
       switch (response){
           case 'y':
                y = x++;
                cout << x << endl << y << endl;
                break;
           case 'Y':
                cout << 'Y'; cout << endl;
                break;
           case 'n':
                cout << 'n'; cout << endl;
                break;
           default:
                cout << response; cout << endl;
                break;
        }
        // Prompt user again with menu choices until Quit is entered
        cout << ":" << endl;
        cin >> response;
    }
    return 0;
}
