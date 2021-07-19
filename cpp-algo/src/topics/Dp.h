//
// Created by koonerts on 6/1/21.
//

#ifndef CPP_ALGO_DP_H
#define CPP_ALGO_DP_H

#include <vector>

namespace cpp_algo::topics {

    auto min_cost_paint_houses_memoized(std::vector<std::vector<int>>& costs) -> int;

    auto min_cost_paint_houses_tabulated(std::vector<std::vector<int>>& costs) -> int;

}

#endif //CPP_ALGO_DP_H
