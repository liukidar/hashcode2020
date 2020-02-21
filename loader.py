f = open('./input/a_example.txt', 'r')

from library import Library
from book import Book
from data import Data

data = Data({
    'metricPreprocessor': 'euclidean',
    'groupGenerator': 'basic',
    'solutionGenerator': 'basic',
    'localImprover': 'basic'
    })

[n_books, n_libraries, data.days] = f.readline().split(' ')

# Create books for data
data.books = [Book(i, score) for i, score in enumerate([int(x) for x in f.readline().split()])]

line = f.readline()

while line != '':
	# Get library data
	n_books, signup_time, daily_ship = line.split()
	line = f.readline()

	# Get library books
	l_books = []
	n_lib = 0
	for x in line.split():
		l_books.append(data.books[int(x)])
		data.books[int(x)].addCopy()
	line = f.readline()

	# Add library to data
	l = Library(n_lib, signup_time, l_books, daily_ship)
	data.libraries.append(l)
	n_lib += 1

print([b.n for b in data.books])