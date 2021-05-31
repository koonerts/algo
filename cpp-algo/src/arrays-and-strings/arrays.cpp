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
            rVec.push_back(val * val);
            ++posIdx;
        } else {
            int val{vec.at(negIdx)};
            rVec.push_back(val * val);
            --negIdx;
        }
    }
    return rVec;
}

vector<int> Arrays::smallestDifference(vector<int> vec1, vector<int> vec2) {
    auto n1 = vec1.size(), n2 = vec2.size();
    sort(vec1.begin(), vec1.end());
    sort(vec2.begin(), vec2.end());

    if (vec1[n1 - 1] <= vec2[0]) {
        return {vec1[n1 - 1], vec2[0]};
    } else if (vec1[0] >= vec2[n2 - 1]) {
        return {vec1[0], vec2[n2 - 1]};
    }

    vector<int> rVec{-1,-1};
    auto minDiff = numeric_limits<int>::max();

    for(auto p1 = vec1.begin(), p2 = vec2.begin(); p1 != vec1.end() || p2 != vec2.end();) {
        auto v1_val = p1 != vec1.end() ? *p1 : *(p1-1);
        auto v2_val = p2 != vec2.end() ? *p2 : *(p2-1);
        auto diff = abs(v1_val - v2_val);

        if (diff < minDiff)
            rVec[0] = v1_val, rVec[1] = v2_val, minDiff = diff;
        auto is_valid = p1 != vec1.end() && p2 != vec2.end();
        if (p2 == vec2.end() || (is_valid && *p1 < *p2))
            ++p1;
        else
            ++p2;
    }
    return rVec;
}
