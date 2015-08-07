N= int (input())
for i in range(0, N):
    
    F, B, T, FD, BD = map(int, input().split())

    current = 0
    time = 0
    
    if F == B and F > FD:
        print("No Ditch")

    elif F > B:
        while current != FD:
            print("W", FD, current, current - FD, time)
            if (current + F) < FD:
                print("I", FD, current, current - FD, time)
                current = current + (F - B)
                time = time + ((F + B) * T)
            else:
                print("E1", FD, current, current - FD, time)
                time = time - ((current - FD) * T)
                current = FD
        print(time, "F")
    
    else:
        while current != BD:
            print("W2", BD, current, current - BD, current + F - B, time)
            if (current + (F - B)) > (-BD):
                print("I", BD, current, current - BD, time)
                current = current + (F - B)
                time = time + ((F + B) * T)
            else:
                print("E2", FD, current, current + BD, time)
                print( ( ( (current + BD) + (B - (current + BD) + B) ) * T) )
                time = time + (( (current + BD) + F) * T)
                current = BD
        print(time, "B")
