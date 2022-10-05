arr = [] # array
answer = 0

k = int(input())

for _ in range(k):
    num = int(input())
    if num != 0:
        arr.append(num)
    else:
        arr.pop()

#array안에 있는 수들을 하나씩 뽑아 더하는 함수
#for n in arr:  answer += n 를 써도 됨
n = 0
for _ in range(len(arr)):
    answer += arr[n]
    n +=1

print(answer)