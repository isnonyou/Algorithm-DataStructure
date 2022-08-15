import sys
n = int(sys.stdin.readline())
xy = []

for i in range(n):
    [x,y] = map(int, input().split())
    xy.append([x,y])

answer = sorted(xy)

for i in range(n):
    print(answer[i][0], answer[i][1])
