//
// Created by koonerts on 5/30/21.
//

#include "arrays.h"
#include <unordered_set>
#include <functional>

using namespace std;


vector<int> Arrays::twoNumberSum(const vector<int> &vec, int targetSum) {
    unordered_set<int> numSet{};
    for (int num : vec) {
        if (numSet.contains(targetSum - num)) {
            return {num, targetSum - num};
        }
        numSet.insert(num);
    }
    return {};
}

bool Arrays::isValidSubsequence(const vector<int> &vec, const vector<int> &seq) {
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

vector<int> Arrays::sortedSquaredArray(const vector<int> &vec) {
    if (vec.empty())
        return {};

    function<int()> binary_search_negative([&vec] {
        int negIdx{-1}, lo{}, hi{static_cast<int>(vec.size() - 1)};
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (vec.at(mid) < 0) {
                negIdx = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return negIdx;
    });

    vector<int> rVec{};
    rVec.reserve(vec.size());

    int negIdx{binary_search_negative()};
    int posIdx{negIdx + 1};
    size_t n{vec.size()};
    while (negIdx >= 0 || posIdx < n) {
        bool valid{negIdx >= 0 && posIdx < n};
        if ((valid && abs(vec.at(posIdx)) <= abs(vec.at(negIdx))) || negIdx < 0) {
            int val{vec.at(posIdx)};
            rVec.push_back(val*val);
            ++posIdx;
        } else {
            int val{vec.at(negIdx)};
            rVec.push_back(val*val);
            --negIdx;
        }
    }
    return rVec;
}

vector<int> Arrays::smallestDifference(const vector<int>& vec1, const vector<int>& vec2) {
    // Write your code here.
    return {};
}
