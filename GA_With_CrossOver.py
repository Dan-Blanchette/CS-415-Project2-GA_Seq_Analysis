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
        self.fitness = 0
        for c in self.genome:
            if c == 'T':
                self.fitness += 1
    
    def mutation(self):
        for i in range(0,genomesize):
            if(random.uniform(0,100) < mutationprob):
                self.genome[i] = random.choice(DNAcharacters)
        self.calcFitness()

    def copy(self,source):
        self.fitness = source.fitness
        for i in range(0,genomesize):
            self.genome[i] = source.genome[i]

   # def __str__(self):
    #    output = "hi "
     #   for c in self.genome:
      #      output = output + c
      #  output += " "
      #  output += "fitness: "
      #  output += str(self.fitness)
      #  return output

popsize = 50
tourn_size = 3

class population:
    def __init__(self): # constructor - constructs a new pop object
        #print("Creating a new population")
        self.avg_fitness = 0
        self.the_pop = []
        for i in range(0,popsize):
            self.the_pop.append(individual())
    
    def calcstats(self):
        self.avg_fitness = 0
        for i in self.the_pop:
            self.avg_fitness += i.fitness
        self.avg_fitness /= popsize

    def generational(self):
        tempPop = population()
        for i in range(0,popsize,2): #  needs an even pop size
            parent = self.tournament() # select, returns an index
            parent2 = self.tournament() # select, returns an index
            tempPop.the_pop[i].copy(self.the_pop[parent])
            tempPop.the_pop[i+1].copy(self.the_pop[parent2])
            tempPop.crossover(i,i+1)
            tempPop.the_pop[i+1].mutation()
            tempPop.the_pop[i].mutation()
            #tempPop.the_pop[i].calcFitness(), already done in mutation
        #mutate them?
        #when new/temp population is full, copy new/temp pop back into the_pop
        for i in range(0,popsize):
            self.the_pop[i].copy(tempPop.the_pop[i])
        self.calcstats()
    
    def onepoint_crossover(self,p1,p2):
        crossover_point = random.randint(0,genomesize)
        for j in range(crossover_point,genomesize):
            temp = self.the_pop[p1].genome[j] # remember parent 1's character
            self.the_pop[p1].genome[j] = self.the_pop[p2].genome[j]
            self.the_pop[p2].genome[j] = temp

    def crossover(self,p1,p2): # uniform crossover
        for j in range(0,genomesize):
            if random.randint(0,100) < 10: # uniform crossover
                print(j)
                temp = self.the_pop[p1].genome[j] # remember parent 1's character
                self.the_pop[p1].genome[j] = self.the_pop[p2].genome[j]
                self.the_pop[p2].genome[j] = temp
                # temp = a
                # a = b
                # b = temp
                #self.the_pop[p1].genome[j],self.the_pop[p2].genome[j] = self.the_pop[p2].genome[j],self.the_pop[p1].genome[j]
                # a,b=b,a
                
    def tournament(self):
        best_so_far = random.randint(0,popsize-1)
        best_fitness = self.the_pop[best_so_far].fitness
        #print(best_so_far)
        for i in range(0,tourn_size - 1):
            current = random.randint(0,popsize-1)
            #print(current)
            current_fit = self.the_pop[current].fitness
            if(current_fit > best_fitness):
                best_so_far = current
                best_fitness = current_fit
        return best_so_far


p = population()
p.the_pop[0].print()
p.the_pop[1].print()
p.onepoint_crossover(0,1)
p.the_pop[0].print()
p.the_pop[1].print()



p = population()
p.calcstats()
print(p.avg_fitness)
for i in range(0,popsize):
    p.the_pop[i].print()
for i in range(0,20):
    p.generational()
    print(p.avg_fitness)
p.calcstats()
print(p.avg_fitness)
for i in range(0,popsize):
    p.the_pop[i].print()