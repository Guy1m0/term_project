# Constraints for n^2 x n^2 Sudoku puzzles.

param n := 3;
param dim := n*n;
set R := {1..dim};  # row indices
set C := {1..dim};  # col indices
set D := {1..dim};  # possible digits
set B := {1..n}*{1..n};   # block-internal indices
set OB := {<r> in R with r mod n == 1}*{<c> in C with c mod n == 1};
var x[R*C*D] binary;  # does digit D appear at coordinates (R,C)?

# There are constraints, but nothing to maximize or minimize.

subto uniq: forall <r,c> in R*C: 
	(sum <d> in D: x[r,c,d]) == 1;   # exactly one digit per cell
subto row: forall <r> in R: forall <d> in D: 
	(sum <c> in C: x[r,c,d]) == 1;   # each digit appears once per row
subto col: forall <c,d> in C * D: 
	(sum <r> in R: x[r,c,d]) == 1;   # each digit appears once per column
subto block: forall <r,c> in OB: forall <d> in D: 
	(sum <br,bc> in B: x[(r + br - 1), (c + bc - 1), d]) == 1; # each digit appears once per block

# Some of the digits are given.  Read these from file sudoku.txt and
# further constrain the solution to match these.

set Givens := { read "sudoku.txt" as "<1n,2n,3n>" comment "#" };
subto givens: forall <r,c,d> in Givens: x[r,c,d]==1;
