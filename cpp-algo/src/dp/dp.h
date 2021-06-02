//
// Created by koonerts on 6/1/21.
//

#ifndef CPP_ALGO_DP_H
#define CPP_ALGO_DP_H

#include <vector>

namespace cpp_algo::dp {

    int
    min_cost_paint_houses_memoized(std::vector<std::vector<int>>& costs);

    int
    min_cost_paint_houses_tabulated(std::vector<std::vector<int>>& costs);

}

#endif //CPP_ALGO_DP_H
