# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Breadth First Search----
"""
In this approach, we maintain a stack of two element-- current node and depth of that node from root
While stack is not empty, we pop the element from stack. If currentNode have a left element, append
currentNode and depth+1 to stack so that we can check for left and right elements of this node as well
Similar for the right element. After that if currentNode doesn't have left and right element, add depth
to the set. Finally return max of this set. This tuple stores depths of each leaf.
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        stack = [[root,1]]
        maxDepth = set()
        while(stack):
            currentNode, depth = stack.pop()
            if currentNode.left:
                stack.append([currentNode.left,depth+1])
            if currentNode.right:
                stack.append([currentNode.right,depth+1])
            if currentNode.left==None and currentNode.right==None:
                maxDepth.add(depth)
        return max(maxDepth)

# Recursive Solution----
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

# Another BFS Approach----
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        nodes = [root]
        depth = 0   
        temp = []
        while nodes:
            for node in nodes:
                if node != None:
                    temp.extend([node.left,node.right])
            nodes = temp
            temp = []
            depth += 1
        return depth-1