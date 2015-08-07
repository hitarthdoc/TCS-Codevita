N = int(input())
A = []

for i in range(0, N):
    A.append(int(input()))
    
X = int(input())

result = False

for i in range(0,N):

    for j in range(0,(N-1)):
        
        for k in range(0,(N-2)):
            if (A[i]+A[j]+A[k])==X and i != k and i != j and j != k:
                result = True
print(result)
