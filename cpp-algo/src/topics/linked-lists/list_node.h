//
// Created by koonerts on 6/12/21.
//

#ifndef CPP_ALGO_LIST_NODE_H
#define CPP_ALGO_LIST_NODE_H



namespace cpp_algo::linked_lists {
    struct ListNode {
        int val;
        ListNode *next;

        ListNode() : val{}, next{nullptr} {}
        ListNode(int val) : val{val}, next{nullptr} {}
        ListNode(int val, ListNode *next) : val{val}, next{nullptr} {}

        auto print() -> void;

        ~ListNode() {
            delete next;
        }
    };
}


#endif //CPP_ALGO_LIST_NODE_H
