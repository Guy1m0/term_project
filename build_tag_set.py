import re,sys
import pickle,nltk

from nltk.corpus import treebank

#grammar list
gra_list = []
dic = {}
#global dic

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

dic_ = ['N.V.','F.H.','J.','Co.','N.M.','Cos.','Ms.','Ltd.','etc.','F.W.',
	'Ky.','K.','H.N.','S.I.','N.C.','L.','D.C.','p.m.','M.','Lt.',
	'J.L.','A.C.','Miss.','M.D.','N.','U.S.S.R.','Sino-U.S.','Prof.','Minn.','Wis.',
	'O.','Va.','Ala.','F.','v.','W.D.','vs.','L.P.','N.Y.','U.K.',
	'Dec.','Mich.','Feb.']
dic_spc = [u'L.', u'D.C.', u'.', u'p.m.', u'M.', u'Lt.', u'J.L.', u'A.C.', u'Miss.', u'M.D.', u'N.', u'U.S.S.R.', u'Sino-U.S.', u'Prof.', u'Minn.', u'Wis.', u'O.', u'Va.', u'Ala.', u'F.', u'Oct.', u'v.', u'W.D.', u'vs.', u'L.P.', u'N.Y.', u'U.K.', u'Dec.', u'Mich.', u'Feb.', u'Tenn.', u'Ill.', u'Ga.', u'S.', u'Pa.', u'Ore.', u'Sept.', u'non-U.S.', u'R.', u'Inc.', u'P.', u'Rep.', u'La.', u'Gov.', u'L.A.', u'W.N.', u'...', u'Messrs.', u'A.', u'T.', u'Mrs.', u'No.', u'Mr.', u'R.D.', u'Rev.', u'N.H.', u'Sen.', u'W.R.', u'Ariz.', u'Corp.', u'Aug.', u'B.', u'E.C.', u'Jr.', u'St.', u'N.J.', u'U.S.A.', u'J.P.', u'Nev.', u'C.', u'Colo.', u'Mass.', u'14.', u'A.D.', u'D.', u'W.', u'Calif.', u'Wash.', u'Dr.', u'E.', u'Fla.', u'Jan.', u'R.P.', u'C.J.B.', u'Mo.', u'A.L.', u'S.p.A.', u'G.', u'Z.', u'Del.', u'R.I.', u'Sr.', u'Pty.', u'Conn.', u'Md.', u'H.', u'Nov.', u'Ind.', u'E.W.', u'U.S.', u'I.', u'N.V.', u'F.H.', u'J.', u'Co.', u'N.M.', u'Cos.', u'Ms.', u'Ltd.', u'etc.', u'F.W.', u'Ky.', u'K.', u'H.N.', u'S.I.', u'N.C.']

def build_dict(size):

	if size == -1:
		modify_raw(filename)
		return
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
	#cs = []
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
		#if token[-1] == '.':
			#cs.append(token)
		for i in range(1,47):
			if tag[:2] == " 1":
				line = token + " " + keys_[i-1] + "\n"
				f.write(line)
			tag= tag[2:]
			#f.write(line)
	#fcfg

	f.write("s' POS\n")

	#print cs
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

	#fcfg
	e.write("WP VBN\n")

	e.write("WP VB\n")
	e.write("WP VBD\n")
	e.write("WP VBP\n")
	e.close()
	#global dic

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
			if word.split() == "":
				continue
			#print word
			if word == ".START" or word == "\n":
				continue
			#print "w:",word
			word = re.sub('[^a-zA-Z0-9\-\.\'\:\!\&\,\/\$]+','',word)
			index += 1
			wr += str(index) + " "
			end_sen = False
			#some special case 
			if word[-1] == '.' and word not in dic_spc:
				#print word
				end_sen = True
				word = word[:-1]

			if '/' in word:
				inx = word.find('/')
				#print inx
				wr += word[:inx] + "\n"
				word = word[inx+1:]
				index += 1
				wr += str(index) + " "

			if '$' in word:
				inx = word.find('$')
				#print inx
				wr += word[:inx + 1] + "\n"

				#wr += str(index) + " "
				#wr += '$' + "\n"
				#index += 1

				word = word[inx+1:]
				index += 1
				wr += str(index) + " "

			if ',' == word[-1]:
				#print ",:", word[:-1]

				wr += word[:-1]+"\n"
				index += 1
				wr += str(index) + " "
				
				wr += 'COM$\n'
				word = ""
				#print "wr:",wr
				

			if ("'s" in word[-2:] or "s'" == word[-2:]) and len(word) > 2:
				#print len(word)
				wr += word[:-2] + "\n"
				
				index += 1
				wr += str(index) + " "
				wr += word[-2:] + "\n"
				word = ""
			
			if "n't" in word:
				
				wr += word[:-3] + "\n"
				
				index += 1
				wr += str(index) + " "
				wr += "n't\n"
				word = ""

			if "'re" in word:
				
				wr += word[:-3] + "\n"
				
				index += 1
				wr += str(index) + " "
				wr += "'re\n"
				word = ""
				
			if word != "":

				wr += word + "\n"			
				#print "word:",word
				#print len(dic)
				#if word[:-1] in dic:
				#if unicode(word[:-1],"utf-8") in dic: #and word.find('.')==(len(word) - 1):
			if end_sen:
				#wr += word[:-1] + "\n"
				index += 1
				wr += str(index) + " .\n"
				continue
			
			'''
			if ':' in word or ';' in word:
				wr += word[:-1]+"\n"
				wr += 'COL$\n'
				continue
			'''

		#print "wr:", wr
		if len(wr) > 0:
			g.write(wr)
			#g.write(wr[:-2] + "\n")
			#index += 1
			#g.write(str(index) + " ")
			#g.write('.\n')
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

	#modify_raw(args[1])
	'''
	datasets = treebank.tagged_words()
	for data in datasets:
		if data[0] == 'new':
			print data[0],data[1]
	'''


