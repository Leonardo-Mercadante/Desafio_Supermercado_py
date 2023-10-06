T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    if K > N:
        print(N)
    else:
        print((N % K) + (N // K))
