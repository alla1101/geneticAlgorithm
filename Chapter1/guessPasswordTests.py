import datetime
import genetic
import unittest
import random

def get_fitness(guess,target):
    return sum(1 for expected, actual in zip(target,guess) if expected==actual)

def display(candidate,startTime):
    timeDiff=datetime.datetime.now()- startTime
    print("{0}\t{1}\t{2}".format(candidate.Genes,candidate.Fitness,str(timeDiff)))

class GuessPasswordTests(unittest.TestCase):

    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    
    def test_Random(self):
        length=50
        target=''.join(random.choice(self.geneset) for _ in range(length))
        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)
 
    def guess_password(self,target):
        startTime = datetime.datetime.now()

        def fnGetFitness(candidate):
            return get_fitness(candidate,target)

        def fnDisplay(candidate):
            display(candidate,startTime)

        optimalFitness=len(target)
        best=genetic.get_best(fnGetFitness,len(target),optimalFitness,self.geneset,fnDisplay)

        self.assertEqual(best.Genes,target)
        
if __name__=='__main__':
    unittest.main()