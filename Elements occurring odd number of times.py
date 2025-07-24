#Python

num = int(input())
nums = [int(x) for x in input().split()]
odd_freq = []
for n in nums:
    if nums.count(n) % 2 != 0:
        odd_freq.append(n)
odd_freq = list(set(odd_freq))
odd_freq.sort()
if len(odd_freq) > 1:
    for i in odd_freq:
        print(i,end = " ")
else:
    print(-1)
