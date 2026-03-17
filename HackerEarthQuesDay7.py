""" 
Q.1 
L = int(input())
N = int(input())

for i in range(N):
    W, H = map(int, input().split())
    
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")     
------------------------------------------
Q.2
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    K = K % N   # important (edge case)
    
    result = arr[-K:] + arr[:-K]
    
    print(*result)
--------------------------------------------     
        
"""