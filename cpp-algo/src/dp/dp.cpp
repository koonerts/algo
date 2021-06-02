//
// Created by koonerts on 6/1/21.
//

#include "dp.h"
#include <functional>
#include <map>

namespace cpp_algo::dp {

    template<typename T1, typename T2>
    struct Pair {
        Pair(int x, int y) : x{x}, y{y} {}

        bool operator==(const Pair &p) const {
            return x == p.x && y == p.y;
        }

        T1 x;
        T2 y;
    };

    struct hash_fn
    {
        template <class T1, class T2>
        size_t operator() (const Pair<T1, T2> &pair) const
        {
            size_t h1 = std::hash<T1>()(pair.x);
            size_t h2 = std::hash<T2>()(pair.y);
            return h1 ^ h2;
        }
    };

    int
    min_cost_paint_houses_memoized(std::vector<std::vector<int>> &costs) {
        std::unordered_map<Pair<int, int>, int, hash_fn> memo{};

        std::function<int(const int, const int)> findMinCost;
        findMinCost = [&](const int idx, const int color) -> int {
            Pair<int, int> p{idx, color};
            if (memo.contains(p)) {
                return memo[p];
            }

            int cost = costs[idx][(int)color];
            if (idx == costs.size()-1) {
                // pass
            } else if (color == 0) {
                cost += std::min(findMinCost(idx + 1, 1), findMinCost(idx + 1, 2));
            } else if (color == 1) {
                cost += std::min(findMinCost(idx+1, 0), findMinCost(idx+1, 2));
            } else {
                cost += std::min(findMinCost(idx+1, 0), findMinCost(idx+1, 1));
            }

            memo[p] = cost;
            return cost;
        };
        auto min1 = std::min(findMinCost(0, 0), findMinCost(0, 1));
        return std::min(min1, findMinCost(0, 2));
    }

    int
    min_cost_paint_houses_tabulated(std::vector<std::vector<int>> &costs) {

        return 0;
    }

}
