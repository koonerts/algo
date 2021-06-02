#include <iostream>
#include <vector>

void print(bool b) {
    std::cout << b << std::endl;
}

int main() {
    std::vector<bool> vb{true, false, true};
    auto b = vb[0];
    print(b);
}

