#Python

num = int(input())
nums = [int(x) for x in input().split()]
unique = []
for n in nums:
    if nums.count(n) == 1:
        unique.append(n)
unique.sort()
for i in unique:
    print(i,end=" ")
