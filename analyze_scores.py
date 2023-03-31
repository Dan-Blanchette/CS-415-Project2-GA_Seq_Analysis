import pandas as pd
import glob_align as ga


f = pd.read_csv("datafile.csv",usecols=[1])


table = [[0 for i in range(0,len(f))] for j in range(0,len(f))]


for i in range(0, len(f['Genome_Sequence'])):
    for j in range(0, len(f['Genome_Sequence'])):
        # if(i != j):
            val = ga.align_seq(f['Genome_Sequence'][i], f['Genome_Sequence'][j])
            table[i][j] = val

# for i in range(0,50):
#     for j in range(0,50):
#         print(table[i][j], ' ', end='')
#     print()

# with open('my_table.csv', 'a') as f:
#     for i in range(0, 50):
#         for j in range(0, 50):
#             f.write(f'{table[i][j]},')
#         f.write('\n')

# import plotly.express as px
# import numpy as np

# fig = px.scatter(
#       x=np.arange(50),
#       y=table,
#       title="individuals and align scores"
# )

# fig.show()

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

    # for j in range(0,50): # column
    #     # print(f'checking indiv {i} and {j}')
    #     if i != j and table[i][j] != 0:
    #         # print(f'{table[i][i]} - {table[i][j]} ({table[i][i] - table[i][j]}) > {table[i][i]}*.65 ({table[i][i]*.85})')
    #         if (table[i][j]) <= (table[i][i]*.2) :
    #             # potential match for group 1
    #             # print("     match found")
    #             if i not in group2 and i not in group1:
    #                 group2.append(i)
    #                 # print(f'        added {i}')
    #             if j not in group2 and j not in group1:
    #                 group2.append(j)

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


ansDF = pd.read_csv('answer_key.csv', usecols=[3])

pop0_counts = 0
pop1_counts = 0
pop2_counts = 0
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

