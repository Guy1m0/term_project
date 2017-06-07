import re,sys,itertools, operator, timeit
from collections import defaultdict
import collections

gra_list = []
t_list = []
t_map_list=[]

dic = {}

gra_map = [] #chossen gra mapping for the text
#use to record the chosen grammar variables



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
	g = open("map","w+")
	for t in pos_map:
		g.write(' ')
		g.write('/'.join(t))
		g.write(' ')
		if t[0] == '.':
			g.write("\n")
	g.close()
	#print pos_map
	#print pos_tag
	#print "length:",len(t_list),len(t_map_list),len(pos_tag)
		#if not finding:
		#	un_gra_map.append(pair)

		#if pos_tag = []			





def prune_1(targted):
	un_dic = defaultdict(int) 
	un_gra_map = [] #remaining
	for pair in targted:
			#for tag_pair in pair:

		if (len(pair[0]) > 1) or (len(pair[1]) > 1):
			un_gra_map.append(pair)
			for p1 in pair[0]:
				for p2 in pair[1]:
					un_dic[p1 + ',' + p2] += 1
			#un_dic[','.join(pair)] += 1
		else:
			p = [pair[0][0],pair[1][0]]
			if p not in gra_map:
				gra_map.append(p)
	#print len(gra_map)
	#print "mult:", un_gra_map
	#print "------------------------------"
	#print "unsorted:", un_dic
	sorted_dic = sorted(un_dic.items(), key = operator.itemgetter(1))
	#print "sorted:", sorted_dic
	
	#for gra in reversed(sorted_dic):
	while True:
		#print "before:", sorted_dic
		#print "un:", len(un_gra_map)
		[un_dic,un_gra_map] = prune(un_gra_map,sorted_dic[-1][0])
		#print "after:", un_dic
		sorted_dic = sorted(un_dic.items(), key = operator.itemgetter(1))
		#print "------------------------------"
		#print "un:", len(un_gra_map)
		if un_gra_map == []:
			break
	#print t_map_list
	
	print "# of origin 'path':",len(t_map_list)
	print "# of grammar use:", len(gra_map)

'''
def prune(targted, gra):
	#print "most grammar:", gra
	un_gra_map = []
	gra_map.append(gra.split(','))
	un_dic = defaultdict(int) 
	#print len(un_dic)

	for pair in targted:
		#print "pair:",pair
		finding = False
		index_1 = 0
		index_2 = 0
		tem = []
		while not finding:

			pair_str = pair[0][index_1]+',' +pair[1][index_2]
			tem.append(pair_str)
			if pair_str == gra:
				#print [pair[0][index_1],pair[1][index_2]]
				#print "length:",i
				#print "combination:", list(combo)
				for t in tem[:-1]:
					un_dic[t] -= 1
				finding = True
				break
			else:
				un_dic[pair_str] += 1

			index_1 = index_1 + 1

			if index_1 == len(pair[0]):
				index_1 = 0
				index_2 = index_2 + 1
			if index_2 == len(pair[1]):
				break
			#print "break out?", finding, i

		if not finding:

			un_gra_map.append(pair)

	return [un_dic,un_gra_map]
	
	#print "single:", gra_map

'''

def comp(targted, database):
	with open(sol) as f:
		lines = f.readlines()

class LoadingFiles():
	dic = {}
	gra_list = []
	t_list = []
