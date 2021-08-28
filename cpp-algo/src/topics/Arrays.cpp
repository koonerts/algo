//
// Created by koonerts on 5/30/21.
//


#include "Arrays.h"
#include <unordered_set>
#include <set>
#include <stack>
#include <numeric>
#include <unordered_map>
#include <queue>
#include "../ext/fmt.h"

using namespace std;
using namespace cpp_algo::ext::fmt;

namespace cpp_algo::topics {

    enum class TraversalDirection {
        Up, Down, Left, Right
    };

    auto Arrays::twoNumberSum(const vector<int> &vec, int targetSum) -> vector<int> {
        unordered_set<int> numSet{};
        for (int num: vec) {
            if (numSet.contains(targetSum - num)) {
                return {num, targetSum - num};
            }
            numSet.insert(num);
        }
        return {};
    }

    auto Arrays::isValidSubsequence(const vector<int> &vec, const vector<int> &seq) -> bool {
        if (seq.size() > vec.size())
            return false;

        auto seqItr = seq.begin();
        for (int n: vec) {
            if (n == *seqItr)
                ++seqItr;
            if (seqItr == seq.end())
                return true;
        }
        return false;
    }

    auto Arrays::sortedSquaredArray(const vector<int> &vec) -> vector<int> {
        if (vec.empty())
            return {};

        auto binary_search_negative = [&vec]() {
            int negIdx{-1}, lo{}, hi{static_cast<int>(vec.size() - 1)};
            while (lo <= hi) {
                int mid = midpoint(lo, hi);
                if (vec.at(mid) < 0) {
                    negIdx = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            return negIdx;
        };

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

    auto Arrays::smallestDifference(vector<int> vec1, vector<int> vec2) -> vector<int> {
        auto n1 = vec1.size(), n2 = vec2.size();
        sort(vec1.begin(), vec1.end());
        sort(vec2.begin(), vec2.end());

        if (vec1[n1 - 1] <= vec2[0]) {
            return {vec1[n1 - 1], vec2[0]};
        } else if (vec1[0] >= vec2[n2 - 1]) {
            return {vec1[0], vec2[n2 - 1]};
        }

        vector<int> rVec{-1, -1};
        auto minDiff = numeric_limits<int>::max();

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

    auto Arrays::moveElementToEnd(vector<int> vec, int toMove) -> vector<int> {
        if (vec.empty())
            return vec;

        for (size_t lo = 0, hi = vec.size() - 1; lo < hi;) {
            if (vec[lo] != toMove) {
                ++lo;
                continue;
            }

            swap(vec[lo], vec[hi]);
            --hi;
        }
        return vec;
    }

    auto Arrays::isMonotonic(const vector<int> &vec) -> bool {
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

    auto Arrays::spiralTraverse(const vector<vector<int>> &vec) -> vector<int> {
        if (vec.empty())
            return {};

        auto dir = TraversalDirection::Right;
        size_t m{vec.size()}, n{vec[0].size()};
        size_t x{}, y{}, left_y{}, right_y{n - 1}, top_x{}, bot_x{m - 1};
        size_t total{n * m};
        vector<int> rVec{};
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
                    throw invalid_argument("Invalid TraversalDirection.");
            }
        }

        return rVec;
    }

    auto Arrays::fourNumberSum(vector<int> vec, int targetSum) -> vector<vector<int>> {
        if (vec.size() < 4)
            return {};

        vector<vector<int>> rVec;
        sort(vec.begin(), vec.end());
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

    auto Arrays::subarraySort(const vector<int> &vec) -> vector<int> {
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

        auto _min{numeric_limits<int>::max()}, _max{numeric_limits<int>::min()};
        while (lo <= hi) {
            _min = min(_min, vec[lo]);
            _max = max(_max, vec[lo]);
            ++lo;
        }

        lo = 0, hi = vec.size() - 1;
        while (lo < hi && (vec[lo] <= _min || vec[hi] >= _max)) {
            if (vec[lo] <= _min)
                ++lo;
            if (vec[hi] >= _max)
                --hi;
        }

        return {static_cast<int>(lo), static_cast<int>(hi)};
    }

    auto Arrays::largestRange(const vector<int> &vec) -> vector<int> {
        set<int> vSet{vec.begin(), vec.end()};
        auto curr{vSet.begin()}, prev{vSet.begin()}, rangeBegin{vSet.begin()};
        vector<int> rVec{*prev, *prev};
        size_t maxRange{1};
        ++curr;

        while (curr != vSet.cend()) {
            if (*curr != *prev + 1) {
                rangeBegin = curr;
            }

            if (size_t currRange = distance(rangeBegin, curr) + 1;
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
    auto Arrays::minRewards(const vector<int> &scores) -> int {
        return -1;
    }

    // TODO
    auto Arrays::zigzagTraverse(const vector<vector<int>> &array) -> vector<int> {
        // Write your code here.
        return {};
    }

    auto Arrays::lengthOfLongestSubstring(string s) -> int {
        if (s.size() <= 1)
            return static_cast<int>(s.size());

        int lo{};
        int maxLen{};
        vector<int> charIdxMap(256, -1);

        for (auto const &c: s) {
            if (charIdxMap[c] >= lo) {
                lo = charIdxMap[c] + 1;
            }
            auto idx = static_cast<int>(&c - &s[0]);
            charIdxMap[c] = idx;
            maxLen = max(maxLen, idx - lo + 1);
        }
        return maxLen;
    }

    auto Arrays::nextPermutation(vector<int> &nums) -> void {
        if (nums.size() <= 1)
            return;

        auto firstDecreasingIter = nums.rbegin() + 1;
        while (firstDecreasingIter != nums.rend() && *firstDecreasingIter >= *(firstDecreasingIter - 1))
            ++firstDecreasingIter;

        if (firstDecreasingIter == nums.rend()) {
            sort(nums.begin(), nums.end());
            return;
        }

        auto iter = firstDecreasingIter.base();
        while (iter != nums.end()) {
            if (*iter > *firstDecreasingIter && (iter + 1 == nums.end() || *(iter + 1) <= *firstDecreasingIter))
                break;
            ++iter;
        }

        iter_swap(firstDecreasingIter, iter);
        reverse(firstDecreasingIter.base(), nums.end());
    }

    // TODO
    auto Arrays::nextClosestTime(string time) -> string {
        return "";
    }

    auto Arrays::insertInterval(vector<vector<int>> &intervals, vector<int> &newInterval) -> vector<vector<int>> {
        vector<vector<int>> retIntervals;

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
            newInterval[0] = min(newInterval[0], intervals[idx][0]);
            newInterval[1] = max(newInterval[1], intervals[idx][1]);
            ++idx;
        }

        retIntervals.push_back(newInterval);
        while (idx < intervals.size()) {
            retIntervals.push_back(intervals[idx]);
            ++idx;
        }

        return retIntervals;
    }

    auto Arrays::maxArea(vector<int> &heights) -> int {
        return -1;
    }

    auto Arrays::tandemBicycle(vector<int> redShirtSpeeds, vector<int> blueShirtSpeeds, bool fastest) -> int {
        return -1;
    }

    auto Arrays::firstNonRepeatingCharacter(string str) -> int {
        vector<int> char_freqs(26, 0);
        vector<int> char_idx(26, 0);

        for (auto i = 0; i < str.size(); ++i) {
            ++char_freqs[str[i] - 'a'];
            char_idx[str[i] - 'a'] = i;
        }

        int minIdx = (1U << 31) - 1;
        for (auto i = 0; i < 26; ++i) {
            if (char_freqs[i] == 1)
                minIdx = min(minIdx, char_idx[i]);
        }

        if (minIdx == (1U << 31) - 1)
            minIdx = -1;

        return minIdx;
    }

    auto Arrays::mergeOverlappingIntervals(vector<vector<int>> &intervals) -> vector<vector<int>> {
        vector<vector<int>> ret_intervals{};
        if (intervals.empty())
            return ret_intervals;

        sort(intervals.begin(), intervals.end(), [](const auto &left, const auto &right) {
            return left[0] <= right[0];
        });

        ret_intervals.emplace_back(intervals[0]);
        for (auto i = 1; i < intervals.size(); ++i) {
            auto n = ret_intervals.size();
            if (intervals[i][0] > ret_intervals[n - 1][1]) {
                ret_intervals.emplace_back(intervals[i]);
            } else {
                ret_intervals[n - 1][1] = max(ret_intervals[n - 1][1], intervals[i][1]);
            }
        }

        return ret_intervals;
    }

    // TODO - https://www.algoexpert.io/questions/Sort%20Stack
    auto Arrays::sortStack(vector<int> stack) -> vector<int> {

        const auto sortStackRec = [&stack](optional<int> prevNum) {
            auto sortStackRecImpl = [&stack](optional<int> prevNum, auto &sortStackRecImplRef) {

            };
            sortStackRecImpl(prevNum, sortStackRecImpl);
        };
        sortStackRec({});
        return stack;
    }

    auto Arrays::multiply(string num1, string num2) -> string {
        if (num1.size() > num2.size())
            return Arrays::multiply(num2, num1);

        if (num1 == "0" || num2 == "0") return "0";
        else if (num1 == "1") return num2;
        else if (num2 == "1") return num1;

        const auto mlty = [](const char &c1, const char &c2) -> int {
            return (c1 - '0') * (c2 - '0');
        };

        auto add = [](const string &s1, const string &s2) -> string {
            auto n1 = s1.size(), n2 = s2.size();
            if (!n1) return s2;
            if (!n2) return s1;

            auto carry = 0;
            auto n = max(n1, n2);
            string result;
            result.reserve(n + 1);
            for (auto i = 0; i < n; ++i) {
                auto s1v = i >= n1 ? 0 : s1[i] - '0';
                auto s2v = i >= n2 ? 0 : s2[i] - '0';
                auto res = s1v + s2v + carry;
                carry = res / 10;
                result += to_string(res % 10);
            }

            if (carry > 0)
                result += "1";
            return result;
        };

        string result;
        for (auto n1_it = num1.crbegin(); n1_it != num1.crend(); ++n1_it) {
            int carry = 0;
            auto dst = distance(num1.crbegin(), n1_it);
            string ss;
            ss.reserve(num2.size() + dst + 1);

            if (dst > 0)
                ss += string(dst, '0');

            for (auto n2_it = num2.crbegin(); n2_it != num2.crend(); ++n2_it) {
                auto res = mlty(*n1_it, *n2_it) + carry;
                carry = res / 10;
                ss += to_string(res % 10);
            }

            if (carry > 0)
                ss += to_string(carry);
            result = add(result, ss);
        }

        reverse(result.begin(), result.end());
        return result;
    }

    // TODO - https://leetcode.com/explore/interview/card/google/59/array-and-strings/3052/
    auto Arrays::rotateMatrix(vector<vector<int>> &matrix) -> void {

    }

    // TODO - https://leetcode.com/explore/interview/card/google/59/array-and-strings/3061/
    auto Arrays::minCostToHireWorkers(vector<int> &quality, vector<int> &wage, int k) -> double {
        return 0;
    }

    auto Arrays::kClosestPoints(vector<vector<int>> &points, int k) -> vector<vector<int>> {
        const auto euclidean_dist = [](const vector<int> &point) {
            return sqrt(pow(point[0], 2) + pow(point[1], 2));
        };

        priority_queue<pair<double, vector<int>>> pq{};
        for (const auto &point: points) {
            auto dst = euclidean_dist(point);
            if (pq.size() < k) {
                pq.emplace(pair(dst, point));
            } else if (dst < pq.top().first) {
                pq.pop();
                pq.emplace(pair(dst, point));
            }
        }

        vector<vector<int>> rpoints;
        rpoints.reserve(k);
        while (!pq.empty()) {
            rpoints.emplace_back(pq.top().second);
            pq.pop();
        }
        return rpoints;
    }

    auto Arrays::maxAreaOfIsland(vector<std::vector<int>> &grid) -> int {
        size_t rows{grid.size()}, cols{grid[0].size()};
        int maxArea = 0;
        queue<pair<int, int>> que{};
        const vector<pair<int, int>> dirs{{1,  0},
                                          {0,  1},
                                          {-1, 0},
                                          {0,  -1}};

        for (int x = 0; x < rows; ++x) {
            for (int y = 0; y < cols; ++y) {
                if (grid[x][y] == 0)
                    continue;

                int area{0};
                grid[x][y] = 0;
                que.emplace(x, y);

                while (!que.empty()) {
                    ++area;
                    const auto[currX, currY] = que.front();
                    que.pop();
                    maxArea = max(maxArea, area);

                    for (const auto[dx, dy]: dirs) {
                        const int newX{currX + dx}, newY{currY + dy};
                        if (newX >= 0 && newY >= 0 && newX < rows && newY < cols && grid[newX][newY] == 1) {
                            grid[newX][newY] = 0;
                            que.emplace(newX, newY);
                        }
                    }
                }

            }
        }

        return maxArea;
    }

    auto Arrays::minTransfers(const vector<std::vector<int>> &transactions) -> int {
        vector<int> balances(22, 0);

        for (const auto &t : transactions) {
            balances[t[0]] -= t[3];
            balances[t[1]] += t[3];
        }

        auto minTransactions{numeric_limits<int>::max()};
        

        return 0;
    }
}