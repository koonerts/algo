//
// Created by koonerts on 6/12/21.
//


#include <cstddef>
#include <memory>
#include "linked_lists.h"


namespace cpp_algo::linked_lists {
    auto reverseKGroup(ListNode *head, int k) -> ListNode * {
        if (k == 0)
            return head;


        ListNode *prev_tail{head}, *prev{}, *curr{head};

        size_t i{};
        while (curr) {
            if (i > 0 && i % k == 0) {
                prev_tail->next = curr;
                prev_tail = curr;
                prev = curr;
                auto tmp = curr->next;
                curr->next = nullptr;
                curr = tmp;
            } else {
                auto tmp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = tmp;
            }

            ++i;
        }

        return nullptr;
    }

    auto createLinkedList(std::vector<int> nums) -> ListNode * {
        ListNode *head{nullptr};
        ListNode *prev{nullptr};
        for (auto n : nums) {
            auto curr = new ListNode{n};
            if (!head) head = curr;
            if (prev) prev->next = curr;
            prev = curr;
        }
        return head;
    }
}
