# 메모리 제한 문제를 어떻게 해결해야할까?
# C언어를 사용하면 되겠지만 용량이 큰 파이썬 같은 경우에는 어떻게 정리래야할까
# sys에 대한 공부가 필요
import sys
input = sys.stdin.readline

N = int(input())
# 리스트의 개수를 제한
X = [0] * 10001

# 이 문제의 경우에는 "계수 정렬"을 사용해야함
#각 입력값에 해당하는 인덱스의 값을 증가시킴.
for _ in range(N):
    X[int(input())] += 1

# 기록된 인덱스 값에 따라서 순차적으로 출력
for i in range(len(X)):
    if X[i] != 0:
        for _ in range(X[i]):
            print(i)
