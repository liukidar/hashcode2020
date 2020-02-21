from library import Library
from data import Data

class Solution:
    libraries = []
    groups = []

    def toDNA(self):
        dna = ''
        for library in self.libraries:
            dna += library.id
    
    def fromDNA(self, _dna, _data):
        for l in _dna:
            self.libraries.append(_data.libraries[l])

    def toTXT(self, _data, _problem_file):
        booksSent = set()
        with open('./output/' + _problem_file, 'w+') as f:
            f.write(str(len(self.libraries)) + '\n')

            for l in self.libraries:
                    libraryBooksSent = []
                    for b in _data.libraries[l].bookListByValue:
                            if b.id not in booksSent:
                                    booksSent.add(b.id)
                                    libraryBooksSent.append(b.id)
                    if (len(libraryBooksSent) != 0):
                        f.write(str(_data.libraries[l].id) + ' ' + str(len(libraryBooksSent)) + '\n')
                        f.write(' '.join(str(x) for x in libraryBooksSent) + '\n')
				