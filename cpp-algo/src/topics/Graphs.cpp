//
// Created by koonerts on 6/9/21.
//

#include "Graphs.h"
namespace cpp_algo::topics {

TreeNode* invertTree(TreeNode* root) {
    if (root == nullptr) {
        return nullptr;
    }
    TreeNode* left = invertTree(root->left);
    TreeNode* right = invertTree(root->right);
    root->left = right;
    root->right = left;
    return root;
}

}  // namespace cpp_algo::ents