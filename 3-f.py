x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
if abs(x1-x2) + abs(y1-y2) == 1 or abs(x1-x2) * abs(y1-y2) == 1:
    print("YES")
else:
    print("NO") 