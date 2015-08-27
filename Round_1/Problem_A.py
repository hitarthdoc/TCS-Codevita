N= int (input())

for i in range(0, N):
    
    F, B, T, FD, BD = map(int, input().split())

    current = 0
    time = 0
    
    if F == B and F < FD:
        print("No Ditch")

    elif F >= B:
        while current != FD:
            if (current + F) < FD:
                current = current + (F - B)
                time = time + ((F + B) * T)
            else:
                time = time - ((current - FD) * T)
                current = FD
        print(time, "F")
        # ans[i] = str(time) + " F"
    
    else:
        while current != BD:
            if (current + (F - B)) > (-BD):
                current = current + (F - B)
                time = time + ((F + B) * T)
            else:
                time = time + ((F + B + (BD - (B - ( current + F)))) *T)
                current = BD
        print(time, "B")
        # ans[i] = str(time) + " B"

# for i in range(0, (len(ans))):
#     print(ans[i])
