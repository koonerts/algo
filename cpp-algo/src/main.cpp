#include <iostream>
#include <vector>
#include "topics/arrays-and-strings/arrays.h"
#include "ext/fmt.h"


using namespace std;
using namespace cpp_algo::ext::fmt;

auto main() -> int {
    vector<vector<int>> intervals{{1,2},{3,5},{6,7},{8,10},{12,16}};
    vector<int> ni{4,8};
    auto res = cpp_algo::arrays::insertInterval(intervals, ni);
    println(res);
}

