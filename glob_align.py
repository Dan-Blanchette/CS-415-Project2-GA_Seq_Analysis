# --------
# @file     glob_align.py
# @author   Jordan Reed, Dan Blanchette, Taylor Martin
# @date     March 2023
# @class    CS 415 Computational Biology
#
# @brief    This file is for the gloabl alignment algorithm.
# --------------------

import blosum
import os

def printmatrix(m,pad = 4): 
    for r in m:
        for d in r:
            print(f"{str(d):>{pad}}", end = "")
        print()

seq1 = "TTAGCCAGT"
seq2 = "TAAGACATTTTAC"


def align_seq(seq1, seq2):
    gap_penalty = -8
    scoring_matrix = [[0 for i in range(0,len(seq1)+1)] for j in range(0,len(seq2)+1)]
    direction_matrix = [["." for i in range(0,len(seq1)+1)] for j in range(0,len(seq2)+1)]

    # fill first row with gap penalty
    for i in range(0,len(scoring_matrix[0])):
        scoring_matrix[0][i] =  i*gap_penalty
        direction_matrix[0][i] = "\u2190" # horizontal

    # fill first column
    for i in range(0,len(scoring_matrix)):
        scoring_matrix[i][0] = i*gap_penalty
        direction_matrix[i][0]  = "\u2191" # vertical

    # fill in rest of table
    for r in range(1, len(scoring_matrix)):
        for c in range(1, len(scoring_matrix[0])):
            vert = scoring_matrix[r-1][c] + gap_penalty
            horz = scoring_matrix[r][c-1] + gap_penalty
            diag = scoring_matrix[r-1][c-1]

            diag += blosum.blosum50[blosum.aminoDictionary[seq2[r-1]]][blosum.aminoDictionary[seq1[c-1]]]
            
            final_value = max(diag, vert, horz)
            scoring_matrix[r][c] = final_value

            if final_value == diag:
                direction_matrix[r][c] = '\u2196' # look up unicode for symbols
            elif final_value == horz:
                direction_matrix[r][c] = '\u2190'
            else:
                direction_matrix[r][c] = '\u2191'

    # printmatrix(scoring_matrix)
    # print(seq1)
    # print(seq2)

    # printmatrix(direction_matrix)

    # aligning sequences

    aligned1 = ""
    aligned2 = ""
    pos1 = len(seq1)
    pos2 = len(seq2)

    while pos1 > 0 or pos2 > 0:
        if direction_matrix[pos2][pos1] == '\u2196': # diagonal
            aligned1 += seq1[pos1-1]
            aligned2 += seq2[pos2-1]
            pos1 -= 1
            pos2 -=1
        elif direction_matrix[pos2][pos1] == '\u2190': # horizontal
            aligned1 += seq1[pos1-1]
            aligned2 += "-"
            pos1 -= 1
        elif direction_matrix[pos2][pos1] == '\u2191': # vertical
            aligned1 += "-"
            aligned2 += seq2[pos2-1]
            # pos1 -= 1
            pos2 -=1
        else:
            print(f"something is wrong {pos1} {pos2}")


    aligned1 = aligned1[::-1]
    aligned2 = aligned2[::-1]

    # print(aligned1)
    # print(aligned2)

    return scoring_matrix[len(seq2)][len(seq1)]

# val = align_seq(seq1, seq2)
# print(val)