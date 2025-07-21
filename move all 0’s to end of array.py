#Python

num = int(input())
nums = [int(x) for x in input().split()]
zeros_count = nums.count(0)
nums = [x for x in nums if x != 0]
zeros = zeros_count * [0]
modified = nums + zeros
for n in modified:
    print(n,end = " ")
