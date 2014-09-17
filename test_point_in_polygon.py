#!/usr/bin/env python
def getNpoints(N):
	out_list = []
	for i in range(0, N):
		vert = tuple(int(x.strip()) for x in input()[1:-1].split(','))
		out_list.append(vert)
	return out_list

def isLeft(p0, p1, p2):
	return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

def isPointInPoly(p, poly):
	cnt = 0
	V = tuple(poly[:]) + (poly[0],)
	for i in range(len(V)-1):
		if (V[i][1] == V[i+1][1] and V[i][1] == p[1]) and (p[0] >= min(V[i][0], V[i+1][0]) and p[0] <= max(V[i][0],V[i+1][0])) :
			return True
		if V[i][1] <= p[1]:
			if V[i+1][1] > p[1]:
				if isLeft(V[i], V[i+1], p) > 0:
					cnt += 1
				elif isLeft(V[i], V[i+1], p) == 0:
					return True
		else:
			if V[i+1][1] <= p[1]:
				if isLeft(V[i], V[i+1], p) < 0:
					cnt -= 1
				elif isLeft(V[i], V[i+1], p) == 0:
					return True
	return cnt != 0

def main():
	pol_N = int(input().strip())
	pol_verts = getNpoints(pol_N)
	test_N = int(input().strip())
	test_points = getNpoints(test_N)
	for point in test_points:
		if isPointInPoly(point, pol_verts):
			print("yes")
		else :
			print("no")


	


if __name__ == "__main__":
	main()
