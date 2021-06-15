//
// Created by koonerts on 6/12/21.
//

#ifndef CPP_ALGO_LINKED_LISTS_H
#define CPP_ALGO_LINKED_LISTS_H


#include <vector>
#include <memory>
#include "list_node.h"


namespace cpp_algo::linked_lists {
    auto createLinkedList(std::vector<int> nums) -> ListNode *;
    auto reverseKGroup(ListNode *head, int k) -> ListNode *;
}


#endif //CPP_ALGO_LINKED_LISTS_H
