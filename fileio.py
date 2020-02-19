import json
import itertools
import numpy as np

class FileIO:    
	# _filenames -> dictionary containing problem filenames
	# _output -> dictionary containing output filenames (for problem output and groups)
	# _version -> hash of used techniques (through all levels)

	files = {}
	filenames = {}
	headerLen = 2 

	def __init__(self, _data, _filenames, _version):
		self.filenames['problem'] = _filenames['problem']
		self.filenames['data'] = _filenames['problem'][:-4] + '_' + _filenames['data'] + '_' + _version['data'] + '.json'
		self.filenames['groups'] = _filenames['problem'][:-4] + '_' + _filenames['groups'] + '_' + _version['groups'] + '.json'
		self.filenames['solutions'] = _filenames['problem'][:-4] + '_' + _filenames['solutions'] + '.json'
		# load preprocessed files data, if not present create it from the prblem statement thorugh the active preprocessor in data
		try:
			with open(self.filenames['data'], 'r') as json_file:
				self.files['data'] = json.load(json_file)
		except IOError:
			with open(self.filenames['problem'], 'r') as files_file:
				self.files['data'] = self.loadProblem(files_file, _data)
			
			# save the preprocessed files into a file
			with open(self.filenames['data'], 'w') as json_file:
				json.dump(self.files['data'], json_file)
		
		# load cached data for groups
		try:
			with open(self.filenames['groups'], 'r') as json_file:
				self.files['groups'] = json.load(json_file)
		except IOError:
				self.files['groups'] = []
				
		# load already computed solutions
		try:
			with open(self.filenames['solutions'], 'r') as json_file:
				self.files['solutions'] = json.load(json_file)
		except IOError:
			self.files['solutions'] = []
	
	def saveData(self):
		# save groups data
		with open(self.filenames['groups'], 'w') as json_file:
			json.dump(self.files['groups'], json_file)

		# save solutions data
		with open(self.filenames['solutions'], 'w') as json_file:
			json.dump(self.files['solutions'], json_file)
		 
	def loadProblem(self, _file, _data):
		# load _file into vectors and calls Data.Preprocessor

		# parameters are the list of problem parameters
		# r is the actual data
		parameters = [] 
		r = []

		# problem parameters
		for line in itertools.islice(_file, 0, self.headerLen):
			parameters += [int(i) for i in line.split()]

		# problem data
		_file.seek(0)
		for line in itertools.islice(_file, self.headerLen, None):
			r.append([int(x) for x in line.split()])

		data = _data.activePreprocessor.parse(parameters, r)

		return [parameters, data]