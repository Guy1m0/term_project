import re,sys,itertools, operator, timeit
from collections import defaultdict

gra_list = []
t_list = []
t_map_list=[]

dic = {}

gra_map = [] #chossen gra mapping for the text
#use to record the chosen grammar variables
un_gra_map = [] #remaining

un_dic = defaultdict(int) 
sorted_dic = []

pos_tag = []
pos_map = []

def match(targted,database):
	#print "context length:", len(targted)
	#print "context:"
	#print targted
	#print "size:", len(database)
	#print database
	#gra_map[str(size)] = []
	for i in range(1,len(database)+1):
		for combo in itertools.combinations(database, i):
			finding = False

			
			if finding:
				return list(combo)
				print list(combo)

def map(targted,database):
	#mapping the first pair
	#for p1 in targted[-1][1]

	for pair in targted:
		#finding = False
		index_1 = 0
		index_2 = 0

		while True:
			pair_list = [pair[0][index_1],pair[1][index_2]]
			if pair_list in database:
				#print [pair[0][index_1],pair[1][index_2]]
				#print "length:",i
				#print "combination:", list(combo)
				pos_tag.append(pair_list[0])
				#finding = True
				break

			index_1 = index_1 + 1
			if index_1 == len(pair[0]):
				index_1 = 0
				index_2 = index_2 + 1
			if index_2 == len(pair[1]):
				print "no way..."
				break
			#print "break out?", finding, i

	pos_tag.append(targted[-1][1][0])
	for i in range (len(t_list)):
		pos_map.append([t_list[i][0],pos_tag[i]])

	pos_map.append([t_list[-1][-1],pos_tag[-1]])
	#print pos_map
	#print pos_tag
	#print "length:",len(t_list),len(t_map_list),len(pos_tag)
		#if not finding:
		#	un_gra_map.append(pair)

		#if pos_tag = []			

def prune_1(targted):
	for pair in targted:
		if len(pair[0]) > 1 or len(pair[1]) > 1:
			un_gra_map.append(pair)
			for p1 in pair[0]:
				for p2 in pair[1]:
					un_dic[p1 + ',' + p2] += 1
			#un_dic[','.join(pair)] += 1
		else:
			gra_map.append([pair[0][0],pair[1][0]])
	#print "mult:", un_gra_map
	#print "------------------------------"
	#print "unsorted:", un_dic
	sorted_dic = sorted(un_dic.items(), key = operator.itemgetter(1))
	#print "sorted:", sorted_dic

	for gra in reversed(sorted_dic):
		prune(un_gra_map,gra[0])
		#print "------------------------------"
		#print "un:", un_gra_map
		if un_gra_map == []:
			break
	#print t_map_list
	print "# of origin 'path':",len(t_map_list)
	print "# of grammar use:", len(gra_map)


def prune(targted, gra):
	un_gra_map = []
	gra_map.append(gra.split(','))
	for pair in targted:
		#print "pair:",pair
		finding = False
		index_1 = 0
		index_2 = 0
		while not finding:
			pair_str = pair[0][index_1]+',' +pair[1][index_2]
			if pair_str == gra:
				#print [pair[0][index_1],pair[1][index_2]]
				#print "length:",i
				#print "combination:", list(combo)

				finding = True
				break
			index_1 = index_1 + 1
			if index_1 == len(pair[0]):
				index_1 = 0
				index_2 = index_2 + 1
			if index_2 == len(pair[1]):
				break
			#print "break out?", finding, i

		if not finding:
			un_gra_map.append(pair)

	
	#print "single:", gra_map



def comp(targted, database):
	pass


def load_dic(filename):
	with open(filename) as f:
		lines = f.readlines()

	for line in lines:
		[tok, tag] = line.split()
		if tok not in dic:
			dic[tok] = [tag]
		else:
			dic[tok].append(tag)
	#print dic

def load_gra(filename):
	with open(filename) as f:
		lines = f.readlines()

	for line in lines:
		[g1,g2] = line.split()
		pair = [g1,g2]

		gra_list.append(pair)
	#print gra_list

def load_text(filename):
	with open(filename) as f:
		lines = f.readlines()
	print "length of context", len(lines)
	ctx = []
	pair = []
	for l in lines:
		ctx.append(l.split())

	for i in range(len(lines)-1):
		#print ctx[i]
		pair = [ctx[i][1],ctx[i+1][1]]
		t_list.append(pair)

	for t_pair in t_list:
		
		p = [dic[t_pair[0]],dic[t_pair[1]]]
		t_map_list.append(p)
	#print t_list
	#print t_map_list

def start(dic,text,gram):
	start = timeit.default_timer()
	load_dic(dic)
	load_text(text)
	load_gra(gram)
	prune_1(t_map_list)
	map(t_map_list,gra_map)
	stop = timeit.default_timer()
	print "running time:", (stop - start)
	#match(t_map_list, gra_list)


if __name__ == '__main__':
	#dic gra text
	args = sys.argv[1:]
	if len(args) != 3:
		print "use default"
		start("dict.txt","text.txt","gram.txt")
	else:
		start(args[0],args[1],args[2])
