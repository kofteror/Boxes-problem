class Boxes:
	def __init__(self, w, l, h):
		self.L = l
		self.H = h
		self.W = w


def tower(box, i, last):
	"""
	tower function: this function finds and return the higest tower possible to build
	using the bricks in the box array , according to the constrain :
	box[i].L>box[j].L AND box[i].W>box[j].W for each i<j bricks
	Assuming boxes is order by the W



	:param box: sorrted array by W
	:param i: last brick index to start build
	:param last: last brick that was added , should be called with None
	:return: highest tower
	"""
	a = 0
	if i == 0:
		if last is None:
			return box[0].H
		elif box[i].L > last.L:
			return box[i].H
		else:
			return 0


	if last is None or box[i].L > last.L:
		a = tower(box, i-1, box[i])+box[i].H
	b = tower(box, i-1, last)
	if a > b:
		return a
	return b

def tower2(boxs, size):
	"""
	Same as tower function, using Dynamic programming


	:param boxs:
	:param size:
	:return:
	"""
	print size
        matrix=[]
	while (size) :
		matrix.append([])
		size-=1;
	for i in range(0, len(boxs)):
		for j in range(0, len(boxs)):
			matrix[i].append(0)

	for i in range(0, len(boxs)):
		for j in range(0, len(boxs)):
			if (i==0):
				matrix[i][j]=boxs[i].H
			else:
				if (j >= i ):
					matrix[i][j]=matrix[i][j-1]
					continue
				if (boxs[i].L < boxs[j].L):
					if j==0:
						matrix[i][j]=boxs[i].H+boxs[j].H
					else:
						if matrix[i][j-1] < boxs[i].H+matrix[j][i] :
							matrix[i][j] = boxs[i].H+matrix[j][i]
						else :
							matrix[i][j] = matrix[i][j-1]

				else:
					if j == 0 :
						matrix[i][j]=boxs[i].H
					else:
						matrix[i][j] = matrix[i][j-1]


        print matrix


boxs = [Boxes(10, 91, 10), Boxes(9, 99, 20), Boxes(8, 81, 300), Boxes(7, 7, 25), Boxes(6, 80, 600)]
print tower(boxs, len(boxs)-1, None)
tower2(boxs, len(boxs))
print tower.__doc__

