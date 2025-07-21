num = int(input())
nums = [int(x) for x in input().split()]
key = int(input())
if key in nums:
    print(nums.index(key))
else:
    print(-1)
