for i in range(len(nums)):
if nums[i] == 0:
nums[i] = -1
dic = {0:-1}
largest = 0
prefixSum = 0
for i in range(len(nums)):
prefixSum += nums[i]
if prefixSum in dic:
index_2_ignore = dic[prefixSum]
largest = max(largest, i - index_2_ignore)
else:
dic[prefixSum] = i
return largest