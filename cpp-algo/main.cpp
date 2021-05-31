#include <iostream>
#include <vector>
#include <iterator>


int main() {
    std::vector<int> v1{1, 2, 3, 4, 5};
    std::vector<int> v2(v1.begin()+2, v1.end());
    v2[0] = 1;

    std::copy(v1.begin(), v1.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;
    std::copy(v2.begin(), v2.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;
}