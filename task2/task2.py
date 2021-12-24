import argparse


def pointer(circle_params, point_params):
	circle_x = float(circle_params[0][0])
	circle_y = float(circle_params[0][1])
	radius = float(circle_params[1][0])


	for i in range(len(point_params)):
		point_x = float(point_params[i][0])
		point_y = float(point_params[i][1])

		if (point_x - circle_x)**2 + (point_y - circle_y)**2 == radius**2:
			print("0", end='\n')
		elif (point_x - circle_x)**2 + (point_y - circle_y)**2 > radius**2:
			print("2", end='\n')
		elif (point_x - circle_x)**2 + (point_y - circle_y)**2 < radius**2:
			print("1", end='\n')



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('file_path_1', type=str, help='file_path_1')
	parser.add_argument('file_path_2', type=str, help='file_path_2')

	input_params = parser.parse_args()

	circle_params = []
	point_params = []

	with open(input_params.file_path_1) as file1:
		for line in file1:
			circle_params.append(line.split())

	with open(input_params.file_path_2) as file2:
		for line in file2:
			point_params.append(line.split())

	pointer(circle_params, point_params)


