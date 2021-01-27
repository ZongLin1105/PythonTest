a = [int(i) for i in input().split()] 
count = 0
for i in range(1,len(a)-1): #不計算最後一個
    if a[i] > a[i-1] and a[i] > a[i+1]:
        count += 1
print(count)

# a = [int(s) for s in input().split()]
# counter = 0
# for i in range(1, len(a) - 1):
#   if a[i - 1] < a[i] > a[i + 1]:
#     counter += 1
# print(counter)