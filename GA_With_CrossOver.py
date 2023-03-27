# --------
# @file     GA_With_CrossOver.py
# @author   Jordan Reed, Dan Blanchette, Taylor Martin
# @date     March 2023
# @class    CS 415 Computational Biology
#
# @brief    This file contains the classes for defining an individual and a population.
# --------------------

import random
import copy

genomesize = 50
DNAcharacters = 'TGCA'
mutationprob = 2
class individual:
    def __init__(self): # constructor - constructs a new individual object
        #print("Creating a new individual")
        self.fitness = 0
        self.genome = []
        for i in range(0,genomesize):
            self.genome.append(random.choice(DNAcharacters))
        self.calcFitness()

    def print(self):
        for c in self.genome:
            print(c,end = "")
        print("  fitness:" + str(self.fitness))

    def calcFitness(self):   # for now: number of T's
        """
        Calculates a fitness score based on the individual characters of the genome string.
        T = 1 pt
        A = 2 pts
        G = 3 pts
        C = 4 pts

        Interested in adding condition of 'single' chars having a point value. If it's a repeated char, i.e. 'TT', no point value is awarded.
        This is not necessary.
        """
        self.fitness = 0

        for c in self.genome:
            if c == 'T':
                self.fitness += 1
            elif c == 'A':
                self.fitness += 2
            elif c == 'G':
                self.fitness += 3
            else:
                self.fitness += 4
    
    def mutate(self, mRate=2):
        """
        Basic mutation function that will walk through the genome and have a chance to mutate each character based on the parameter given.

        :param mRate: integer between 0 and 100; chance a character can be mutated; defaults to 2
        """
        for i in range(0, len(self.genome)):
            if random.uniform(0,100) < mRate:
                self.genome[i] = random.choice(DNAcharacters)
        
        self.calcFitness()
    
    def mult_mutate(self, highRate=80, lowRate=2):
        """
        Basic mutation function that will walk through the genome and have a chance to mutate each character based on the parameter given.

        :param mRate: integer between 0 and 100; chance a character can be mutated; defaults to 2
        """
        current_rate = lowRate

        for i in range(0, len(self.genome)):
            if random.uniform(0,100) < 25:
                if current_rate == lowRate:
                    current_rate = highRate
                else:
                    current_rate = lowRate

            if random.uniform(0,100) < current_rate:
                self.genome[i] = random.choice(DNAcharacters)
        
        self.calcFitness()

    def copy(self,source):
        self.fitness = source.fitness
        for i in range(0, genomesize):
            self.genome[i] = source.genome[i]

    def __str__(self):
        string = ""

        for i in range(0, len(self.genome)):
            string += self.genome[i]
        
        # string += " fitness: " + str(self.fitness)

        return string

# set the population size
popsize = 50
# size of participants in the tournament for selection (low selection pressure at 3)
tourn_size = 3

