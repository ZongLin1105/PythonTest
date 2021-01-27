n = eval(input())
m = eval(input())
a =[["."] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            a[i][j]="*"
for row in a:
    print(*row)