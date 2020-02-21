import library
import book


class Group:
    libs = []
    value = None
    computedValue = None
    evaluation = None

    def __init__(self, libs):
        self.libs = libs
        self.libs.sort(key=library.Library.orderFactor)

    def evaluate(self):
        if self.evaluation == None:
            v = 0
            for lib in self.libs:
                v += lib.evaluate()

            self.evaluation = v / len(self.libs)

        return self.evaluation

    def score(self, _start, _end, _usedBooks):
        s = 0
        for lib in self.libs:
            s += lib.score(_start, _end, _usedBooks)
