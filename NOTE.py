from itertools import permutations

numbers = '17'
nums = set()

for i in range(1,len(numbers)):
    nums.update(map(int,list(permutations(numbers,i))))
print(nums)