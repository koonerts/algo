//
// Created by koonerts on 6/5/21.
//

#include "fmt.h"

namespace cpp_algo::ext::fmt {
    auto println(const ListNode &head) -> void {
        std::cout << head.val;
        auto node = head.next;

        while (node) {
            std::cout << "->" << node->val;
            node = node->next;
        }
        std::cout << std::endl;
    }
}