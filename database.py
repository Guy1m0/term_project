import re,sys
import pickle,nltk

from nltk.corpus import treebank
from collections import defaultdict

dic_tag = defaultdict(list)
dic_gra = defaultdict(list)

text = []
text_tagged = []

def tag_update(tag):
	if tag == ',':
		return 'COM$'
	if tag == ':':
		return 'COL$'
	return tag

def dic_2_list(d):
	text_list = []
	for token in d:
		for tag in d[token]:
			text_list.append(token + ' ' + tag)
	return text_list

def write_on_file(lis,filename,numbered = False):

	t = open(filename,"w+")
	line_num = 1
	for word in lis:
		if numbered:
			t.write(str(line_num) + ' ')
			line_num += 1
		t.write(word + '\n')

def build_dic_n_gra(ran):

	filename = "tagged/wsj_0000"
	pre_tag = ''
	for i in range(ran):
		num = str(i + 1)
		fname = filename[:-len(num)]+num+".pos"
		#print "filename:", f
		f = open(fname)
		
		for word in f.read().split():

			index = word.rfind('/')
			if index != -1:

				token = word[:index]
				tag = word[index+1:]

				if dic_tag[token] == []:
					dic_tag[token].append(tag)
				else:
					if tag not in dic_tag[token]:
						dic_tag[token].append(tag)

				if pre_tag!='':
					if dic_gra[pre_tag] == [] or tag not in dic_gra[pre_tag]:
						dic_gra[pre_tag].append(tag)
				pre_tag = tag

	write_on_file(dic_2_list(dic_tag),'dict')	
	write_on_file(dic_2_list(dic_gra),'gram')

def gen_text_and_tagged(ran, mode = 'w'):
	#t = open('text',"w+")
	#t_map = open('text_map',"w+")
	filename = "tagged/wsj_0000"
	
	for i in range(ran):
		if mode == 's':
			if i <= ran - 2:
				continue
		#print i
		num = str(i + 1)

		#could do single, but not whole
		#63
		#54
		#error_files = ['41','42','49','54','63','66','68','71']
		error_files = ['41','49','66']
		if num in error_files and mode == 'w':
			continue
		fname = filename[:-len(num)]+num+".pos"
		#print "filename:", f
		f = open(fname)
		
		for word in f.read().split():

			index = word.rfind('/')
			if index != -1:

				text.append(word[:index])
				text_tagged.append(word[index+1:])

	write_on_file(text,'text',True)
	write_on_file(text_tagged,'text_tagged',True)

if __name__ == '__main__':

	args = sys.argv[1:]
	#199: 94176
	#101: 48194
	#51: 24300
	#10: 1986

	#withou errors:
	#62: 23960
	#build_dic_n_gra(199)
	gen_text_and_tagged(int(args[0]),args[1])