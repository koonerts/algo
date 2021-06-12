//
// Created by koonerts on 5/31/21.
//

#include <catch2/catch.hpp>
#include "../../src/topics/arrays-and-strings/arrays.h"

using namespace cpp_algo::arrays;

TEST_CASE("isValidSubsequence") {
    CHECK(isValidSubsequence({5, 1, 22, 25, 6, -1, 8, 10}, {1, 6, -1, 10}));
    CHECK_FALSE(isValidSubsequence({1, 2, 3}, {1, 2, 2}));
}

TEST_CASE("sortedSquaredArray") {
    CHECK(sortedSquaredArray({1, 2, 3}) == std::vector<int>{1, 4, 9});
    CHECK(sortedSquaredArray({-4, -2, 0, 1, 2, 3}) == std::vector<int>{0, 1, 4, 4, 9, 16});
}

TEST_CASE("smallestDifference") {
    CHECK(smallestDifference({-1, 5, 10, 20, 28, 3}, {26, 134, 135, 15, 17}) == std::vector<int>{28, 26});
}

TEST_CASE("moveElementToEnd") {
    auto result{moveElementToEnd({2, 1, 2, 2, 2, 3, 4, 2}, 2)};
    auto is_valid{result == std::vector<int>{1, 3, 4, 2, 2, 2, 2, 2} || result == std::vector<int>{4, 1, 3, 2, 2, 2, 2, 2}};
    CHECK(is_valid);
}

TEST_CASE("spiralTraverse") {
    std::vector<std::vector<int>> matrix = {{4,  2,  3,  6,  7,  8,  1,  9,  5,  10},
                                            {12, 19, 15, 16, 20, 18, 13, 17, 11, 14}};
    CHECK(spiralTraverse(matrix) == std::vector<int>{4, 2, 3, 6, 7, 8, 1, 9, 5, 10, 14, 11, 17, 13, 18, 20, 16, 15, 19, 12});
}

TEST_CASE("fourNumberSum") {
    CHECK(fourNumberSum({7, 6, 4, -1, 1, 2}, 16) == std::vector<std::vector<int>>{{-1, 4, 6, 7},
                                                                                  {1,  2, 6, 7}});
}

TEST_CASE("subarraySort") {
    CHECK(subarraySort({1, 2}) == std::vector<int>{-1, -1});
    CHECK(subarraySort({1, 2, 3}) == std::vector<int>{-1, -1});
    CHECK(subarraySort({1, 2, 3, 4}) == std::vector<int>{-1, -1});
    CHECK(subarraySort({2, 1}) == std::vector<int>{0, 1});
    CHECK(subarraySort({1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19}) == std::vector<int>{3, 9});
    CHECK(subarraySort({1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19}) == std::vector<int>{4, 9});
}

TEST_CASE("largestRange") {
    CHECK(largestRange({1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6}) == std::vector<int>{0, 7});
}

TEST_CASE("insertInterval") {
    std::vector<std::vector<int>> intervals{{1,  2},
                                            {3,  5},
                                            {6,  7},
                                            {8,  10},
                                            {12, 16}};
    std::vector<int> newInterval{4, 8};
    CHECK(insertInterval(intervals, newInterval) == std::vector<std::vector<int>>{{1,  2},
                                                                                  {3,  10},
                                                                                  {12, 16}});
}