import sys

N, K = map(int, sys.stdin.readline().split())
A = []

for i in range(N):
    A.append(int(sys.stdin.readline()))
count = 0

# 뒤에서부터 찾지 않으면 너무 오랜 시간이 걸리는 것같기도하고
# while문은 사용했는데 시간초과가 발생했다.

A.sort(reverse=True)

for i in A:
    if K >= i:
        count = count + (K // i)
        K = K % i
        if K <= 0:
            break
print(count)


