//
// Created by koonerts on 5/29/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>

uint Factorial(uint number) {
    return number > 1 ? Factorial(number - 1) * number : 1;
}

TEST_CASE("factorials_are_correct", "[factorial]") {
    CHECK(Factorial(0) == 1);
    CHECK(Factorial(1) == 1);
    CHECK(Factorial(2) == 2);
    CHECK(Factorial(3) == 6);
    CHECK(Factorial(10) == 3628800);
}

