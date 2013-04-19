class Chest(object):
	def __init__(self, c_id, k_type, keys):
		self.c_id  = c_id
		self.keys = keys
		self.k_type = k_type


class Key(object):
	def __init__(self,k_id):
		self.k_id = k_id

	def can_open(self, chest):
		return self.k_id == chest.k_type
			

class Graph_Node(object):
	"""docstring for """
	def __init__(self, chest, edges):
		self.chest = chest
		self.edges = edges
		
	def add_to_edges(self,node):
		self.edges.append(node)

def check_termination(chests,key_catalog):
	for chest in chests:
		for key in key_catalog:
			if key.can_open(chest):
				return False
	return True

def initialize_chest_graph(start, chests, key_catalog):
	if len(chests) == 0:
		return
	if check_termination(chests, key_catalog):
		return 
	else:
		for chest in chests:
			for key in key_catalog:
				if key.can_open(chest):
					node = Graph_Node(chest,[])
					start.add_to_edges(node)
					k_rest = key_catalog[:]
					k_rest.remove(key)
					c_rest = chests[:]
					c_rest.remove(node.chest)
					if len(node.chest.keys) != 0:
						k_rest += node.chest.keys
					initialize_chest_graph(node,c_rest,k_rest)


def longest_path_len(node, depth):
	if len(node.edges) == 0:
		return depth 
	else:
		path_len = []
		for n in node.edges:
			path_len.append(longest_path_len(n,depth + 1))
		return max(path_len) 



def traverse_graph(node, visited, length, chest_table):
	iteration = 0
	while len(visited) != length:
		target_length = length - iteration
		candidate = []
		node_table = {}
		for n in node.edges:
			if longest_path_len(n,0) == target_length:
				cid = n.chest.c_id
				candidate.append(cid)
				node_table[cid] = n
		if len(candidate) != 0:
			min_cid = min(candidate)
			chest = chest_table[min_cid - 1]
			visited.append(min_cid)
			node = node_table[min_cid]
		iteration += 1
	return visited

def main():
	fi = open("D-small-attempt0.in", "r")
	fo = open("output.txt", "w")
	case_num = int(fi.readline().strip())
	for i in range(case_num):
		sizes = fi.readline().strip().split()
		chest_num = int(sizes[1])
		key_catalog = []
		k_list = fi.readline().strip().split()
		chest_table = []
		for k_id in k_list:
			key_catalog.append(Key(int(k_id)))
		for j in range(chest_num):
			content = fi.readline().strip().split()
			cid = j + 1
			k_type = int(content[0])
			keys = []
			for k_id in content[2:]:
				keys.append(Key(int(k_id)))
			chest_table.append(Chest(cid,k_type,keys))
		start = Graph_Node(None,[])
		initialize_chest_graph(start,chest_table,key_catalog)
		longest = longest_path_len(start,0)
		if longest < chest_num:
			fo.write("Case #{0}: IMPOSSIBLE\n".format(i+1))
			print "Case #{0}: IMPOSSIBLE\n".format(i+1)
		else:
			visited = traverse_graph(start,[],longest,chest_table)
			a = ''
			for num in visited:
				a = a + ' ' + str(num)
			fo.write("Case #{0}:{1}\n".format(i+1,a))
			print "Case #{0}:{1}\n".format(i+1,a)		
	fi.close()
	fo.close()

if __name__ == '__main__':
	main()