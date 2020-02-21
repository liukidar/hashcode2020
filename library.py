from book import Book
class Library:
    value_used = None
    value_total = None
    startDay = None
    lastBook = None
    evaluation = None

    def __init__(self, _id, signupDays, booksList, booksPerShip): 
        self.id = _id
        self.signupDays = signupDays
        self.booksList = booksList #ordered by id
        self.bookListByValue = self.booksList
        self.bookListByValue.sort(key=Book.value) 
        self.booksPerShip = booksPerShip

    def distance(self, l2):
        # calcola numero diversi
        different = 0
        tot = len(self.booksList) + len(l2.booksList)
        i = 0
        j = 0
        while i < len(self.booksList) and j < len(l2.booksList):
            if self.booksList[i] == l2.booksList[j]:
                i += 1
                j += 1
            elif self.booksList[i] > l2.booksList[j]:
                different += 1
                j += 1
            elif self.booksList[i] < l2.booksList[j]:
                different += 1
                i += 1
        different += (len(self.booksList) - i) if j == len(l2.booksList) else (len(l2.booksList) - j)
        return different/tot
        #return len(set(self.booksList & l2.booksList)) / len(set(self.booksList | l2.booksList))

    def orderFactor(self):
        return len(self.booksList)

    # heuristic
    def evaluate(self):
        if self.evaluation == None: 
            v = 0
            for book in self.booksList:
                v += book.value()

            self.evaluation = v / (self.signupDays + len(self.booksList) / self.booksPerShip)
        
        return self.evaluation
    
    def score(self, _start, _end, _usedBooks):
        self.startDay = _start + self.signupDays
        self.lastBook = min((_end - self.startDay) * self.booksPerShip, len(self.bookListByValue))
        self.value_used = 0

        for book in self.bookListByValue[0:self.lastBook]:
            self.value_used += book.value() if book.id not in _usedBooks else 0
            _usedBooks[book.id] = True

        #total = used
        #while b = next(book):
        #    total += b.value()

        return self.value_used