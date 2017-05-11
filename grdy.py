import re,sys

gra_list = []
t_list = []
dic = {}



def load_dic(filename):
	with open(filename) as f:
		lines = f.readlines()

	for line in lines:
		if line[0] not in dic:
			dic[line[0]] = [line[1]]
		else:
			dic[line[0]].append(line[1])

def load_gra(filename):
	with open(filename) as f:
		lines = f.readlines()

	for line in lines:
		pair = [line[0],line[1]]

		gra_list.append(pair)

def load_text(filename):
	with open(filename) as f:
		lines = f.readlines()
	for l in range(0:len(lines)):
		pair = [lines[l],lines[l+1]]

		t_list.append(pair)



if __name__ == '__main__':
	#dic gra text
	args = sys.argv[1:]
	if len(args) != 3:
		print "use default"
		load_dic("dict.txt")
		load_text("text.txt")
		load_gra("gram.txt")
	else:
		load_dic(args[0])
		load_gra(args[1])
		load_text(args[2])
	