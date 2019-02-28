class Photo(object):
	def __init__(self, id, orient, tags):
		self.id = id
		self.orient = orient
		self.tags = set(tags)

	def __repr__(self):
		return str(f"{'V' if self.orient else 'H'} {self.tags}")


if __name__ == '__main__':
	pass
