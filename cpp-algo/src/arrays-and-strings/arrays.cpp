//
// Created by koonerts on 5/30/21.
//

#include "arrays.h"
#include <unordered_set>
#include <set>


namespace cpp_algo::arrays {
    enum class TraversalDirection {
        Up, Down, Left, Right
    };

    auto twoNumberSum(const std::vector<int> &vec, int targetSum) -> std::vector<int> {
        std::unordered_set<int> numSet{};
        for (int num : vec) {
            if (numSet.contains(targetSum - num)) {
                return {num, targetSum - num};
            }
            numSet.insert(num);
        }
        return {};
    }

    auto isValidSubsequence(const std::vector<int> &vec, const std::vector<int> &seq) -> bool {
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

    auto sortedSquaredArray(const std::vector<int> &vec) -> std::vector<int> {
        if (vec.empty())
            return {};

        auto binary_search_negative = [&vec]() {
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

    auto smallestDifference(std::vector<int> vec1, std::vector<int> vec2) -> std::vector<int> {
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

    auto moveElementToEnd(std::vector<int> vec, int toMove) -> std::vector<int> {
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

    auto isMonotonic(const std::vector<int> &vec) -> bool {
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

    auto spiralTraverse(const std::vector<std::vector<int>> &vec) -> std::vector<int> {
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
            }
        }

        return rVec;
    }

    auto fourNumberSum(std::vector<int> vec, int targetSum) -> std::vector<std::vector<int>> {
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

    auto subarraySort(const std::vector<int> &vec) -> std::vector<int> {
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

    auto largestRange(const std::vector<int> &vec) -> std::vector<int> {
        std::set<int> vSet{vec.begin(), vec.end()};
        auto curr{vSet.begin()}, prev{vSet.begin()}, rangeBegin{vSet.begin()};
        std::vector<int> rVec{*prev, *prev};
        size_t maxRange{1};
        ++curr;

        while (curr != vSet.cend()) {
            if (*curr != *prev + 1) {
                rangeBegin = curr;
            }

            size_t currRange = std::distance(rangeBegin, curr) + 1;
            if (currRange > maxRange) {
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
    auto minRewards(const std::vector<int> &scores) -> int {
        return -1;
    }

// TODO
    auto zigzagTraverse(const std::vector<std::vector<int>> &array) -> std::vector<int> {
        // Write your code here.
        return {};
    }
}

