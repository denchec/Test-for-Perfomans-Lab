import argparse



def leveling(list):
	if (min(list) + max(list)) % 2 == 0:
		mean = (min(list) + max(list)) // 2
	elif (min(list) + max(list)) % 2 == 1:
		mean = (min(list) + max(list)) // 2 + 1

	list.sort()

	if len(list) % 2 == 0:
	    x = list[len(list) // 2] - mean
	    y = mean - list[len(list) // 2 - 1]
	    if x > y:
	        mean_list = list[len(list) // 2 - 1]
	    elif y > x:
	        mean_list = list[len(list) // 2]
	elif len(list) % 2 == 1:
	    mean_list = list[len(list) // 2]

	count = 0


	for i in range(len(list)):
		while list[i] != mean_list:
			if list[i] > mean_list:
				list[i] -= 1
				count += 1
			elif list[i] < mean_list:
				list[i] += 1
				count += 1



	return count




if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('file_path', type=str, help='file_path')

	input_params = parser.parse_args()

	list = []

	with open(input_params.file_path) as file:
		for line in file:
			list.append(int(line))

	print(leveling(list))


