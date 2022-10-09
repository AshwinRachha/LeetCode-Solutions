dic = {}
def dfs1(root):
nonlocal dic
if root:
dic[root.val] = target - root.val
if root.left:
dfs1(root.left)
if root.right:
dfs1(root.right)
dfs1(root1)
def dfs2(root):
if not root:
return False
else:
val = root.val
if target - val in dic:
return True
return dfs2(root.left) or dfs2(root.right)
return dfs2(root2)