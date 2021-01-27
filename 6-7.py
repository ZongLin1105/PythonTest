a = eval(input())
i = 0
sum = 0
while (a != 0):
    i += 1 
    sum += a
    a = eval(input())
print("%.2f" % (sum/i))  #小數點後2位