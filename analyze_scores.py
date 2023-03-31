import pandas as pd
import glob_align as ga

import plotly.express as px
import numpy as np
import copy

def make_graph(table): # table is 50x50 aligned scores
    copy_table = copy.deepcopy(table)
    fig = px.scatter(
        x=np.arange(50),
        y=copy_table,
        title="Individuals and Alignment Scores"
    )
    fig.update_layout(showlegend=False)
        
    # fig.show()
    fig.write_image("indiv_align_scores.png")

def make_group_graph(table, group, population='population_1'):
    npt = np.array(table)
    npg = np.array(group)

    fig = px.scatter(
        npt[npg],
        
        title=population + " Alignment Scores")

    fig.update_layout(showlegend=False)
        
    fig.show()
    fig.write_image(population + "_align_scores.png")

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

    return right/(right+wrong)

def create_table():
    f = pd.read_csv("datafile.csv",usecols=[1])

    table = [[0 for i in range(0,len(f))] for j in range(0,len(f))]


    for i in range(0, len(f['Genome_Sequence'])):
        for j in range(0, len(f['Genome_Sequence'])):
            # if(i != j):
                val = ga.align_seq(f['Genome_Sequence'][i], f['Genome_Sequence'][j])
                table[i][j] = val
    return table

def analyze_scores(table):
    # following code works with 76% accuracy ie identifies low mutation rate really well

    group1 = []
    group2 = []
    group3 = []

    # top 40%
    for i in range(0,50): # row
        for j in range(0,50): # column
            if i != j and table[i][j] != 0:
                if (table[i][j]) >= (table[i][i]*.6) :
                    if i not in group1:
                        group1.append(i)
                    if j not in group1:
                        group1.append(j)
    group1.sort()
    
    # bottom 35%
    print(group1, len(group1))
    for i in range(0,50): # row
        if i not in group1:
            val = np.mean(table[i])
            if val < table[i][i]*.35 and i not in group2:
                group2.append(i)
    group2.sort()
    
    # everything else goes in group 3
    for i in range(0, 50):
        if i not in group1 and i not in group2:
            group3.append(i)

    return group1, group2, group3


def main():
    table = create_table()
    group1, group2, group3 = analyze_scores(table)
    calculate_accuracy(group1, group2, group3)
    make_graph(table)
    make_group_graph(table, group1, "population_0")
    make_group_graph(table, group2, "population_1")
    make_group_graph(table, group3, "population_2")
    make_group_graph(table, group2+group3, "populations_1_2")

if __name__ == "__main__":
    main()