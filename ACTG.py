import queue
class HuffmanNode(object):
	def __init__(self, children, root=None):
		self.children = children
	
	def children(self):
		return ((self.children))

def outputFile(d):
	
	length = len(seq)
	A = seq.count("A") / length
	C = seq.count("C") / length
	T = seq.count("T") / length
	G = seq.count("G") / length
	freq = [(A, 'A'), (C, 'C'), (T, 'T'), (G, 'G')]
	
	
	integer = int(3/ (d - 1))
	
	dum = 0
	if 3 - integer * (d - 1) != 0:
		dum = (d - 1) - (3 - integer * (d - 1))
	print("d="+str(d))
	print("dum="+str(dum))
	
	children = []
	
	
	
	for num in range(0, dum):
		freq.append((0.0, " "))
	print(freq)
	
	
	def create_tree(frequencies):
		p = queue.PriorityQueue()

		for value in frequencies:  # 1. Create a leaf node for each symbol
			p.put(value)  # and add it to the priority queue
		while p.qsize() > 1:  # 2. While there is more than one node

			sumup = 0
			children = []
			for num in range(0, d):
				getthenode = p.get()
				children.append(getthenode)
				sumup += getthenode[0]
			
			# 2a. remove two highest nodes
			node = HuffmanNode(children)  # 2b. create internal node with children
			p.put((sumup, node))  # 2c. add new node to queue

		return p.get()  # 3. tree is complete - return root node
	
	
	node = create_tree(freq)
	
	
	# =================== 以上是Dave提供的思路  ==================
	# 树里的每一个节点是一个tuple，node[0]是频率，node[1]是HuffmanNode 或者 character
	# 下面是我的实现
	def walk_tree(node, prefix="", code={}):
		"""
		node 是一个tuple(freq, HuffmanNode|character)
		"""
		if isinstance(node[1], HuffmanNode):  # node[1]是一个HuffmanNode
			code0 = []
			for num in range(0, d):
				code0.append(walk_tree(node[1].children[num], str(num), code.copy()))  # 这里如果直接传入code会出错
			# num+=1
			
			for num in range(0, d):
				if len(code0[num]) > 0:
					for k, v in code0[num].items():
						code[k] = prefix + v
		
		
		else:  # node[1]是一个字符
			code[node[1]] = prefix
		return (code)
	
	
	code = walk_tree(node)
	
	print(code)
	seqReplace=seq
	averageLength=0
	averageCodewordLength=0
	# 输出每个字母的编码
	for i in sorted(freq, reverse=True):
		try:
			print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
			seqReplace=seqReplace.replace(i[1], code[i[1]])
			averageLength+=i[0]*len(code[i[1]])
			if i[0]!=0:
				averageCodewordLength+=len(code[i[1]])*0.25
		except Exception as e:
			print(e)
			continue
			
	
	
	fo = open("fileWhenD=" + str(d), "w")
	fo.write(seqReplace)
	fo.close()
	
	
	print("the length before encode: "+str(len(seq)))
	print("the length after encode: "+str(len(seqReplace)))
	print("the average length is: "+str(len(seqReplace)/len(seq)))
	print("the average codeword length is: "+str(averageCodewordLength))
	print("\n")

inputfile ="NC_000964.3.seq"
f = open(inputfile, "r")
seq = f.read()
f.close()

for d in range(2,5):
	outputFile(d)