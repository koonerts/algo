//
// Created by koonerts on 6/4/21.
//

#ifndef CPP_ALGO_IS_ITERABLE_H
#define CPP_ALGO_IS_ITERABLE_H

namespace cpp_algo::traits {
    template<typename T, typename = std::void_t<>>
    struct is_iterable : std::false_type {};

    template<typename T>
    struct is_iterable<T, std::void_t<decltype(std::declval<T>().begin(), std::declval<T>().end())>> : std::true_type {};
}

#endif //CPP_ALGO_IS_ITERABLE_H
