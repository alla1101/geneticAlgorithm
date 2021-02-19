import sys;
sys.path.append("..");
import Library.genetic as genetic;
import math,random,datetime,unittest;

def get_fitness(genes,target):
    sum=0;
    for i in range(0,len(target) ):
        if(str(genes[i]) == target[i]):
            sum+=1;
    return sum;

def display(candidate,startTime):
    timeDiff=datetime.datetime.now() - startTime;
    print("{0}\t{1}\t{2}".format( ''.join( str(i) for i in candidate.Genes),str(candidate.Fitness),str(timeDiff) ) );

class OneMaxTests(unittest.TestCase):
    
    geneSet=None;
    
    def test(self,length=100):
        self.geneSet=[0,1];
        target="1"*100;
        self.guess_password(target);


    def guess_password(self,target):
        startTime=datetime.datetime.now();

        def fnGetFitness(genes):
            return get_fitness(genes,target);        
        
        def fnDisplay(genes):
            display(genes,startTime);

        optimalFitness=len(target);
        
        best=genetic.get_best(
            fnGetFitness,
            len(target),
            optimalFitness,
            self.geneSet,
            fnDisplay
        );

        self.assertEqual(''.join(str(i) for i in best.Genes),target);
        print("  ");

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test(4000) );

if __name__ == '__main__':
    unittest.main();