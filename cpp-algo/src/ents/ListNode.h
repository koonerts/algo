//
// Created by koonerts on 6/12/21.
//

#ifndef CPP_ALGO_LISTNODE_H
#define CPP_ALGO_LISTNODE_H



namespace cpp_algo::ents {
    struct ListNode {
        int val;
        ListNode *next;

        ListNode() : val{}, next{nullptr} {}
        explicit ListNode(int val) : val{val}, next{nullptr} {}
        ListNode(int val, ListNode *next) : val{val}, next{next} {}

        ListNode(const ListNode &) = default;
        ListNode &operator=(const ListNode &) = default;
        ListNode(ListNode &&) noexcept = default;
        ListNode &operator=(ListNode &&) noexcept = default;

        ~ListNode() {
            delete next;
        }
    };
}


#endif //CPP_ALGO_LISTNODE_H
