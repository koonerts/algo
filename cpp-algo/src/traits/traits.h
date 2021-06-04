//
// Created by koonerts on 6/4/21.
//

#ifndef CPP_ALGO_TRAITS_H
#define CPP_ALGO_TRAITS_H

#include "is_iterable.h"
namespace cpp_algo::traits {
    template <typename T>
    constexpr bool is_iterable_v = is_iterable<T>::value;
}

#endif //CPP_ALGO_TRAITS_H
