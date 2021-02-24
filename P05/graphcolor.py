import sys;
sys.path.append("..");
import Library.genetic as genetic;
import math,random,datetime,unittest,csv;

class Rule: 
    Node=None;
    Adjacent= None;

    def __init__(self,node,adjacent):
        if node < adjacent:
            node,adjacent=adjacent,node;
        self.Node=node;
        self.Adjacent=adjacent;

    def __eq__(self,other):
        return self.Node == other.Node and self.Adjacent==other.Adjacent;

    def __hash__(self):
        return hash(self.Node)*397 ^ hash(self.Adjacent);
    
    def __str__(self):
        return self.Node + " -> " + self.Adjacent;

    def IsValid(self,genes,nodeIndexLookup):
        index=nodeIndexLookup[self.Node];
        adjacentStateIndex = nodeIndexLookup[self.Adjacent];
        return genes[index] != genes[adjacentStateIndex];

def build_rules(items):
    rulesAdded={};
    for state,adjacent in items.items():
        for adjacentState in adjacent:
            if adjacentState=='':
                continue;
            rule=Rule(state,adjacentState);
            if rule in rulesAdded:
                rulesAdded[rule]+=1;
            else:
                rulesAdded[rule]=1;
    
    for k,v in rulesAdded.items():
        if v!=2:
            print("rule {0} is not bidirectional".format(k));
    return rulesAdded;

def load_data(localFileName):
    """ Expects: AA,BB;CC 
    """
    with open(localFileName,mode='r') as infile:
        reader=csv.reader(infile);
        lookup={};
        for row in reader:
            if row[1]:
                lookup.update({ row[0]: row[1].split(";") } );
            else:
                lookup.update({ row[0]: [] } );
    """
        Testing Data

    """
    for key in lookup:
            list=lookup[key];
            for state in list:
                if state not in lookup.keys():
                    print("Problem with key: {0}".format(state));
                    sys.exit("Error Here");
                list2=lookup[state];
                # Check For Reverse Existence 
                list2.index(key);

    return lookup;

def display(candidate,startTime):
    timeDiff=datetime.datetime.now() - startTime;
    print(
        "{0}\t{1}\t{2}".format(
            ''.join(map(str,candidate.Genes)),
            str(candidate.Fitness),
            str(timeDiff)
        )        
    );

def get_fitness(genes,rules,stateIndexLookUp):
    rulesThatPass= sum(
        1 for rule in rules 
        if rule.IsValid(genes,stateIndexLookUp)
    );

    return rulesThatPass;

class graphcolor(unittest.TestCase):
    def test(self):
        states=load_data("../FilesToUse/statesmap.csv");
        rules=build_rules(states);
        optimalValue=len(rules);
        stateIndexLookUp={
            key: index for index,key in enumerate(sorted(states))
        };
        colors=["Orange","Yellow","Green","Blue"];
        colorLookup={color[0]:color for color in colors};
        geneset=list(colorLookup.keys());

        startTime=datetime.datetime.now();
        
        def fnDisplay(candidate):
            display(candidate,startTime);
        
        def fnGetFitness(genes):
            return get_fitness(genes,rules,stateIndexLookUp);
        
        best=genetic.get_best(fnGetFitness,len(states),optimalValue,geneset,fnDisplay);

        self.assertTrue(not optimalValue > best.Fitness);
        
        for key,index in stateIndexLookUp.items():
            color_key=best.Genes[index];
            color=colorLookup[color_key];
            print("{0} is {1}".format(key,color));
        
if __name__ == '__main__':
    unittest.main();