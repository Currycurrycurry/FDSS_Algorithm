// Definition for a binary tree node.

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
    TreeNode(int x) : val(x), left(NULL), right(NULL), parent(NULL) {}
};

class Solution {
public:
    TreeNode* getNextNode(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        TreeNode* pNext = nullptr;
        if (root->right != nullptr) {
            TreeNode* pRight = root->right;
            while (pRight->left != nullptr) {
                pRight = pRight->left;
            }
            pNext = pRight;
        }
        else if (root->parent != nullptr) {
            TreeNode* pCurrent = root;
            TreeNode* pParent = root->parent;
            while (pParent != nullptr && pCurrent == pParent -> right) {
                pCurrent = pParent;
                pParent = pParent->parent;
            }
            pNext = pParent;
        }
        return pNext;


    }
};

int main() {
    Solution solution = Solution();
    solution.getNextNode(nullptr);
}