len1, len2 = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

differ1 = set(list1) - set(list2)
differ2 = set(list2) - set(list1)

result = len(differ1) + len(differ2)
print(result)
