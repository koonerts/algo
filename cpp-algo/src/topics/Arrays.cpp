//
// Created by koonerts on 5/30/21.
//


#include "Arrays.h"
#include <unordered_set>
#include <set>
#include <numeric>
#include <unordered_map>


namespace cpp_algo::topics {
    enum class TraversalDirection {
        Up, Down, Left, Right
    };

    auto Arrays::twoNumberSum(const std::vector<int> &vec, int targetSum) -> std::vector<int> {
        std::unordered_set<int> numSet{};
        for (int num : vec) {
            if (numSet.contains(targetSum - num)) {
                return {num, targetSum - num};
            }
            numSet.insert(num);
        }
        return {};
    }

    auto Arrays::isValidSubsequence(const std::vector<int> &vec, const std::vector<int> &seq) -> bool {
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

    auto Arrays::sortedSquaredArray(const std::vector<int> &vec) -> std::vector<int> {
        if (vec.empty())
            return {};

        auto binary_search_negative = [&vec]() {
            int negIdx{-1}, lo{}, hi{static_cast<int>(vec.size() - 1)};
            while (lo <= hi) {
                int mid = std::midpoint(lo, hi);
                if (vec.at(mid) < 0) {
                    negIdx = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            return negIdx;
        };

        std::vector<int> rVec{};
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

    auto Arrays::smallestDifference(std::vector<int> vec1, std::vector<int> vec2) -> std::vector<int> {
        auto n1 = vec1.size(), n2 = vec2.size();
        sort(vec1.begin(), vec1.end());
        sort(vec2.begin(), vec2.end());

        if (vec1[n1 - 1] <= vec2[0]) {
            return {vec1[n1 - 1], vec2[0]};
        } else if (vec1[0] >= vec2[n2 - 1]) {
            return {vec1[0], vec2[n2 - 1]};
        }

        std::vector<int> rVec{-1, -1};
        auto minDiff = std::numeric_limits<int>::max();

        for (auto p1 = vec1.begin(), p2 = vec2.begin(); p1 != vec1.end() || p2 != vec2.end();) {
            auto v1_val = p1 != vec1.end() ? *p1 : *(p1 - 1);
            auto v2_val = p2 != vec2.end() ? *p2 : *(p2 - 1);
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

    auto Arrays::moveElementToEnd(std::vector<int> vec, int toMove) -> std::vector<int> {
        if (vec.empty())
            return vec;

        for (size_t lo = 0, hi = vec.size() - 1; lo < hi;) {
            if (vec[lo] != toMove) {
                ++lo;
                continue;
            }

            std::swap(vec[lo], vec[hi]);
            --hi;
        }
        return vec;
    }

    auto Arrays::isMonotonic(const std::vector<int> &vec) -> bool {
        if (vec.size() <= 1)
            return true;

        auto vIter = vec.begin() + 1;
        while (vIter != vec.end() && *vIter == *(vIter - 1))
            ++vIter;

        if (vIter == vec.end())
            return true;

        bool is_increasing = *vIter > *(vIter - 1);
        while (vIter != vec.end()) {
            if (is_increasing && *vIter < *(vIter - 1))
                return false;
            if (!is_increasing && *vIter > *(vIter - 1))
                return false;
            ++vIter;
        }
        return true;
    }

    auto Arrays::spiralTraverse(const std::vector<std::vector<int>> &vec) -> std::vector<int> {
        if (vec.empty())
            return {};

        auto dir = TraversalDirection::Right;
        size_t m{vec.size()}, n{vec[0].size()};
        size_t x{}, y{}, left_y{}, right_y{n - 1}, top_x{}, bot_x{m - 1};
        size_t total{n * m};
        std::vector<int> rVec{};
        rVec.reserve(total);

        while (rVec.size() < total) {
            switch (dir) {
                case TraversalDirection::Right:
                    while (true) {
                        rVec.push_back(vec[x][y]);
                        if (y == right_y) {
                            ++top_x;
                            ++x;
                            dir = TraversalDirection::Down;
                            break;
                        }
                        ++y;
                    }
                    break;
                case TraversalDirection::Down:
                    while (true) {
                        rVec.push_back(vec[x][y]);
                        if (x == bot_x) {
                            --right_y;
                            --y;
                            dir = TraversalDirection::Left;
                            break;
                        }
                        ++x;
                    }
                    break;
                case TraversalDirection::Left:
                    while (true) {
                        rVec.push_back(vec[x][y]);
                        if (y == left_y) {
                            --bot_x;
                            --x;
                            dir = TraversalDirection::Up;
                            break;
                        }
                        --y;
                    }
                    break;
                case TraversalDirection::Up:
                    while (true) {
                        rVec.push_back(vec[x][y]);
                        if (x == top_x) {
                            ++left_y;
                            ++y;
                            dir = TraversalDirection::Right;
                            break;
                        }
                        --x;
                    }
                    break;
                default:
                    throw std::invalid_argument("Invalid TraversalDirection.");
            }
        }

        return rVec;
    }

    auto Arrays::fourNumberSum(std::vector<int> vec, int targetSum) -> std::vector<std::vector<int>> {
        if (vec.size() < 4)
            return {};

        std::vector<std::vector<int>> rVec;
        std::sort(vec.begin(), vec.end());
        for (size_t i = 0; i < vec.size() - 3; ++i) {
            for (size_t j = i + 1; j < vec.size() - 2; ++j) {
                size_t k{j + 1}, l{vec.size() - 1};

                while (k < l) {
                    int sum = vec[i] + vec[j] + vec[k] + vec[l];

                    if (sum == targetSum) {
                        rVec.push_back({vec[i], vec[j], vec[k], vec[l]});
                        ++k, --l;
                    } else if (sum < targetSum) {
                        ++k;
                    } else {
                        --l;
                    }
                }
            }
        }

        return rVec;
    }

    auto Arrays::subarraySort(const std::vector<int> &vec) -> std::vector<int> {
        if (vec.size() <= 1)
            return {-1, -1};

        size_t lo{}, hi{vec.size() - 1};
        while (lo < hi && (vec[lo] <= vec[lo + 1] || vec[hi] >= vec[hi - 1])) {
            if (vec[lo] <= vec[lo + 1])
                ++lo;
            if (vec[hi] >= vec[hi - 1])
                --hi;
        }

        if (lo >= hi)
            return {-1, -1};

        auto min{std::numeric_limits<int>::max()}, max{std::numeric_limits<int>::min()};
        while (lo <= hi) {
            min = std::min(min, vec[lo]);
            max = std::max(max, vec[lo]);
            ++lo;
        }

        lo = 0, hi = vec.size() - 1;
        while (lo < hi && (vec[lo] <= min || vec[hi] >= max)) {
            if (vec[lo] <= min)
                ++lo;
            if (vec[hi] >= max)
                --hi;
        }

        return {static_cast<int>(lo), static_cast<int>(hi)};
    }

    auto Arrays::largestRange(const std::vector<int> &vec) -> std::vector<int> {
        std::set<int> vSet{vec.begin(), vec.end()};
        auto curr{vSet.begin()}, prev{vSet.begin()}, rangeBegin{vSet.begin()};
        std::vector<int> rVec{*prev, *prev};
        size_t maxRange{1};
        ++curr;

        while (curr != vSet.cend()) {
            if (*curr != *prev + 1) {
                rangeBegin = curr;
            }

            if (size_t currRange = std::distance(rangeBegin, curr) + 1;
                    currRange > maxRange) {
                rVec[0] = *rangeBegin;
                rVec[1] = *curr;
                maxRange = currRange;
            }
            prev = curr;
            ++curr;
        }

        return rVec;
    }

    // TODO
    auto Arrays::minRewards(const std::vector<int> &scores) -> int {
        return -1;
    }

    // TODO
    auto Arrays::zigzagTraverse(const std::vector<std::vector<int>> &array) -> std::vector<int> {
        // Write your code here.
        return {};
    }


    auto Arrays::lengthOfLongestSubstring(std::string s) -> int {
        if (s.size() <= 1)
            return static_cast<int>(s.size());

        int lo{};
        int maxLen{};
        std::vector<int> charIdxMap(256, -1);

        for (auto const &c : s) {
            if (charIdxMap[c] >= lo) {
                lo = charIdxMap[c] + 1;
            }
            auto idx = static_cast<int>(&c - &s[0]);
            charIdxMap[c] = idx;
            maxLen = std::max(maxLen, idx - lo + 1);
        }
        return maxLen;
    }

    auto Arrays::nextPermutation(std::vector<int> &nums) -> void {
        if (nums.size() <= 1)
            return;

        auto firstDecreasingIter = nums.rbegin() + 1;
        while (firstDecreasingIter != nums.rend() && *firstDecreasingIter >= *(firstDecreasingIter - 1))
            ++firstDecreasingIter;

        if (firstDecreasingIter == nums.rend()) {
            std::sort(nums.begin(), nums.end());
            return;
        }

        auto iter = firstDecreasingIter.base();
        while (iter != nums.end()) {
            if (*iter > *firstDecreasingIter && (iter + 1 == nums.end() || *(iter + 1) <= *firstDecreasingIter))
                break;
            ++iter;
        }

        std::iter_swap(firstDecreasingIter, iter);
        std::reverse(firstDecreasingIter.base(), nums.end());
    }

    // TODO
    auto Arrays::nextClosestTime(std::string time) -> std::string {
        return "";
    }

    auto Arrays::insertInterval(std::vector<std::vector<int>> &intervals, std::vector<int> &newInterval) -> std::vector<std::vector<int>> {
        std::vector<std::vector<int>> retIntervals;

        if (intervals.empty()) {
            retIntervals.push_back(newInterval);
            return retIntervals;
        }

        auto idx = 0;
        while (idx < intervals.size() && intervals[idx][1] < newInterval[0]) {
            retIntervals.push_back(intervals[idx]);
            idx++;
        }

        auto is_overlapping = [&intervals, &newInterval, &idx]() {
            return idx < intervals.size() && (
                    (newInterval[0] >= intervals[idx][0] && newInterval[0] <= intervals[idx][1]) ||
                    (newInterval[1] >= intervals[idx][0] && newInterval[1] <= intervals[idx][1]) ||
                    (intervals[idx][0] >= newInterval[0] && intervals[idx][0] <= newInterval[1]) ||
                    (intervals[idx][1] >= newInterval[0] && intervals[idx][1] <= newInterval[1])
            );
        };

        while (is_overlapping()) {
            newInterval[0] = std::min(newInterval[0], intervals[idx][0]);
            newInterval[1] = std::max(newInterval[1], intervals[idx][1]);
            ++idx;
        }

        retIntervals.push_back(newInterval);
        while (idx < intervals.size()) {
            retIntervals.push_back(intervals[idx]);
            ++idx;
        }

        return retIntervals;
    }

    auto Arrays::maxArea(std::vector<int> &heights) -> int {
        return -1;
    }

    auto Arrays::tandemBicycle(std::vector<int> redShirtSpeeds, std::vector<int> blueShirtSpeeds, bool fastest) -> int {
        return -1;
    }
}