#Python

n = int(input())
arr = [int(x) for x in input().split()]
target = int(input())
nums = {}
flag = False
for i in range(n):
    diff = target - arr[i]
    if diff in nums:
        print(diff,arr[i])
        flag = True
        break
    else:
        nums[arr[i]] = arr[i]
if flag == False:
    print(-1)
