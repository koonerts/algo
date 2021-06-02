//
// Created by koonerts on 5/30/21.
//

#ifndef CPP_ALGO_ARRAYS_H
#define CPP_ALGO_ARRAYS_H

#include <vector>

struct Arrays {
    enum class TraversalDirection {
        Up, Down, Left, Right
    };

    static std::vector<int>
    twoNumberSum(const std::vector<int> &vec, int targetSum);

    static bool
    isValidSubsequence(const std::vector<int> &vec, const std::vector<int> &seq);

    static std::vector<int>
    sortedSquaredArray(const std::vector<int> &vec);

    static std::vector<int>
    smallestDifference(std::vector<int> vec1, std::vector<int> vec2);

    static std::vector<int>
    moveElementToEnd(std::vector<int> vec, int toMove);

    static bool
    isMonotonic(const std::vector<int> &vec);

    static std::vector<int>
    spiralTraverse(const std::vector<std::vector<int>> &vec);

    static std::vector<std::vector<int>>
    fourNumberSum(std::vector<int> vec, int targetSum);

    static std::vector<int>
    subarraySort(const std::vector<int> &vec);

    static std::vector<int>
    largestRange(const std::vector<int>& vec);

    static int
    minRewards(const std::vector<int> &scores);
};

#endif //CPP_ALGO_ARRAYS_H
