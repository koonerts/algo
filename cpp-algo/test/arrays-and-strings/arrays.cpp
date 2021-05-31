//
// Created by koonerts on 5/31/21.
//

#include <catch2/catch.hpp>
#include "../../src/arrays-and-strings/arrays.h"


TEST_CASE("isValidSubsequence") {
    Arrays arr{};
    CHECK(arr.isValidSubsequence({5, 1, 22, 25, 6, -1, 8, 10}, {1, 6, -1, 10}));
    CHECK_FALSE(arr.isValidSubsequence({1, 2, 3}, {1, 2, 2}));
}

TEST_CASE("sortedSquaredArray") {
    Arrays arr{};
    CHECK(arr.sortedSquaredArray({1, 2, 3}) == std::vector<int>{1, 4, 9});
    CHECK(arr.sortedSquaredArray({-4, -2, 0, 1, 2, 3}) == std::vector<int>{0, 1, 4, 4, 9, 16});
}


TEST_CASE("smallestDifference") {
    Arrays arr{};
    CHECK(arr.smallestDifference({-1, 5, 10, 20, 28, 3}, {26, 134, 135, 15, 17}) == std::vector<int>{28, 26});
}
