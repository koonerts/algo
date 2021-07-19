//
// Created by koonerts on 5/30/21.
//

#ifndef CPP_ALGO_ARRAYS_H
#define CPP_ALGO_ARRAYS_H

#include <vector>
#include <string>

namespace cpp_algo::topics {
    struct Arrays {
        static auto twoNumberSum(const std::vector<int> &vec, int targetSum) -> std::vector<int>;

        static auto isValidSubsequence(const std::vector<int> &vec, const std::vector<int> &seq) -> bool;

        static auto sortedSquaredArray(const std::vector<int> &vec) -> std::vector<int>;

        static auto smallestDifference(std::vector<int> vec1, std::vector<int> vec2) -> std::vector<int>;

        static auto moveElementToEnd(std::vector<int> vec, int toMove) -> std::vector<int>;

        static auto isMonotonic(const std::vector<int> &vec) -> bool;

        static auto spiralTraverse(const std::vector<std::vector<int>> &vec) -> std::vector<int>;

        static auto fourNumberSum(std::vector<int> vec, int targetSum) -> std::vector<std::vector<int>>;

        static auto subarraySort(const std::vector<int> &vec) -> std::vector<int>;

        static auto largestRange(const std::vector<int> &vec) -> std::vector<int>;

        static auto minRewards(const std::vector<int> &scores) -> int;

        static auto zigzagTraverse(const std::vector<std::vector<int>> &array) -> std::vector<int>;

        static auto lengthOfLongestSubstring(std::string s) -> int;

        static auto nextPermutation(std::vector<int> &nums) -> void;

        static auto nextClosestTime(std::string time) -> std::string;

        static auto insertInterval(std::vector<std::vector<int>>& intervals, std::vector<int>& newInterval) -> std::vector<std::vector<int>>;

        static auto maxArea(std::vector<int>& height) -> int;

        static auto tandemBicycle(std::vector<int> redShirtSpeeds, std::vector<int> blueShirtSpeeds, bool fastest) -> int;
    };
}

#endif //CPP_ALGO_ARRAYS_H
