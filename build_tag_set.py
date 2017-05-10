import re,sys
import pickle,nltk

from nltk.corpus import treebank

#grammar list
gra_list = []
dic = {}

keys = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS',
	'MD','NN','NNP','NNPS','NNS','PDT','POS','PRP','PRP$','RB',
	'RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN',
	'VBP','VBZ','WDT','WP','WP$','WRB','$','``',"''",'(',
	')',',','--','.',':','-NONE-']

keys_ = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS',
	'MD','NN','NNP','NNPS','NNS','PDT','POS','PRP','PRP$','RB',
	'RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN',
	'VBP','VBZ','WDT','WP','WP$','WRB','$','``',"''",'(',
	')','COM$','--','.','COL$','-NONE-']

def build_dict(size):
	datasets = treebank.tagged_words()
	if size > 0:
		datasets = datasets[:size]

	gra = []
	for data in datasets:
		token = data[0]
		tag = data[1]
		
		add_new_token(token,tag)

		if len(gra) == 0:
			gra = tag
		else:
			if [gra,tag] not in gra_list:
				gra_list.append([gra,tag])
			#else:
				#print "find mult", [gra,tag]
			gra = tag

	print "grammar variables:",len(gra_list)
	print "dic variables:", len(dic)

	if ',' in dic:
		dic['COM$'] = dic[',']
		del dic[',']
	if ':' in dic:
		dic['COL$'] = dic[':']
	
		del dic[':']

	write_on_file()
	#print gra_list
	#print_token()
	#print dic


def add_new_token(token,tag):
	if token in dic:
		dic[token] = change_tag(dic[token],tag)
	else:
		dic[token] = change_tag('',tag)

def change_tag(ori,tag):
	new_tag = ''
	for key in keys:
		if tag == key:
			new_tag = new_tag + ' 1'
			if ori != '':
				ori = ori[2:]
			continue

		if ori == '':
			new_tag = new_tag + ' 0'
		else:
			new_tag = new_tag + ori[:2]
			ori = ori[2:]
	return new_tag

def write_on_file():
	g = open('keys.txt',"w+")
	for key in keys:
		if key == ',':
			key = 'COM$'
		if key == ':':
			key = 'COL$'
		g.write(key + "\n")
	g.close()

	f = open('dict.txt',"w+")
	for token,tag in dic.iteritems():
		for i in range(1,47):
			if tag[:2] == " 1":
				line = token + " " + keys_[i-1] + "\n"
				f.write(line)
			tag= tag[2:]
			#f.write(line)
	f.close()

	e = open('gram.txt',"w+")
	for gra in gra_list:
		#print gra

		line = tag_update(gra[0]) + " " + tag_update(gra[1])
		'''
		for key in keys:
			if gra[0] == key or gra[1] == key:
				line += ' 1'
			else:
				line += ' 0'
		'''
		line += "\n"
		e.write(line)
	e.close()

def tag_update(tag):
	if tag == ',':
		return 'COM$'
	if tag == ':':
		return 'COL$'
	return tag

def modify_raw(filename):
	g = open('text.txt',"w+")
	with open("raw/" + filename) as f:
		lines = f.readlines()
	index = 0
	#print lines
	for line in lines:

		if line == "\n":
			continue

		wr = ""
		#print line
		for word in line.split():

			#print word
			if word == ".START" or word == "\n":
				continue

			index += 1
			wr += str(index) + " "
			if ',' in word:
				wr += word[:-1]+"\n"
				index += 1
				wr += str(index) + " "
				
				wr += 'COM$\n'
				continue
			'''
			if ':' in word or ';' in word:
				wr += word[:-1]+"\n"
				wr += 'COL$\n'
				continue
			'''
			wr += word + "\n"
		#print "wr:", wr
		if len(wr) > 0:
			g.write(wr[:-2] + "\n")
			index += 1
			g.write(str(index) + " ")
			g.write('.\n')
	f.close()
	g.close()




def print_token():
	for token,tag in dic.iteritems():
		print token,":",
		for key in keys:
			#print tag[:2]
			if tag[:2] == ' 1':
				print key,
			tag = tag[2:]
		print ""

if __name__ == '__main__':

	args = sys.argv[1:]
	if args[0] == '0':
		build_dict(0)
	elif args[0] == '-1':
		pass
	else:
		build_dict(int(args[0]))


	modify_raw(args[1])
	'''
	datasets = treebank.tagged_words()
	for data in datasets:
		if data[0] == 'new':
			print data[0],data[1]
	'''


