longest_sequence = 0
for left in range(len(nums)):
num_zeros = 0
for right in range(left, len(nums)):
if num_zeros == 2:
break
if nums[right] == 0:
num_zeros += 1
if num_zeros <= 1:
longest_sequence = max(longest_sequence, right - left + 1)
return longest_sequence