class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        health = 1
        maximum = float('-inf')
        for num in damage:
            health += num
            maximum = max(maximum, num)
        health -= min(armor, maximum)
        return health