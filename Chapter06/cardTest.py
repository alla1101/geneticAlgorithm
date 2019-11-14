import sys
sys.path.append("..")

import datetime
import Library.genetic as genetic
import unittest
import operator
import functools
import  random

def mutate(genes,geneset):
    if len(genes) == len(set(genes)):
        count=random.randint(1,4)
        while count > 0:
            count-=1 
            indexA,indexB=random.sample(range(len(genes)),2)
            genes[indexA],genes[indexB]=genes[indexB],genes[indexA]
    else:
        indexA=random.randrange(0,len(genes))
        indexB=random.randrange(0,len(geneset))
        genes[indexA]=geneset[indexB]
def get_fitness(genes):
    group1Sum=sum(genes[0:5])    
    group2Product=functools.reduce(operator.mul,genes[5:10])
    duplicateCount=(len(genes)-len(set(genes)))
    return Fitness(group1Sum,group2Product,duplicateCount)

def display(candidate,startTime):
    timeDiff=datetime.datetime.now()-startTime
    print(
        "{0} - {1}\t{2}\t{3}".format(
            ', '.join(map(str,candidate.Genes[0:5])),
            ', '.join(map(str,candidate.Genes[5:10])),
            candidate.Fitness,
            str(timeDiff)
        )
    )

class Fitness:
    summation=None
    product=None
    TotalDifference = None
    duplicates=None
    def __init__(self, summation,Product,duplicates):
        self.product=Product
        self.summation=summation
        sumDifference = abs(36 - summation)
        productDifference = abs(360 - Product)
        self.TotalDifference = sumDifference + productDifference
        self.duplicates=duplicates
    def __gt__(self,other):
        if self.duplicates != other.duplicates:
            return self.duplicates < other.duplicates
        return self.TotalDifference < other.TotalDifference
    def __str__(self):
        return "sum: {0} prod: {1} dups: {2}".format(
            self.summation,
            self.product,
            self.duplicates
        )

class CardTest(unittest.TestCase):
    def test(self):
        geneset=[i+1 for i in range(10)]
        startTime=datetime.datetime.now()

        def fnGetfitness(genes):
            return get_fitness(genes)
        def fnDisplay(candidate):
            display(candidate,startTime)
        def fnMutate(genes):
            mutate(genes,geneset)

        optimalFitness=Fitness(36,360,0)

        best=genetic.get_best(fnGetfitness, len(geneset), optimalFitness, geneset, fnDisplay,fnMutate)
        
        self.assertTrue(not optimalFitness > best.Fitness)


if __name__=='__main__':
    unittest.main()