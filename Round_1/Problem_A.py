import math

N = int (input())

for i in range(0, N):
	
	F, B, T, FD, BD = map(int, input().split())
	direction = 0;
	if F > FD:
		print( T * FD, "F")
		continue

	elif F == B and F < FD:
		print("No Ditch")
		continue

	elif (F > B):
		direction = 1
	else:
		direction = -1

	dist_per_turn = 0
	turns = 0
	total_distance_travelled = 0

	if direction == 1:
		dist_per_turn = F - B
		turns = int( math.floor ( ( FD / dist_per_turn ) ) ) - 1
		last_position = dist_per_turn * turns
		delta_dist = FD - last_position
		if (delta_dist > 0):
			total_distance_travelled = ( (F + B) * turns ) + delta_dist
		else:
			total_distance_travelled = ( (F + B) * turns )

		print (total_distance_travelled, dist_per_turn, turns, last_position, delta_dist)
		print (total_distance_travelled * T, "F")
	elif direction == -1:
		dist_per_turn = B - F
		turns = int( math.floor ( ( BD / dist_per_turn ) ) )
		last_position = dist_per_turn * turns
		delta_dist = BD - last_position
		if (delta_dist > 0):
			total_distance_travelled = ( (F + B) * turns ) + (2 * F) + delta_dist
		else:
			total_distance_travelled = ( (F + B) * turns )
			
		print (total_distance_travelled, dist_per_turn, turns, last_position, delta_dist)
		print (total_distance_travelled * T, "B")

	# else:
	# 	continue
