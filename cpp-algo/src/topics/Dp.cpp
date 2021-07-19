//
// Created by koonerts on 6/1/21.
//

#include "Dp.h"
#include <functional>
#include <unordered_map>

namespace cpp_algo::topics {

    template<typename T1, typename T2>
    struct Pair {
        Pair(T1 x, T2 y) : m_x{x}, m_y{y} {}
        Pair<T1, T2>(const Pair<T1, T2> &) = default;
        Pair<T1, T2>(Pair<T1, T2> &&) noexcept = default;
        Pair<T1, T2> &operator=(Pair<T1, T2> &&) noexcept = default;
        Pair<T1, T2> &operator=(const Pair<T1, T2> &) = default;


        auto operator==(const Pair &p) const -> bool {
            return m_x == p.m_x && m_y == p.m_y;
        }

        T1 m_x;
        T2 m_y;
    };

    struct pair_hash_fn {
        template<class T1, class T2>
        auto operator()(const Pair<T1, T2> &pair) const -> size_t {
            size_t h1 = std::hash<T1>()(pair.m_x);
            size_t h2 = std::hash<T2>()(pair.m_y);
            return h1 ^ h2;
        }
    };

    auto min_cost_paint_houses_memoized(std::vector<std::vector<int>> &costs) -> int {
        std::unordered_map<Pair<int, int>, int, pair_hash_fn> memo{};

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

    auto min_cost_paint_houses_tabulated(std::vector<std::vector<int>> &costs) -> int {
        return 0;
    }

}
