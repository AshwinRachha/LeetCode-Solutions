class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        changes = target[0]
        for i in range(1, len(target)):
            changes += max(0, target[i]-target[i-1])
        return changes