#load taggings for each word
	def __init__(self):
		pass

	def load_dic(self,filename):
		with open(filename) as f:
			lines = f.readlines()

		for line in lines:
			[tok, tag] = line.split()
			#save the word tagging pair to dic
			if tok not in self.dic:
				self.dic[tok] = [tag]
			else:
				self.dic[tok].append(tag)
				#print self.dic[tok]

		#print self.dic['book']
		return self.dic
		#print dic

	#load available following tagging for the given tagging, and save to gra_list
	def load_gra(self,filename):
		with open(filename) as f:
			lines = f.readlines()

		for line in lines:
			[g1,g2] = line.split()

			pair = [g1,g2]
			#print pair
			self.gra_list.append(pair)

		return self.gra_list
		#print gra_list

	#load targted context and replace the word to taggings
	def load_text(self,filename):
		with open(filename) as f:
			lines = f.readlines()
		print "length of context", len(lines)
		ctx = []
		pair = []
		for l in lines:
			ctx.append(l.split())

		#for i in range(len(lines)):
			#print ctx[i]
			#pair = [ctx[i][1],ctx[i+1][1]]
		#	self.t_list.append(ctx[i][1])

		return ctx#self.t_list

	def load_text_tagged(self,filename):
		with open(filename) as f:
			lines = f.readlines()
		print "length of context", len(lines)
		ctx = []
		pair = []
		for l in lines:
			ctx.append(l.split())
		#print ctx
		return ctx



