#Python

arr = int(input())
nums = [int(x) for x in input().split()]
ele = int(input())
if ele in nums:
    nums.remove(ele)

for num in nums:
    print(num,end = " ")
