import pandas as pd
import glob_align as ga

import plotly.express as px
import numpy as np

def make_graph(table): # table is 50x50 aligned scores
    fig = px.scatter(
        x=np.arange(50),
        y=table,
        title="individuals and alignment scores"
    )

    fig.show()

def calculate_accuracy(group1, group2, group3):
    
    ansDF = pd.read_csv('answer_key.csv', usecols=[3])

    right = 0
    wrong = 0
    for i in group1: #pop0
        if ansDF['Population'][i] == 'pop0':
            right += 1
        else:
            wrong += 1
    print(f'right {right} wrong {wrong} total: {right+wrong}')

    for i in group2: #pop1
        if ansDF['Population'][i] == 'pop1':
            right += 1
        else:
            wrong += 1
    print(f'right {right} wrong {wrong} total: {right+wrong}')

    for i in group3: #pop2
        if ansDF['Population'][i] == 'pop2':
            right += 1
        else:
            wrong += 1
    print(f'right {right} wrong {wrong} total: {right+wrong}')
    print(f'accuracy: {right/(right+wrong)}')

f = pd.read_csv("datafile.csv",usecols=[1])


table = [[0 for i in range(0,len(f))] for j in range(0,len(f))]


for i in range(0, len(f['Genome_Sequence'])):
    for j in range(0, len(f['Genome_Sequence'])):
        # if(i != j):
            val = ga.align_seq(f['Genome_Sequence'][i], f['Genome_Sequence'][j])
            table[i][j] = val

# make_graph(table)


# following code works with 76% accuracy ie identifies low mutation rate really well
import numpy as np


group1 = []
group2 = []
group3 = []

# percentage = .82
# top 35%
for i in range(0,50): # row
    for j in range(0,50): # column
        if i != j and table[i][j] != 0:
            if (table[i][j]) >= (table[i][i]*.6) :
                if i not in group1:
                    group1.append(i)
                if j not in group1:
                    group1.append(j)

for i in range(0,50):
    if i in group1:
        for j in range(0,50):
            table[i][j] = 0
group1.sort()
print(group1, len(group1))
for i in range(0,50): # row
    if i not in group1:
        val = np.mean(table[i])
        if val < table[i][i]*.35 and i not in group2:
            group2.append(i)

for i in range(0,50):
    if i in group2:
        for j in range(0,50):
            table[i][j] = 0
group2.sort()
print(group2, len(group2))

for i in range(0, 50):
    if table[i][0] != 0 and table[i][1] != 0:
        group3.append(i)

print(group3, len(group3))

calculate_accuracy(group1, group2, group3)