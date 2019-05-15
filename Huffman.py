import queue


class HuffmanNode(object):
    def __init__(self, children, root=None):
        self.children = children
    def children(self):
        return((self.children))
    
    
d=int(input("d="))
integer=int(25/(d-1))

dum=0
if 25-integer*(d-1)!=0:
	dum=(d-1)-(25-integer*(d-1))
print("the number of dummy: "+str(dum))
children=[]

freq = [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'),
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'),
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z') ]

for num in range(0,dum):
	freq.append((0.0," "))

def create_tree(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:    # 1. Create a leaf node for each symbol
        p.put(value)             #    and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        sumup=0
        children=[]
        for num in range(0,d):
	        getthenode=p.get()
	        children.append(getthenode)
	        sumup+=getthenode[0]
	        
        node = HuffmanNode(children)
        p.put((sumup, node))
    return p.get()

node = create_tree(freq)


def walk_tree(node, prefix="", code={}):
    """
    node 是一个tuple(freq, HuffmanNode|character)
    """
    if isinstance(node[1], HuffmanNode): # node[1]是一个HuffmanNode
	    code0=[]
	    for num in range(0,d):
	        code0.append(walk_tree(node[1].children[num], str(num), code.copy()) )# 这里如果直接传入code会出错
	        #num+=1
		    
	    for num in range(0, d):
		    if len(code0[num]) > 0:
			    for k, v in code0[num].items():
				    code[k] = prefix + v
			    

    else: # node[1]是一个字符
        code[node[1]] = prefix
    return(code)


code = walk_tree(node)

# 输出每个字母的编码
for i in sorted(freq, reverse=True):
    try:
        print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
    except Exception as e:
        print(e)
        continue