class GreedyMM():
	tag_dic = {} 
	Stt = defaultdict(list) #use to record word covered by tag-tag
	Htt = defaultdict(list) #use to record word covered by tag-tag
	gra_list = []
	t_list = []
	t_tag_list = [] #convert the word-word with its corresponding tag-tag

	def __init__(self, dic,gra,text):
		self.tag_dic = dic #available tag-tag dictionary
		self.gra_list = gra #bigram grammar
		self.t_list = text #the targeting text, such as 1 I, 2 am

	def l_dic(self, tag):
		return len(self.Stt[tag])

	def alg2(self):

		
		chosen = [] #chosen bigram tag
		ctx = [] #word only targeting text
		Urem = [] #Number of elements in U remaining to be covered
		Urem.append(0) #use inter to represent Wn word

		#init 
		for l in self.t_list:
			
			Urem.append(int(l[0]))
			ctx.append(l[1])
		#include 'START' and 'END'
		Urem.append((Urem[-1]+1))

		pre_tag = ['START']
		pos = 0

		for word in ctx:
			pair = []
			#finding all the tag for the word
			for tag_1 in pre_tag:
				next_tag = self.tag_dic[word]
				#finding all the tag for the word
				for tag_2 in next_tag:
					S = tag_1 + ' ' + tag_2
					#check if the Tag-Tag follows grammar
					if [tag_1,tag_2] not in self.gra_list:
						#exception
						if 'START' != tag_1:# and 'END' != tag_2:
							#print "not existed", [tag_1,tag_2]
							continue
					#use to record the tag-tag in DIC&GRA
					pair.append([tag_1,tag_2])
					#update to dictionary
					if pos not in self.Stt[S]:
						self.Stt[S].append(pos)
					if (pos + 1) not in self.Stt[S]:
						self.Stt[S].append(pos+1)
			pos += 1
			pre_tag = next_tag
			self.t_tag_list.append(pair)
		#adding the END node
		pair = []
		for t in next_tag:
			self.Stt[t + ' ' + 'END'].extend([pos,pos+1])
			pair.append([t,'END'])
		self.t_tag_list.append(pair)
		#print self.Stt['. end']

		#continue if 'word' remains
		while (Urem != []):
			#find the most used tag-tag
			most_tag = max(self.Stt, key = self.l_dic)
			
			chosen.append(most_tag)
			all_ele = self.Stt[most_tag]
			#delete chosen one
			del self.Stt[most_tag]
			#update Stt
			for edge in self.Stt:
				ori = self.Stt[edge]
				self.Stt[edge] = list(set(ori) - set(all_ele))

			Urem = list(set(Urem) - set(all_ele))

		#stop = timeit.default_timer()
		#print "running time:", (stop - start)
		return chosen

	def finding_holes(self,tri_taggings, chosen):
		[pre_tag,mid_tag,next_tag] = tri_taggings
		holes = []
		finding = False
		#print tri_taggings
		for tag_1 in pre_tag:
			if ' '.join(tag_1) not in chosen:
				continue
			for tag_3 in next_tag:
				if ' '.join(tag_3) not in chosen:
					continue
				for tag_2 in mid_tag:
					#print "close"
					if tag_1[1] == tag_2[0] and tag_2[1] == tag_3[0]:
						finding = True
						#print "very close"
						if ' '.join(tag_2) not in chosen:
							holes.append(' '.join(tag_2))
		#if not holes:
		#	print "edge e':", pre_tag
		#	print "edge e'':", mid_tag
		#	print "missing:",next_tag
		if finding:
			return list(set(holes))
		else:
			return 'error'

	def finding_path(self, target_tag, t_list, chosen):
		pos = 0
		path = []
		last_pos = len(t_list) - 1

		while pos <= last_pos:
			nodes = []
			for tag in t_list[pos]:
				if target_tag == tag[0]:
					if ' '.join(tag) in chosen:
						nodes.append(tag[1])
			#print "nodes", nodes
			if not nodes:
				#print "failed on:", t_list[pos:]
				#print "remainging:", path
				return []
			else:
				
				if len(nodes) == 1:
					pos += 1
					target_tag = nodes[0]
					path.append(nodes[0])
				else:
					pos += 1
					#print "current path:",path
					#print "potential nodes", nodes
					for node in nodes:
						#print "target node:", node						
						#print [node], pos, t_list[pos:]
						path_ = self.finding_path(node,t_list[pos:],chosen)
						if path_:
							#print "finding!"
							path.append(node)
							#print "path:",path
							#print "path_:",path_
							path.extend(path_)
							
							return path

		return path

	def bfs_path(self, root, t_list,chosen):
		visited, queue = set(), [root]
		q_list = collections.deque(t_list)

		while q_list:
			neighbours = q_list.popleft()
			for neighbour in neighbours:
				if neighbour[0] in queue:
					if ' '.join(neighbour) in chosen:
						visited.add(neighbour[1])
			queue = visited
			visited = set()
		print queue
		if queue == set(['END']):
			return True
		else:
			return False



	def test(self,t_list):
		whole_tag = []
		for tags in t_list:
			for tag in tags:
				if ' '.join(tag) not in whole_tag:
					whole_tag.append(' '.join(tag))
		#return self.finding_path('START',t_list,whole_tag)
		if not self.bfs_path('START', t_list,whole_tag):
			print "not finding"
	def d_bug(self, h_list, t_list,chosen):

		for hole in h_list:

			p_chosen = []
			p_not_chosen = []
			m_chosen = []
			m_not_chosen = []
			n_chosen = []
			n_not_chosen = []

			print "hole pos:", hole
			for pre_tag in t_list[hole-1]:
				if ' '.join(pre_tag) in chosen:
					p_chosen.append(pre_tag)
				else:
					p_not_chosen.append(pre_tag)

			for mid_tag in t_list[hole]:
				if ' '.join(mid_tag) in chosen:
					m_chosen.append(mid_tag)
				else:
					m_not_chosen.append(mid_tag)

			for next_tag in t_list[hole+1]:
				if ' '.join(next_tag) in chosen:
					n_chosen.append(next_tag)
				else:
					n_not_chosen.append(next_tag)

			print "chosen:"
			print "pre:", p_chosen
			print "mid:", m_chosen
			print "next:", n_chosen
			print "not chosen"
			print "pre:", p_not_chosen
			print "mid:", m_not_chosen
			print "next:", n_not_chosen

			print "-------------------------------------------------"


	def alg3(self,chosen):		
		pos = 1		
		Urem = []
		t_list = self.t_tag_list
		

		test = False
		if test:
			path = self.test(t_list)
			return path
		else:
			#path = self.finding_path('START',t_list,chosen)
			path = self.bfs_path('START', t_list,chosen)

		while not path:
			need_holes = []
			for i in range(len(self.t_tag_list)-2):
				holes = self.finding_holes([self.t_tag_list[i],self.t_tag_list[i+1],self.t_tag_list[i+2]],chosen)
				if holes:
					if holes == 'error':
						need_holes.append(i+1)
						continue
					Urem.append(i+1)
					for hole in holes:
						if (i + 1) not in self.Htt[hole]:
							self.Htt[hole].append(i+1)


			#print "number of holes:", len(self.Htt), "number of existed:", len(chosen)
			#print "pos of holes needed", need_holes

			if not self.Htt:
				print "path not available"
				self.d_bug(need_holes, self.t_tag_list, chosen)
				return []
						#print hole,Htt[hole]

			while Urem:
				most_tag = max(self.Htt, key=self.l_dic)

				chosen.append(most_tag)
				all_ele = self.Htt[most_tag]

				del self.Htt[most_tag]

				for htt in self.Htt:
					ori = self.Htt[htt]
					self.Htt[htt] = list(set(ori) - set(all_ele))
				Urem = list(set(Urem) - set(all_ele))
			print "remaining holes:", len(self.Htt), "current tag-tag:",len(chosen)
			#path = self.finding_path('START',t_list,chosen)
			path = self.bfs_path('START', t_list, chosen)
			#print "--------------------------------------------------"
			#print chosen
			#print "path:", path
			

		#print most_tag,Htt[most_tag]
		#print t_list
		#print chosen
		print path
		return path
		
		#finding holes


