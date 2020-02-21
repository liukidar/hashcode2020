

from random import sample
from library import Library
from book import Book
from data import Data
from genetic import Solution

files = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']

for input_file in files[0:1]:
	with open('./input/' + input_file, 'r') as f:

		data = Data({
				'metricPreprocessor': 'euclidean',
				'groupGenerator': 'basic',
				'solutionGenerator': 'basic',
				'localImprover': 'basic'
				})

		[n_books, n_libraries, data.days] = f.readline().split()

		# Create books for data
		data.books = [Book(i, score) for i, score in enumerate([int(x) for x in f.readline().split()])]

		line = f.readline()
		i = 0

		while line:
			if len(line) < 2 or i >= int(n_libraries):
				break

			# Get library data
			n_books, signup_time, daily_ship = line.split()
			line = f.readline()

			# Get library books
			l_books = []
			for x in line.split():
				l_books.append(data.books[int(x)])
				data.books[int(x)].addCopy()
			line = f.readline()

			# Add library to data
			l = Library(i, signup_time, l_books, daily_ship)
			data.libraries.append(l)

			i += 1
		s = Solution()
		s.libraries = [x.id for x in sample(data.libraries, len(data.libraries))]

		s.toTXT(data, input_file)
		print('Done writing ' + input_file)
