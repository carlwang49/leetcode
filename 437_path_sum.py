from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        stack = [root]
        self.count = 0
        self.targetSum = targetSum
        
        while stack:
            top = stack.pop()
            if top.left:
                stack.insert(0, top.left)
            if top.right:
                stack.insert(0, top.right)
            self.traverse(curr=top, summ=0)
        
        return self.count

    def traverse(self, curr: TreeNode, summ: int):
        if curr is None:
            return
        curr_val = curr.val
        summ += curr_val
        if self.targetSum == summ:
            self.count += 1
        self.traverse(curr.left, summ)
        self.traverse(curr.right, summ)


class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        self.count = 0
        self.targetSum = targetSum
        self.prefix_sum_map = defaultdict(int)
        self.traverse(root, 0)
        return self.count

    def traverse(self, curr: TreeNode, summ):
        if not curr:
            return 
        curr_val = curr.val
        summ += curr_val
        if summ == self.targetSum:
            self.count += 1
        if self.prefix_sum_map.get(summ-self.targetSum):
            self.count += self.prefix_sum_map[summ-self.targetSum]
        self.prefix_sum_map[summ] += 1
        self.traverse(curr.left, summ)
        self.traverse(curr.right, summ)
        self.prefix_sum_map[summ] -= 1

        
        
            
            