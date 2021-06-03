//
// Created by koone on 6/2/2021.
//

#ifndef CPP_ALGO_MIN_HEAP_H
#define CPP_ALGO_MIN_HEAP_H

#include <vector>

namespace cpp_algo::containers {
    template <typename T>
    struct min_heap {

        min_heap(std::vector<int> vector) {
            _heap = buildHeap(vector);
        }

        auto buildHeap(std::vector<int> &vector) -> std::vector<int>;

        auto siftDown(int currentIdx, int endIdx, std::vector<int> &heap) -> void;

        auto siftUp(int currentIdx, std::vector<int> &heap) -> void;

        auto peek() -> int;

        auto remove() -> int;

        auto insert(int value) -> void;

    private:
        std::vector<int> _heap;
    };
}

#endif //CPP_ALGO_MIN_HEAP_H
