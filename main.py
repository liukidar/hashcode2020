from data import Data
from fileio import FileIO

gData = Data({
	'metricPreprocessor': 'euclidean',
	'groupGenerator': 'basic',
	'solutionGenerator': 'basic',
	'localImprover': 'basic'
})
fileIO = FileIO(gData, {
	'problem': 'input.txt',
	'data': 'data',
	'groups': 'groups',
	'solutions': 'solutions'
}, gData.version())


