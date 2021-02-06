import sys;
sys.path.append("..");
import Library.genetic as genetic;
import math,random,datetime,unittest;

def get_fitness(genes,target):
    return sum( 
        1 for expected, actual in zip(target,genes) if expected == actual 
    );

def display(candidate,startTime):
    timeDiff=datetime.datetime.now() - startTime;
    print(
        "{0}\t{1}\t{2}".format( ''.join(candidate.Genes),candidate.Fitness,str(timeDiff) )
    );

class GuessPasswordTests(unittest.TestCase):
    
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.";

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_for_i_am_b3);

    def test_onemax(self):
        target="1"*100;
        self.geneSet="01";
        self.guess_password(target);

    def test_Hello_World(self):
        target = "Hello World!";
        self.guess_password(target);

    def test_for_i_am_b3(self):
        target="qwffgeeoeivdfvhfdvpgwtrrbntyoib rb";
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

        self.assertEqual(''.join(best.Genes),target);
        print("  ");

if __name__ == '__main__':
    unittest.main();