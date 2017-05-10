set token := {read "dict.txt" as "<1s>"};
set key := {1..46};

set tag_given := {read "dict.txt" as "<1s,2n,3n>"};
set gram_given := {read "gram.txt" as "<1s,2s>"};

var dict[token*key] binary;
var gram[key*key] binary;


