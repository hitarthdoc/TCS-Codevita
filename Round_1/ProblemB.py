M = float(input())
T = int(input())
R = float(input())
if M > 0 and T > 0 and R >= 0:
	per = (R/1200)+1

	sum1 = M
	for i in range(0,T):
		sum1 = M + (sum1/per) 
	sum1=sum1-M
	print(float(sum1))
else:
	print("Invalid Input")
