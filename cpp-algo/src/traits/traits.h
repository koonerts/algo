//
// Created by koonerts on 6/4/21.
//

#ifndef CPP_ALGO_TRAITS_H
#define CPP_ALGO_TRAITS_H

namespace cpp_algo::traits {
    template<typename T, typename = std::void_t<>>
    struct is_iterable : std::false_type {};

    template<typename T>
    struct is_iterable<T, std::void_t<decltype(std::declval<T>().begin(), std::declval<T>().end())>> : std::true_type {};

    template <typename T>
    constexpr bool is_iterable_v = is_iterable<T>::value;

    template<typename>
    struct is_vector : std::false_type {};

    template<typename T, typename A>
    struct is_vector<std::vector<T,A>> : std::true_type {};

    template<typename T>
    constexpr bool is_vector_v = is_vector<T>::value;
}

#endif //CPP_ALGO_TRAITS_H
