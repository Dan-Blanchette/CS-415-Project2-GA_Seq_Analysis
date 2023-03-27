# --------
# @file     glob_align.py
# @author   Jordan Reed, Dan Blanchette, Taylor Martin
# @date     March 2023
# @class    CS 415 Computational Biology
#
# @brief    This file is for the gloabl alignment algorithm.
# --------------------

import blosum

def printmatrix(m,pad = 4): 
    for r in m:
        for d in r:
            print(f"{str(d):>{pad}}", end = "")
        print()

seq1 = "TTAGCCAGT"
seq2 = "TAAGACATTTTAC"

gappenalty = -8

scoringmatrix = [[0 for i in range(0,len(seq1)+1)] for j in range(0,len(seq2)+1)]
directionmatrix = [["." for i in range(0,len(seq1)+1)] for j in range(0,len(seq2)+1)]


# fill first row with gap penalty
for i in range(0,len(scoringmatrix[0])):
    scoringmatrix[0][i] =  i*gappenalty
    directionmatrix[0][i] = "\u2190" # horizontal

# firll first column
for i in range(0,len(scoringmatrix)):
    scoringmatrix[i][0] = i*gappenalty
    directionmatrix[i][0]  = "\u2191" # vertical

# fill in rest of table
for r in range(1, len(scoringmatrix)):
    for c in range(1, len(scoringmatrix[0])):
        vert = scoringmatrix[r-1][c] + gappenalty
        horz = scoringmatrix[r][c-1] + gappenalty
        diag = scoringmatrix[r-1][c-1]

        diag += blosum.blosum50[blosum.aminoDictionary[seq2[r-1]]][blosum.aminoDictionary[seq1[c-1]]]
        
        scoringmatrix[r][c] = max(vert,horz,diag)
        #directionmatrix[r][c] = "v or h or d"
        if diag >= horz and diag >= vert:
            directionmatrix[r][c] = "\u2196"
        if horz > diag and horz > vert:
            directionmatrix[r][c] = "\u2190"
        if vert > diag and vert > horz:
            directionmatrix[r][c] = "\u2191"

printmatrix(scoringmatrix)
print(seq1)
print(seq2)

printmatrix(directionmatrix)

# aligning sequences

aligned1 = ""
aligned2 = ""
pos1 = len(seq1)
pos2 = len(seq2)

while pos1 > 0 or pos2 > 0:
    if directionmatrix[pos2][pos1] == '\u2196': # diagonal
        aligned1 += seq1[pos1-1]
        aligned2 += seq2[pos2-1]
        pos1 -= 1
        pos2 -=1
    elif directionmatrix[pos2][pos1] == '\u2190': # horizontal
        aligned1 += seq1[pos1-1]
        aligned2 += "-"
        pos1 -= 1
    elif directionmatrix[pos2][pos1] == '\u2191': # vertical
        aligned1 += "-"
        aligned2 += seq2[pos2-1]
        # pos1 -= 1
        pos2 -=1
    else:
        print("something is wrong")


aligned1 = aligned1[::-1]
aligned2 = aligned2[::-1]

print(aligned1)
print(aligned2)