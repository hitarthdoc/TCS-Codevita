def insect(lst, t):
    # print(t)

    if t != 0:

        t = t - 1

        lst.sort()
        # print( lst)

        abc = []

        for i in range(0, len(lst) ):

            print("\nsjdhgf", i)

            if i == 0:
                abc.append( lst[i] )
                # print( "sdrjgh", abc)

            else:
                for j in range(0, i):

                    a = lst[i] + lst[j]
                    print(a)
                    abc[ len(abc): ] = [a]
                    

                abc.append( lst[i] )

                abc = list( set( lst ) )
                abc.sort()
        print(abc)
        ans = insect(abc, t)

        return ans

    else:
        return lst

n = int(input())
l = [ [] for x in range(n) ]   
for x in range(0,n):
    l[x] = list(map(int,input().split()))
    if (0 < l[x][0] and l[x][0] < l[x][1] and l[x][1] <10000001):
        break
 

a = insect( [2,5], 3 )
print( a)


