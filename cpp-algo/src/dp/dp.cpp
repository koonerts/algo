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

    struct hash_fn {
        template<class T1, class T2>
        size_t operator()(const Pair<T1, T2> &pair) const {
            size_t h1 = std::hash<T1>()(pair.x);
            size_t h2 = std::hash<T2>()(pair.y);
            return h1 ^ h2;
        }
    };

    int
    min_cost_paint_houses_memoized(std::vector<std::vector<int>> &costs) {
        std::unordered_map<Pair<int, int>, int, hash_fn> memo{};

        const auto findMinCost = [&costs, &memo](const int idx, const int color) {
            auto findMinCostImpl = [&costs, &memo](const int idx, const int color, auto &findMinCostRef) {
                Pair<int, int> p{idx, color};
                if (memo.contains(p)) {
                    return memo[p];
                }

                int cost = costs[idx][(int) color];
                if (idx == costs.size() - 1) {
                    // pass
                } else if (color == 0) {
                    cost += std::min(findMinCostRef(idx + 1, 1, findMinCostRef), findMinCostRef(idx + 1, 2, findMinCostRef));
                } else if (color == 1) {
                    cost += std::min(findMinCostRef(idx + 1, 0, findMinCostRef), findMinCostRef(idx + 1, 2, findMinCostRef));
                } else {
                    cost += std::min(findMinCostRef(idx + 1, 0, findMinCostRef), findMinCostRef(idx + 1, 1, findMinCostRef));
                }

                memo[p] = cost;
                return cost;
            };
            return findMinCostImpl(idx, color, findMinCostImpl);
        };

        return std::min({findMinCost(0, 0), findMinCost(0, 1), findMinCost(0, 2)});
    }

    int
    min_cost_paint_houses_tabulated(std::vector<std::vector<int>> &costs) {

        return 0;
    }

}
