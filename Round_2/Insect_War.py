def insect(lst, t):
    # print(t)
    ans = lst
    abc = []
    
    if t != 0:

        t = t - 1

        lst.sort()
        print("skdfhgshsekjrhnge", lst)


        xy = []
        for i in range(0, len(lst) ):

            print("\nsjdhgf", i)

            if i == 0:
                abc.append( lst[i] )
                # print( "sdrjgh", abc)

            else:
                for j in range(0, i):

                    a = lst[i] + lst[j]
                    print(a)
                    xy.append(a)

                    print("\ndlrjhghjgjkngkjsdngjkn", xy)
                
                abc.append(xy)

                abc.append( lst[i] )

                abc = list( set( lst ) )
                abc.sort()
        print(abc)
        ans = insect(abc, t)

        return ans

    else:
        return ans

n = int(input())
l = [ [] for x in range(n) ]   
for x in range(0,n):
    l[x] = list(map(int,input().split()))
    if (0 < l[x][0] and l[x][0] < l[x][1] and l[x][1] <10000001):
        break
 

a = insect( [2,5], 2 )
print( a)
