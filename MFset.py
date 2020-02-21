class node :
	"stores the name of the element, and an index to parent"

	def __init__( self, n, p=None ) :
		"Takes element's name, and parent's index"
		self.name = n
		self.parent = p
		self.count = 1

class mfset :
	"A set of disjoint sets"

	def __init__( self, L ) :
		"Takes a list of single-elements (to be made into sets)"

		self.idx = {}	# the hash table, stores the vertices (as nodes)

			# iterate over list of elements, make each a set of one
			#		(a tree w/one node in it), store the node in the hash table
		for i in L :
			self.idx[ i ] = node( i ) 

	def findNode( self, t ) :
		"Given element t, returns node at top of tree"
		# merge actually needs the whole node, so it can modify the parent ptr,
		#		not just the label at the top.  So, a helper method for find and
		#		merge

		if( not self.idx.has_key( t ) ) :
			return None

		p = self.idx[ t ]
		while( p.parent != None ) :
			p = p.parent

		# path-compression.  Re-traverse path to root, setting each node's
		#		parent to the root (make the trees short and fat)
		q = self.idx[ t ]
		while( q != p ) :
			r = q
			q = q.parent
			r.parent = p

		return p
	
	def find( self, t ) :
		"Given element t, returns label at top of tree"

		return self.findNode( t ).name

	def merge( self, x, y ) :
		"merges sets containing x, y"

		t1 = self.findNode( x )
		t2 = self.findNode( y )

		if t1== t2 or t1==None or t2==None :
			return None

		# merge smaller tree into larger
		if( t1.count < t2.count ) :
			t1.parent = t2
			t2.count += t1.count
		else :
			t2.parent = t1
			t1.count += t2.count
