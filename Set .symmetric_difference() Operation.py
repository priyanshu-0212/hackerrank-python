n = int(input())
set_a = set(map(int, input().split()))

m = int(input())
set_b = set(map(int, input().split()))

uncommon_set = set_a.symmetric_difference(set_b)
print(len(uncommon_set))
