N= int (input())
for i in range(0, N):
    
    F, B, T, FD, BD = map(int, input().split())

    current = 0
    time = 0
    
    if F == B and F > FD:
        print("No Ditch")

    elif F > B:
        while current != FD:
            if (current + F) < FD:
                current += (F - B)
                time = (F + B) * T
            else:
                current = current + (F - (current - FD))
                time = (F - (current - FD)) * T
        print(time, "F")
    
    else:
        while current != BD:
            if B > (current - BD):
                current += (F - B)
                time = (F + B) * T
            else:
                current = current + (F - B + (current - BD))
                time = (F - B + (current - FD)) * T
        print(time, "B")
