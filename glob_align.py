def printmatrix(m,pad = 4): 
    for r in m:
        for d in r:
            print(f"{str(d):>{pad}}", end = " ")
        print()

seq1 = "TTAGCCAGT"
seq2 = "TAAGACATTTTAC"
gappenalty = -8
scoringmatrix = [[00 for i in range(0,len(seq1)+1)] for j in range(0,len(seq2)+1)]
directionmatrix = [["." for i in range(0,len(seq1)+1)] for j in range(0,len(seq2)+1)]
print(scoringmatrix)
scoringmatrix[0][1] = 77
print(scoringmatrix)
printmatrix(scoringmatrix)

for i in range(0,len(scoringmatrix[0])):
    scoringmatrix[0][i] =  i*gappenalty
    directionmatrix[0][i] = "h "
for i in range(0,len(scoringmatrix)):
    scoringmatrix[i][0] = i*gappenalty
    directionmatrix[i][0]  = "v "

for r in range(1,len(scoringmatrix)):
    for c in range(1,len(scoringmatrix[r])):
        vert = scoringmatrix[r-1][c] + gappenalty
        horz = scoringmatrix[r][c-1] + gappenalty
        diag = scoringmatrix[r-1][c-1]
        if(seq1[c-1] == seq2[r-1]):
            diag += 10
        else:
            diag -= 10
        scoringmatrix[r][c] = max(vert,horz,diag)
        #directionmatrix[r][c] = "v or h or d"
        if diag >= horz and diag >= vert:
            directionmatrix[r][c] = "\u2196"
        if horz > diag and horz > vert:
            directionmatrix[r][c] = "\u2190"
        if vert > diag and vert > horz:
            directionmatrix[r][c] = "\u2191"

printmatrix(scoringmatrix,4)
print(seq1)
print(seq2)

printmatrix(directionmatrix,0)