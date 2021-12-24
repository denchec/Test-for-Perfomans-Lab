import argparse


def sum_1(n, m):
	x = []

	for i in range(n):
		x.append(i+1)

	b = 0
	end = []

	flag = 1

	while b != x[0]:
		cycle = 0
		y = []


		for j in range(m):
			if b == 0:
				if b + (j + 1) - cycle > n:
					cycle += n
				y.append(b + (j + 1) - cycle)
			else:
				if b + j - cycle > n:
					cycle += n
				y.append(b + j - cycle)

		end.append(y[0])

		b = y[-1]

	return end



if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('n', type=int, help='n')
	parser.add_argument('m', type=int, help='m')

	input_params = parser.parse_args()

	print(sum_1(input_params.n, input_params.m))






