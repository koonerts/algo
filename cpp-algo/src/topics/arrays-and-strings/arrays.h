//
// Created by koonerts on 5/30/21.
//

#ifndef CPP_ALGO_ARRAYS_H
#define CPP_ALGO_ARRAYS_H

#include <vector>
#include <string>

namespace cpp_algo::arrays {
    auto twoNumberSum(const std::vector<int> &vec, int targetSum) -> std::vector<int>;

    auto isValidSubsequence(const std::vector<int> &vec, const std::vector<int> &seq) -> bool;

    auto sortedSquaredArray(const std::vector<int> &vec) -> std::vector<int>;

    auto smallestDifference(std::vector<int> vec1, std::vector<int> vec2) -> std::vector<int>;

    auto moveElementToEnd(std::vector<int> vec, int toMove) -> std::vector<int>;

    auto isMonotonic(const std::vector<int> &vec) -> bool;

    auto spiralTraverse(const std::vector<std::vector<int>> &vec) -> std::vector<int>;

    auto fourNumberSum(std::vector<int> vec, int targetSum) -> std::vector<std::vector<int>>;

    auto subarraySort(const std::vector<int> &vec) -> std::vector<int>;

    auto largestRange(const std::vector<int> &vec) -> std::vector<int>;

    auto minRewards(const std::vector<int> &scores) -> int;

    auto zigzagTraverse(const std::vector<std::vector<int>> &array) -> std::vector<int>;

    auto lengthOfLongestSubstring(std::string s) -> int;

    auto nextPermutation(std::vector<int> &nums) -> void;

    auto nextClosestTime(std::string time) -> std::string;

    auto insertInterval(std::vector<std::vector<int>>& intervals, std::vector<int>& newInterval) -> std::vector<std::vector<int>>;

}

#endif //CPP_ALGO_ARRAYS_H
