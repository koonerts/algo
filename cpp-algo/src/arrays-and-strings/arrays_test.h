//
// Created by koonerts on 5/30/21.
//

#ifndef CPP_ALGO_ARRAYS_TEST_H
#define CPP_ALGO_ARRAYS_TEST_H

#include <vector>

namespace cpp_algo::arrays {
    enum class TraversalDirection {
        Up, Down, Left, Right
    };

    std::vector<int>
    twoNumberSum(const std::vector<int> &vec, int targetSum);

    bool
    isValidSubsequence(const std::vector<int> &vec, const std::vector<int> &seq);

    std::vector<int>
    sortedSquaredArray(const std::vector<int> &vec);

    std::vector<int>
    smallestDifference(std::vector<int> vec1, std::vector<int> vec2);

    std::vector<int>
    moveElementToEnd(std::vector<int> vec, int toMove);

    bool
    isMonotonic(const std::vector<int> &vec);

    std::vector<int>
    spiralTraverse(const std::vector<std::vector<int>> &vec);

    std::vector<std::vector<int>>
    fourNumberSum(std::vector<int> vec, int targetSum);

    std::vector<int>
    subarraySort(const std::vector<int> &vec);

    std::vector<int>
    largestRange(const std::vector<int>& vec);

    int
    minRewards(const std::vector<int> &scores);

    std::vector<int>
    zigzagTraverse(const std::vector<std::vector<int>>& array);
}

#endif //CPP_ALGO_ARRAYS_TEST_H
