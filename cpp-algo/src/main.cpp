#include <iostream>
#include "topics/Arrays.h"
#include "ext/fmt.h"
#include "unordered_map"

using namespace std;
using namespace cpp_algo::topics;
using namespace cpp_algo::ext::fmt;



int main() {
    auto result = Arrays::minTransfers({{0,1,10},{2,0,5}});
    cout << result << endl;
}
