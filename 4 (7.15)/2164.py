'''
N = int(input())
M = []
tmp = 0

for i in range(1, N+1):
    M.append(i)

while len(M) > 2:
    X = len(M)
    del M[0]
    tmp = M[0]
    del M[0]
    M.append(tmp)
del M[0]

print(M[0])
'''
# 리스트 형태로 존재하면 시간이 오래걸림
N = int(input())
n = 0

if N == 1:
    print(N)
if N > 1:
    while 2 ** n < N:
        n = n + 1
    ans = (N - 2 ** (n - 1)) * 2
    print(ans)
