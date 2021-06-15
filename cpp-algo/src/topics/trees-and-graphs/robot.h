//
// Created by koone on 6/12/2021.
//

#ifndef CPP_ALGO_ROBOT_H
#define CPP_ALGO_ROBOT_H

namespace cpp_algo::trees_and_graphs {
    struct Robot {
    public:
        // Returns true if the cell in front is open and robot moves into the cell.
        // Returns false if the cell in front is blocked and robot stays in the current cell.
        auto move() -> bool;

        // Robot will stay in the same cell after calling turnLeft/turnRight.
        // Each turn will be 90 degrees.
        auto turnLeft() -> void;
        auto turnRight() -> void;

        // Clean the current cell.
        auto clean() -> void;

        auto cleanRoom(Robot &robot) -> void;
    };
}

#endif //CPP_ALGO_ROBOT_H
