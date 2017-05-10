# load data
#

#load available token with tag in database
set token := {read "dict.txt" as "<1s>"};
#load total available tags for each word
set tag := {read "keys.txt" as "<1s>"};

#load available token*tag sets
set tag_given := {read "dict.txt" as "<1s,2s>"};
#load available tag*tag sets for this bigram
set gram_given := {read "gram.txt" as "<1s,2s>"};
#load numbers of words in the training text
set index := {read "text.txt" as "<1n>" };
#load training text 
set context := {read "text.txt" as "<1n 2s>"};
#for any given position a, fetch the targetd grammar
set context_2 := {<a,b,c> in context * token with <a+1,c> in context};
#for any given position i, get the available set of token*tag
set l := {<i,tk,tg> in index * tag_given with <i,tk> in context}; 
#combine the sets of available grammars and token*tag
set ll := {<i,tk,tkn,tg,tgn> in context_2 * gram_given with <i,tk,tg> in l
						and <i+1,tkn,tgn> in l};
						
do print context;
do print ll;
var L[ll] binary;
var G[gram_given] binary;

param size:=max(index);

subto flow_in_out: forall <i> in index with i < size: (sum <a,b,c,d,e> in ll with a==i: L[a,b,c,d,e]) == 1;
subto grammar: forall <a,b,c> in context_2: forall <g1,g2> in gram_given with <a,b,c,g1,g2> in ll: G[g1,g2] >= L[a,b,c,g1,g2];

minimize cost: sum <g1,g2> in gram_given: G[g1,g2];


