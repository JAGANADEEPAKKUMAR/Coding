#Python

n = int(input())
nums = list(map(int,input().split()))
if len(nums) <= 20:
    mean = sum(nums)/len(nums)
    print("{:.2f}".format(mean))


#Java
