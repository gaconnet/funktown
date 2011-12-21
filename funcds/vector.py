from .lookuptree import LookupTree 

class ImmutableVector:
	def __init__(self, initvalues=None):
		if not initvalues: initvalues = []
		self.tree = LookupTree(initvalues)
		self._length = len(initvalues)

	def assoc(self, index, value):
		newvec = ImmutableVector()
		newvec.tree = self.tree.assoc(index, value)
		if index >= self._length:
			newvec._length = index+1
		else:
			newvec._length = self._length
		return newvec

	def conj(self, value):
		return self.assoc(self._length, value)

	def get(self, index):
		try:
			return self[index]
		except IndexError: return None

	def __len__(self):
		return self._length

	def __getitem__(self, index):
		if index >= self._length: raise IndexError()
		return self.tree[index]

