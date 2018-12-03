package LeetCode;

class Solution_951 {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        int ll = root1.left == null ? 100 : root1.left.val;
        int lr = root1.right == null ? 100 : root1.right.val;
        int rl = root2 == null ? 100 : root2.left.val;
        int rr = root2 == null ? 100 : root2.right.val;

        if (ll != rr || lr != rl) return false;
        if (ll != 100) {
            if (!flipEquiv(root1.left, root2.right)) return false;
        }
        if (lr != 100) {
            if (!flipEquiv(root1.right, root2.left)) return false;
        }

        return true;
    }
    //TODO: not exactly adhering to problem statement
}
