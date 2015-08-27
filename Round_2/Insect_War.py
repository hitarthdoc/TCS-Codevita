def insect(lst, t):
    # print(t)

    if t != 0:

        t = t - 1

        lst.sort()
        # print( lst)

        temp = list()

        for i in range(0, len(lst) ):

            print("\nsjdhgf", i)

            if i == 0:
                temp.append( lst[i] )
                # print( "sdrjgh", temp)

            else:
                for j in range(0, i):

                    a = lst[i] + lst[j]
                    print(a)
                    temp.append(a)
                
                temp.append( lst[i] )

                temp = list( set( lst ) )
                temp.sort()
        print(temp)
        ans = insect(temp, t)

        return ans

    else:
        return lst

a = insect( [2,5], 3 )
print( a)
