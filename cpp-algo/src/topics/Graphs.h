//
// Created by koonerts on 6/9/21.
//

#ifndef CPP_ALGO_GRAPHS_H
#define CPP_ALGO_GRAPHS_H

#include <string>
#include <vector>

namespace cpp_algo::topics
{

    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };

    auto ladderLength(std::string beginWord, std::string endWord, std::vector<std::string> &wordList) -> int;
    auto invertTree(TreeNode* root) -> TreeNode*;
};

#endif //CPP_ALGO_GRAPHS_H
