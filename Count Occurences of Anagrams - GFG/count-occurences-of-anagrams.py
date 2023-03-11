#User function Template for python3
from collections import Counter
class Solution:

	
	def search(self,pat, txt):
	    # code here
	    # f - 1, o - 1, r - 1 (len - 3)
	    # Sliding window of length (len(pat)) and roll it over txt and check if the frequency array matches.
	    # If the frequency array matches then we increment count and move on
	    # when we move on, we maintain the start poiner and the next pointer, we decrement count for start pointer 
	    # because we have moved forward by 1 and we increment the element at next pointer.
	    
	    m, n = len(pat), len(txt)
	    count1 = Counter(pat)
	    count2 = Counter(txt[:m])
	    #print(count1, count2)
	    ans = 0
	    
	    for i in range(n - m + 1):
	        if count1 == count2:
	            ans += 1
	        # We will decrement entry i from count2 and increment entry i + m
	        count2[txt[i]] -= 1
	        if count2[txt[i]] == 0:
	            del count2[txt[i]]
	        if i + m < n:
	            count2[txt[i+m]] += 1
	   
	       
	    
	    return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends