dic = {}
count = 0
prefixSum = 0
dic[0] = 1
for i, num in enumerate(nums):
prefixSum += num
if prefixSum - k in dic:
count += dic[prefixSum-k]
dic[prefixSum] = dic.get(prefixSum, 0) + 1
return count