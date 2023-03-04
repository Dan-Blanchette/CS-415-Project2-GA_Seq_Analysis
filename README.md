# CS415 Computation Biology: Sequence Analysis

## Project #2 Genetic Algorithm and Sequence Analysis


## Proposal:

### Project 2a: Genetic Algorithm and Sequence Alignment
### Jordan Reed
### Dan Blanchette
### Taylor Martin
### March 8, 2023
### Project Description
We are going to run experiments on multiple populations with different mutation
rates for each population. One population will have a high mutation rate,
one will have a low mutation rate, and one will have a mix of high and low
mutation rates (the high mutation rate will target certain codons). The mixed
population could be done on a codon basis or on an individual basis. This means
a population could have individuals with high and low mutation rates, or an
individual could have low or high mutation rates. At the end of the generational
model, we’ll take a subset of each population, mix it all up and see if we can
figure out what population each individual is from.

### Fitness Calculation

We plan to encode using nucleic acids like the first assignment. Our fitness
function we plan to use is very simple: each character will be assigned a point
value and the score will be added up. For example, a ’T’ will be worth 1 point,
’A’ will be worth 2 points, ’G’ is worth 3 points, and ’C’ will be worth 4 points.
Alignment Method

In order to figure out which individual is from which population, we will use
the Blosum50 matrix with a global alignment approach.

### Expected Results
The population with the lowest mutation rate we expect to be identified the
easiest, as it will likely be closest to the our fitness function results (almost all
’C’s). We expect the highest mutation rate to be the hardest to identify the
individuals from, as the individual codons will be the most randomized.
2
