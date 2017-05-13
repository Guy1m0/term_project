Optimization on MinTagPath problem

Getting Started:
These instructions will get you a copy of the project up and running on your local machine for dvelopment and testing purposes.

Prerequisites:
Since the tag dictionary derived from the open-source project NLTK, Natural Language Toolkit, builging new tag dictionary is required the package NLTK installed.

NLTK can be installed as following method:
```
sudo pip install -U nltk
```
And then, run the Python interpreter and type the commands:
```
import nltk
nltk.download()
```
Running the tests
As the default dictionary has been provided, dict.txt, the first step is parsing the text for pos-tagging.
```
python build_tag_set.py -1 filename
```
Therefore, the system will search the file in raw folder. Among these files, 24k and 2k, which contains around 24,000 or 2,000 words, might be the good option for testing and run the code as following:
```
python build_tag_set.py -1 2k
```
or use the existed wsj file
```
python build_tag_set.py -1 wsj_0001
```
After parsing, a new generated file text.txt will be updated and ready for tagging. Then please use the following code:
```
python grdy.py
```
It will show the running time of the project and save the POS-tag in the file map

For the integer programming, please run the following code to simply the procedure:
```
time scip -c 'read mm.zpl' -c opt -l filename -c quit
```
Therefore, the result will be stored in the file, filename

Testing Result:
Running the 2k file:
IP 76.056s
grdy.py 0.09s

Running the 24k file:
IP 1765s
grady.py 1.158s


Notes:
The tag format use Penn Treebank:
1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
37. $
38. ``
39. ''
40. (
41. )
42. COM$ represent ,
43. --
44. .
45. COL$ represent :
46. -NONE- word not exist in the dictionary or hard to distinguish 
