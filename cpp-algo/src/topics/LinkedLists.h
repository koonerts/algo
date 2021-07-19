//
// Created by koonerts on 6/12/21.
//

#ifndef CPP_ALGO_LINKEDLISTS_H
#define CPP_ALGO_LINKEDLISTS_H


#include <vector>
#include <memory>
#include "../ents/ListNode.h"


namespace cpp_algo::topics {
    auto createLinkedList(std::vector<int> nums) -> cpp_algo::ents::ListNode *;
    auto reverseKGroup(cpp_algo::ents::ListNode *head, int k) -> cpp_algo::ents::ListNode *;
}


#endif //CPP_ALGO_LINKEDLISTS_H
