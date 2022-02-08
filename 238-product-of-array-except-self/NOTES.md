product = 1
res = []
for i, num in enumerate(nums):
res.append(product)
product = product * nums[i]
#print(res)
product = 1
for i in range(len(nums)-1, -1, -1):
res[i] *= product
product *= nums[i]
print(res, product)
return res