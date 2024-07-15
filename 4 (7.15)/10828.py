'''
N = int(input())
stack = []
store = []
for i in range(N):
    store.append(input())

def push(X):
    stack.append(X)

def pop():
    if len(stack) == 0:
        print(-1)
    print(stack[0])
    del stack[0]

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0
'''
# input 함수를 사용할 경우 시간초과 에러가 뜸, 입출력 속도 비교 -> sys.stdin.readline > raw_input() > input()
# 각자 쓰는 경우가 다를까? 그 경우는 무슨 경우일까?

import sys

N = int(sys.stdin.readline())
stack=[]

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

# 이렇게 C언어의 strcmp같이 문자가 맞는지 안맞는지 확인하면서 코딩을 해야할까? 아니면 명령어 형식으로 만들면 안되나?

