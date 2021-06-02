//
// Created by koonerts on 6/1/21.
//

#include <catch2/catch.hpp>
#include "../../src/dp/dp.h"

using namespace cpp_algo::dp;

TEST_CASE("min_cost_paint_houses_memoized") {
    std::vector<std::vector<int>> costs{{17,2,17},{16,16,5},{14,3,19}};
    CHECK(min_cost_paint_houses_memoized(costs) == 10);
}