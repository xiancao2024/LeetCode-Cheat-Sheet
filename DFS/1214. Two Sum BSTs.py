# 1214. Two Sum BSTs
1214. Two Sum BSTs
'''
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:      
        if not root1 or not root2:
            return False
        
        def helper(root, result):
            if not root:
                return []
            helper(root.left, result)
            result.append(root.val)
            helper(root.right, result)
            return result
        
        ans1 = []
        lis1 = helper(root1, ans1)
        lis1.sort()
        ans2 = []
        lis2 = helper(root2, ans2)
        lis2.sort()

        left = 0
        right = len(lis2) -1
        while left < len(lis1) and right >= 0:
            summ = lis1[left] + lis2[right]
            if summ == target:
                return True
            elif summ > target:
                right -= 1
            else:
                left += 1
                
        return False 