#include <iostream>
#include <vector>
#include "topics/arrays-and-strings/arrays.h"
#include "topics/linked-lists/linked_lists.h"
#include "topics/linked-lists/list_node.h"
#include "ext/fmt.h"


using namespace std;
using namespace cpp_algo::ext::fmt;
using namespace cpp_algo::linked_lists;

auto main() -> int {
    ListNode *head = createLinkedList({1,2,3,4,5});
    head->print();
}

