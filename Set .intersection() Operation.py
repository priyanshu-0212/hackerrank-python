n = int(input())
set_a = set(map(int, input().split()))

m = int(input())
set_b = set(map(int, input().split()))

common_set  = set_a.intersection(set_b)
print(len(common_set))
