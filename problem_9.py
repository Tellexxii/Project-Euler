def Pythagorean():
	thousand = 1000
	for a in range(1, thousand + 1):
		for b in range(a + 1, thousand + 1):
			c = thousand - a - b
			if a * a + b * b == c * c:
				return str(a * b * c)

print(Pythagorean())


