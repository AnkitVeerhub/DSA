#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

// Binary Tree Node Definition
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Top View Function
vector<int> topView(TreeNode* root) {
    if (!root) return {};

    map<int, int> top_view; // horizontal distance -> node value
    queue<pair<TreeNode*, int>> q; // node, horizontal distance

    q.push({root, 0});

    while (!q.empty()) {
        auto [node, hd] = q.front();
        q.pop();

        if (top_view.find(hd) == top_view.end()) {
            top_view[hd] = node->val;
        }

        if (node->left) q.push({node->left, hd - 1});
        if (node->right) q.push({node->right, hd + 1});
    }

    vector<int> result;
    for (auto& [hd, val] : top_view) {
        result.push_back(val);
    }

    return result;
}

// Main Function with Example Input
int main() {
    /*
         1
        / \
       2   3
        \
         4
          \
           5
            \
             6
    */
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->left->right->right = new TreeNode(5);
    root->left->right->right->right = new TreeNode(6);

    vector<int> view = topView(root);

    cout << "Top View of the Binary Tree: ";
    for (int val : view) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
