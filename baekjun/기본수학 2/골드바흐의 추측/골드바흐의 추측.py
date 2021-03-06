import sys
import math

def solution(N):
    check = [True] * (N)

    # N까지 소수목록 생성
    for i in range(2, int(N**0.5)+1):
        for j in range(i+i,N,i):
            if check[i]:
                check[j] = False

    Prime = [i for i in range(2,N) if check[i]]

    #골드바흐
    for i in range(int(len(Prime)*0.5)+1,-1,-1):
        for j in range(len(Prime)-1,i,-1):
            if Prime[i] == N - Prime[j] and i < j: 
                return Prime[i], Prime[j]

times = int(sys.stdin.readline())
for _ in range(times):
    N = int(sys.stdin.readline())
    answer = solution(N)
    print(f'{answer[0]} {answer[1]}')
