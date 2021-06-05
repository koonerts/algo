#include <iostream>
#include <vector>
// #include <future>
#include "traits/traits.h"
#include "arrays-and-strings/arrays.h"

using namespace std;
using namespace cpp_algo::traits;

template<typename T>
auto printVec(const vector<T> &v) {
    cout << "[";
    for (auto &n : v) {
        cout << n;
        auto idx = &n - &v[0];
        if (idx < v.size()-1)
            cout << ", ";
    }
    cout << "]" << endl;
}

auto main() -> int {
    vector<int> v{1,3,2};
    cpp_algo::arrays::nextPermutation(v);
    printVec(v);
}

