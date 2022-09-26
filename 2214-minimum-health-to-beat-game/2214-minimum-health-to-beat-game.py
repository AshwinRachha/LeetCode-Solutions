class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        maximum, health = float('-inf'), 1
        for i, n in enumerate(damage):
            health += n
            maximum = max(maximum, n)
        to_sub = min(maximum , armor)
        health -= to_sub
        return health
        