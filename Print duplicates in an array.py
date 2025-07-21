#Python

num = int(input())
nums = [int(x) for x in input().split()]
duplicates = []
for n in nums:
    if nums.count(n) > 1:
        duplicates.append(n)
duplicate = list(set(duplicates))
duplicate.sort()
for i in duplicate:
    print(i,end=" ")