class GreedyJC():
	tag_dic = {}
	gra_list = []
	t_list = []
	def __init__(self, dic,gra,text):
		self.tag_dic = dic
		self.gra_list = gra
		self.t_list = text

class GreedyJE():
	tag_dic = {}
	gra_list = []
	t_list = []
	def __init__(self, dic,gra,text):
		self.tag_dic = dic
		self.gra_list = gra
		self.t_list = text

def necs_tag_out(t_list):

	for t_pair in t_list:
		p = []
		#print t_pair[0],t_pair[1]
		[tagging_ori_1,tagging_ori_2] = [dic[t_pair[0]],dic[t_pair[1]]]
		for tag_1 in tagging_ori_1:
			for tag_2 in tagging_ori_2:

				if [tag_1,tag_2] in gra_list:
					p.append([tag_1,tag_2])
				#else:
					#print "not found:",tag_1,tag_2


		if len(p) == 1:
			#if p[0] not in gra_list:
			#	print "no way...:",p[0]
			if p[0] not in gra_map:
				gra_map.append(p[0])
		else:
			t_map_list.append(p)
	print "original tagging pair:",len(t_list)
	print "single tag-tag size:",len(gra_map)
	print "after 1st selection:",len(t_map_list)

def match(list_1,list_2):
	match = 0
	for i in range(len(list_1)):
		print list_1[i][1],list_2[i]
		if list_1[i][1] == list_2[i]:
			match += 1

	print float(match)/len(list_1)
	return match/len(list_1)

def start(dic,text,gram):
	start = timeit.default_timer()
	load_dic(dic)
	load_gra(gram)
	load_text(text)

	necs_tag_out(t_list)
	#prune(t_map_list)
	#map(t_map_list,gra_map)
	stop = timeit.default_timer()
	print "running time:", (stop - start)
	#match(t_map_list, gra_list)

if __name__ == '__main__':
	#dic gra text
	args = sys.argv[1:]
	database = LoadingFiles()
	tag_dic = database.load_dic('dict')
	gra_list = database.load_gra('gram')
	t_list = database.load_text('text')
	t_tagged_list = database.load_text_tagged('text_tagged')
	#print gra_list
	start = timeit.default_timer()
	MM = GreedyMM(tag_dic,gra_list,t_list)
	path = MM.alg3(MM.alg2())
	stop = timeit.default_timer()
	print "running time:", (stop - start)
	#print path
	#print match(t_tagged_list,path)
	'''
	if len(args) != 3:
		print "use default"
		start("dict.txt","text","gram")
	else:
		start(args[0],args[1],args[2])
	'''
