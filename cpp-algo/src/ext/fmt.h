//
// Created by koonerts on 6/5/21.
//

#ifndef CPP_ALGO_FMT_H
#define CPP_ALGO_FMT_H

#include <vector>
#include <iostream>

namespace cpp_algo::ext::fmt {

    template<typename T, typename A>
    auto println(const std::vector<T, A> &v) -> void {
        std::cout << "[";
        for (auto &n : v) {
            std::cout << n;
            auto idx = &n - &v[0];
            if (idx < v.size() - 1)
                std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }

}

#endif //CPP_ALGO_FMT_H
