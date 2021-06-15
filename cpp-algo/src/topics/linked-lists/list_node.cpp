//
// Created by koonerts on 6/12/21.
//

#include <iostream>
#include "list_node.h"


namespace cpp_algo::linked_lists {
    auto ListNode::print() -> void {
        std::cout << val;
        auto node = next;

        while (node) {
            std::cout << node->val;
            if (node->next)
                std::cout << "->";
            node = node->next;
        }
        std::cout << std::endl;
    }
}