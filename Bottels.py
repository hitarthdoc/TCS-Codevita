N = int(input())
if N >= 3:

    A = []
    flag = False

    for i in range(0, N):
        A.append(int(input()))
        if A[i] > 0:
            flag = True
    
    if flag==False:
        X = int(input())

        if X >0:
            result = False

            for i in range(0,N):

                for j in range(0,(N-1)):
                    
                    for k in range(0,(N-2)):
                        if A[i]+A[j]+A[k]==X and i != k and i != j and j != k:
                            result = True
            print(result)
