def findNumbers(nums, target):
    for i in range(len(nums)): #first element will be summed up with the rest of elements each, 2nd element will be summed up with rest of elemets each
       for j in range(i+1,len(nums)): #element to be summed with first element
         if nums[i] + nums[j] == target:
           return [i,j]
# write your implementation here
    return None

print(findNumbers([2,7,11,15],9))
print(findNumbers([3,2,4],6))
print(findNumbers([3,3],6))

