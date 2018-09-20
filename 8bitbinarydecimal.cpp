#include <iostream>
#include <cmath>

int main();

int main() {
    long unsigned int input;
    std::string type;
    std::cout << "Enter the number you would like converted to binary: ";
    std::cin >> input;
    if(std::cin.fail() || input > 255) {
        std::cout << "Error" << std::endl;
        return(0);
    }

    if(input < 128) {
        std::cout << "Would you like to print the leading 0s? ";
        std::cin >> type;
    }

    bool s(false);

    for (int i = 0; i < 8; i++) {
        long unsigned int power = pow(2, 7 - i);
        if(type == "y"){
            s = true;
        }
        if(power<=input){
            std::cout << 1;
            input=input-power;
            if(!s) s = true;
        }
        else if(power>input && s){
            std::cout << 0;
        }
    }

    return(0);
}