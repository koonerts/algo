#include <iostream>
#include "topics/Arrays.h"
#include "ext/fmt.h"
#include "unordered_map"

using namespace std;
using namespace cpp_algo::topics;
using namespace cpp_algo::ext::fmt;



int main() {
    unordered_map<int, int> m{};
    cout << m[1] << endl;
    cout << m.contains(1) << endl;
}
