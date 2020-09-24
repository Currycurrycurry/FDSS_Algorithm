# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        inorder_list = inorder(root)
        if not inorder_list or len(inorder_list) == 0:
            return []
        cur_num = 1
        max_num = 1
        res = [inorder_list[0]]
        for i in range(1, len(inorder_list)):
            if inorder_list[i] == inorder_list[i-1]:
                cur_num += 1
            else:
                cur_num = 1
            if cur_num == max_num:
                res.append(inorder_list[i])
            elif cur_num > max_num:
                res = [inorder_list[i]]
                max_num = cur_num
        return res

    # wrong reason: pass by value and pass by inference
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        def findInorderMode(root, cur_num, max_num, pre):
            if not root:
                return
            findInorderMode(root.left, cur_num, max_num, pre)
            if pre:
                if root.val == pre.val:
                    cur_num += 1
                else:
                    cur_num = 1
            nonlocal res
            if cur_num == max_num:
                res.append(root.val)
            elif cur_num > max_num:
                res = [root.val]
                max_num = cur_num
            pre = root
            findInorderMode(root.right, cur_num, max_num, pre)
        findInorderMode(root, 1, 0, None)
        return res
    
    # correct
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        max_num = 0
        cur_num = 1
        pre = None
        if not root:
            return res
        def findInorderMode(root):
            if not root:
                return
            findInorderMode(root.left)
            nonlocal res, max_num, cur_num, pre
            if pre:
                if root.val == pre.val:
                    cur_num += 1
                else:
                    cur_num = 1
            if cur_num == max_num:
                res.append(root.val)
            elif cur_num > max_num:
                res = [root.val]
                max_num = cur_num
            pre = root
            findInorderMode(root.right)
        findInorderMode(root)
        return res

    def findMode(self, root: TreeNode) -> List[int]:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        ans = []
        cnt, max_cnt, last = 0, 0, None
        for v in inorder(root):
            if v == last:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                ans = [v]
            elif cnt == max_cnt:
                ans.append(v)
            max_cnt = max(max_cnt, cnt)
            last = v
        return ans

