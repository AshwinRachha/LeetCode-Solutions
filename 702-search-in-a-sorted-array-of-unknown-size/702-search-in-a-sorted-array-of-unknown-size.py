# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        start = 0
        end = 10000
        
        while start <= end:
            
            mid = (end + start) >> 1
            
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) == 2147483647 or reader.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1