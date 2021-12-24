import json
import argparse


file_value = {}

def func(item_list):
	global file_value
	for item in item_list:
		if "value" in item:
			item["value"] = file_value[item["id"]]
		if "values" in item:
			func(item["values"])



if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('file_path_1', type=str, help='file_path_1')
	parser.add_argument('file_path_2', type=str, help='file_path_2')


	input_params = parser.parse_args()

	with open(input_params.file_path_1) as path1:
		file_test = json.load(path1)

	with open(input_params.file_path_2) as path2:
		file_value_ = json.load(path2)

	file_value = {}
	for val in file_value_["values"]:
		file_value[val["id"]] = val["value"]

	func(file_test["tests"])

				


	print(file_test)

	json_file = json.dumps(file_test)

	with open("report.json", "w") as outfile:
		outfile.write(json_file)

