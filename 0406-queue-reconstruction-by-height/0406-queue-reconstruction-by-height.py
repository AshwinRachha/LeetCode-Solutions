class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        """
        [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        [5, 0], 
        """
        
        people.sort(key = lambda x : (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
        