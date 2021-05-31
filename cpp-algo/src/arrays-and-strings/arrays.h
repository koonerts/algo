//
// Created by koonerts on 5/30/21.
//

#ifndef CPP_ALGO_ARRAYS_H
#define CPP_ALGO_ARRAYS_H

#include <vector>

struct Arrays {
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
    spiralTraverse(const std::vector<std::vector<int>>& array);
};

#endif //CPP_ALGO_ARRAYS_H
