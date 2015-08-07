N = int(raw_input("Enter N:"))
S = []

for i in range(0, N):
	S.append(int(raw_input("\nEnter S:")))

X = int(raw_input("Enter X:"))

print X

for i in range(0,N):

	for j in range(0,(N-1)):
		
		for k in range(0,(N-2)):
			if S[i]+S[j]+S[k]==X and i != k and i != j and j != k:
				print "true"

		
		
		# if i + S[] +
