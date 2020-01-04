import sys
import csv


def mapper(path):
	
	counter = 1
	with open(path) as csvf:
		mappings = []
		reader = csv.reader(csvf, delimiter = ',')
		next(reader, None)
		for line in reader :

			movie_Id, rating = line[1], line[2]
			mappings += [(movie_Id, rating)]
			if counter % 2000 == 0:
				break;
			counter += 1

		for i in sorted(mappings, key = lambda x : x[1], reverse = True):
			print(i[0], i[1])

	
def main():
	file_path = sys.stdin
	mapper(file_path)

if __name__ == "__main__":
	main()
