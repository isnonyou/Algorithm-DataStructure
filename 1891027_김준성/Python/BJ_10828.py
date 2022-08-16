def push(stack, num):
    stack.append(int(num))
    return stack

def pop(stack):
    if len(stack) < 1:
        print(-1)
    else:
        print(stack.pop())
    return stack
    
def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack) < 1:
        print(1)
    else:
        print(0)

def top(stack):
    if(len(stack) < 1):
        print(-1)
    else:
        print(stack[len(stack)-1])

i = int(input())
num = 0
stack = []

order = []
for _ in range(0, i):
    order.append(input().split(" "))

for o in order:
    if o[0] == "push":
        stack = push(stack, int(o[1]))
    elif o[0] == "pop":
        stack = pop(stack)
    elif o[0] == "size":
        size(stack)
    elif o[0] == "empty":
        empty(stack)
    else:
        top(stack)


# for _ in range(0, i):
#     order = input().split(" ")
#     if order[0] == "push":
#         stack = push(stack, int(order[1]))
#     elif order[0] == "pop":
#         stack = pop(stack)
#     elif order[0] == "size":
#         size(stack)
#     elif order[0] == "empty":
#         empty(stack)
#     else:
#         top(stack)