class population:
    def __init__(self): # constructor - constructs a new pop object
        #print("Creating a new population")
        self.avg_fitness = 0
        self.the_pop = []

        for i in range(0,popsize):
            self.the_pop.append(individual())
        
        self.calcstats()
    
    def calcstats(self):
        self.avg_fitness = 0
        for i in self.the_pop:
            self.avg_fitness += i.fitness
        self.avg_fitness /= popsize

    def single_mutate_generational(self, mutate_rate = 2):
        """
        models sexual reproduction in a generational model
        """
        tempPop = population()
        for i in range(0,popsize,2): #  needs an even pop size
            parent = self.tournament() # select, returns an index
            parent2 = self.tournament() # select, returns an index

            tempPop.the_pop[i].copy(self.the_pop[parent])
            tempPop.the_pop[i+1].copy(self.the_pop[parent2])

            tempPop.crossover(i,i+1)

            tempPop.the_pop[i+1].mutate(mutate_rate)
            tempPop.the_pop[i].mutate(mutate_rate)
            
        #when new/temp population is full, copy new/temp pop back into the_pop
        for i in range(0,popsize):
            self.the_pop[i].copy(tempPop.the_pop[i])
        self.calcstats()
    
    def mult_mutate_generational(self, highRate=80, lowRate=2):
        """
        models sexual reproduction in a generational model
        """
        tempPop = population()
        for i in range(0,popsize,2): #  needs an even pop size
            parent = self.tournament() # select, returns an index
            parent2 = self.tournament() # select, returns an index

            tempPop.the_pop[i].copy(self.the_pop[parent])
            tempPop.the_pop[i+1].copy(self.the_pop[parent2])

            tempPop.crossover(i,i+1)

            tempPop.the_pop[i+1].mult_mutate(highRate, lowRate)
            tempPop.the_pop[i].mult_mutate(highRate, lowRate)
            
        #when new/temp population is full, copy new/temp pop back into the_pop
        for i in range(0,popsize):
            self.the_pop[i].copy(tempPop.the_pop[i])
        self.calcstats()

    def crossover(self,p1,p2): # uniform crossover
        for i in range(0,genomesize):
            if random.randint(0,100) < 10: # uniform crossover
                # swap chars in parents at same locations
                self.the_pop[p1].genome[i], self.the_pop[p2].genome[i] = self.the_pop[p2].genome[i], self.the_pop[p1].genome[i]
        
        self.the_pop[p1].calcFitness()
        self.the_pop[p2].calcFitness()
                
    def tournament(self):
        best_so_far = random.randint(0,popsize-1)
        best_fitness = self.the_pop[best_so_far].fitness
        
        for i in range(0,tourn_size - 1):
            current = random.randint(0,popsize-1)
            current_fit = self.the_pop[current].fitness

            if(current_fit > best_fitness):
                best_so_far = current
                best_fitness = current_fit
        
        return best_so_far
    
    def __str__(self):
        string = ""

        for i in range(0, len(self.the_pop)):
            string += self.the_pop[i].__str__() + "\n"
        
        string += f'avg fitness: {self.avg_fitness}'

        return string

    def copy(self, source):
        self.avg_fitness = source.avg_fitness
        for i in range(0, len(self.the_pop)):
            self.the_pop[i].copy(source.the_pop[i])
'''
create data for the population and individual
'''


def create_highRate_pop(pop):
    # print(pop.avg_fitness)
    # print(pop)
    for i in range(0, 20):
        pop.single_mutate_generational(80)
    #     print(pop.avg_fitness)
    print(pop)

def create_lowRate_pop(pop):
    # print(pop.avg_fitness)
    # print(pop)
    for i in range(0, 20):
        pop.single_mutate_generational(2)
    #     print(pop.avg_fitness)
    print(pop)

def create_multRate_pop(pop):
    # print(pop.avg_fitness)
    # print(pop)
    for i in range(0, 20):
        pop.mult_mutate_generational(highRate=85, lowRate=5)
    #     print(pop.avg_fitness)
    print(pop)


pops = []
pops.append(population())
pops.append(population())
pops.append(population())
pops[1].copy(pops[0])
pops[2].copy(pops[0])

print("low rate")
create_lowRate_pop(pops[0])

print("high rate")
create_highRate_pop(pops[1])

print("mult rate")
create_multRate_pop(pops[2])

data = {'Genome_Sequence': [], 'Avg_Fitness': [], 'Population': []}

for i in range(0,50):
    popChoice = random.randint(0,2)
    data['Genome_Sequence'].append(pops[popChoice].the_pop[i])
    data['Avg_Fitness'].append(pops[popChoice].avg_fitness)
    data['Population'].append(f'pop{popChoice}')

import pandas as pd

df1 = pd.DataFrame(data={'Genome_Sequence': data['Genome_Sequence'], 'Avg_Fitness': data['Avg_Fitness'], 'Population': data['Population']})

df1.to_csv("answer_key.csv")
df1.to_csv("datafile.csv", columns=['Genome_Sequence'])
