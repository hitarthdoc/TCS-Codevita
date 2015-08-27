N = abs(int (input()))

if N <= 1000:
    A = [10, 7, 5, 1]
    ans = []
    for y in range(0, N):

        i = 0
        j = 0

        L = abs(int (input()))

        while L != 0:

            i = i + int(L / A[j])

            L = L % A[j]

            j += 1

        ans.append(i)

    print()
    for i in range(0, len(ans)):
        print(ans[i])