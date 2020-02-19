import preprocessors

class Data:

	# contiene le tecniche divise per livello 
	# 	- preprocessors
	# 	- creazione gruppi
	# 	- creazione soluzione
	#	- ricerca locale

	metricPreprocessors = {
		'euclidean': preprocessors.Euclidean()
	}
	groupGenerators = {
		'basic': None
	}
	solutionGenarators = {
		'basic': None
	}
	localImprovers = {
		'basic': None
	}

	def __init__(self, _settings):
		self.activePreprocessor = self.metricPreprocessors[_settings['metricPreprocessor']]
		self.activeGroupGenerator = self.groupGenerators[_settings['groupGenerator']]
		self.activeSolutionGenarator = self.solutionGenarators[_settings['solutionGenerator']]
		self.activeLocalImprover = self.localImprovers[_settings['localImprover']]

	def version(self):
		return {
			'data': '0',
			'groups': '0'
		}

