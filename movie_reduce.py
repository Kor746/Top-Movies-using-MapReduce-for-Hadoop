import sys


def reducer(infile):
	limit = 5
	for line in infile:
		if limit == 0:
			break;
		line = line.strip()
		tokens = line.split(" ")
		movieId, rating = tokens[0], float(tokens[1])
		print(movieId, rating)
		limit -= 1


def main():
	stream = sys.stdin
	reducer(stream)

if __name__ == "__main__":
	main()
