N = int(raw_input())
if N >= 3:

    S = []

    for i in range(0, N):
        S.append(int(raw_input()))

    X = int(raw_input())

    result = False

    for i in range(0,N):

        for j in range(0,(N-1)):
            
            for k in range(0,(N-2)):
                if S[i]+S[j]+S[k]==X and i != k and i != j and j != k:
                    result = True
                
    print result
