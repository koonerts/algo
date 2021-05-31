//
// Created by koonerts on 5/30/21.
//

#include "arrays.h"
#include <unordered_set>

using namespace std;

vector<int> twoNumberSum(const vector<int>& vec, int targetSum) {
    unordered_set<int> numSet{};
    for (int num : vec) {
        if (numSet.contains(targetSum-num)) {
            return {num, targetSum-num};
        }
        numSet.insert(num);
    }
    return {};
}

bool isValidSubsequence(const vector<int> &vec, const vector<int> &seq) {
    if (seq.size() > vec.size())
        return false;

    auto seqItr = seq.begin();
    for (int n : vec) {
        if (n == *seqItr)
            ++seqItr;
        if (seqItr == seq.end())
            return true;
    }
    return false;
}

