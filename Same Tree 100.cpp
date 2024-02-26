// Binary Tree Node
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    bool isSameTree(TreeNode *p, TreeNode *q)
    {
        // Define the base cases for the recursion, if both p and q become NULL then it means that both the
        // binary trees are equal
        if (!p && !q)
            return true;
        // If either one becomes NULL before the other one then it means that the other tree still has elements
        // left to be recursed on, hence they wont be equal
        if (!p || !q)
            return false;
        // Compare the current node
        return p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};