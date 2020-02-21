import group
import numpy
import disjoint_set as ds

class Grouper:
    def createGroups(self, libraries, threshold):
        edges = []
        for i in range(len(libraries)):
            for j in range(i, len(libraries)):
                edges.append((libraries[i].id, libraries[j].id, libraries[i].distance(libraries[j])))
        
        edges.sort(key=lambda x: x[2], reverse=True)
        index = 0
        while edges[index][2] > threshold:
            index += 1
        
        edges = edges[:index]

        return self.kruskal(libraries, edges)
        
    def kruskal(self, libraries, edges):
        forest = ds.DisjointSet()
        
        for lib in libraries:
            forest.find(lib.id)

        for edge in edges:
            if not forest.connected(edge[0], edge[1]):
                forest.union(edge[0], edge[1])

        
		for tree in forest.iterset():
			groups.append(Group([libraries[i] for i in tree]))
    
        #forest = list(forest)
        #listaGruppi = []
        #for elemento in forest:
        #    listaGruppi[elemento[1]].append(elemento[0])
        #    groups = []
		#	for tree in forest.iterset():
		#		groups.append(Group([libraries[i] for i in tree]))

        return groups

