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

        std::vector<int> buildHeap(std::vector<int> &vector);

        void siftDown(int currentIdx, int endIdx, std::vector<int> &heap);

        void siftUp(int currentIdx, std::vector<int> &heap);

        int peek();

        int remove();

        void insert(int value);

    private:
        std::vector<int> _heap;
    };
}

#endif //CPP_ALGO_MIN_HEAP_H
