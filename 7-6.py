a = [int(i) for i in input().split()] 
#print(len(set(a)))
b = []
count = 0
for i in a:
    if i not in b:
        b.append(i)
        count += 1
print(count)
print(b)
# num_distinct = 1
# a = [int(s) for s in input().split()]
# for i in range(1, len(a)):
#   if a[i - 1] != a[i]:
#     num_distinct += 1
# print(num_distinct)
