//
// Created by koonerts on 5/29/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include "../src/arrays-and-strings/arrays.h"


TEST_CASE("is_valid_subsequence") {
    Arrays arr{};
    CHECK(arr.isValidSubsequence({5, 1, 22, 25, 6, -1, 8, 10}, {1, 6, -1, 10}));
    CHECK_FALSE(arr.isValidSubsequence({1, 2, 3}, {1, 2, 2}));
}

TEST_CASE("sorted_squared_array") {
    Arrays arr{};
    CHECK(arr.sortedSquaredArray({1, 2, 3}) == std::vector<int>{1, 4, 9});
    CHECK(arr.sortedSquaredArray({-4, -2, 0, 1, 2, 3}) == std::vector<int>{0, 1, 4, 4, 9, 16});
}

