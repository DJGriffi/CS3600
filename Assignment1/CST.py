#########################################################
##  CS 3600 (Winter 2023), Assignment #1, Question #1  ##
##   Script File Name: CST.py                          ##
##       Student Name: Drew Griffiths                  ##
##         Login Name: djamesg                         ##
##              MUN #: 201997184                       ##
#########################################################

import sys

def main():

    cst = CST(sys.argv[1])
    print("The item universe is : ", end='')
    for ele in cst.universe:
        print(ele, end=' ')
    print()
    print("The given subsets are : ")
    for x, y in cst.dict.items():
        print(str(x) + ": " + str(sorted(y)))
    sol = ""
    cst.DFS(1, sol)
    print("The optimal cost is : ", cst.optCost)
    print("The optimal solution subset covers: ")
    for ele in cst.optSol:
        print("{", end=' ')
        for val in ele:
            for c in val:
                if c == ' ': continue
                print(c, end=' ')
            print("}")



class CST:
    """
    Takes a set cover problem via a .txt file and recursively performs depth-first
    search to find the minimal set cover solution.
    """

    def __init__(self, fileName: str) -> None:
        """
        Constructor 

        Args:
            fileName (str): name of .txt file to be read in
        """

        self.n = None   
        self.universe = None
        self.optSol = []
        self.optCost = sys.maxsize
        self.dict = {}
        self.leftSide = sys.maxsize
        self.rightSide = sys.maxsize
        self.load(fileName)

        
    def load(self, filename: str) -> None:
        """
        Parses given text file and sets the instance variables n (number of sets given),
        universe (set universe), and dict (dictionary of given sub-sets).
        
        Args:
            filename (str): .txt file of a specific set cover problem
        """

        with open(filename, 'r') as file:

            nm = file.readline().strip().split() #makes array
            for i in range(len(nm)):
                nm[i] = int(nm[i])

            self.n = nm[1]
            self.universe = [str(i) for i in range(1, nm[0] + 1)]

            lineArr = [line.strip() for line in file]
            subSetArr = []
            for ele in lineArr:
                subSetArr.append(ele.split())
            for i in range(1, self.n + 1):
                subSetArr[i - 1].pop(0)
                for ele in subSetArr[i - 1]:
                    self.dict[i] = set(subSetArr[i - 1])


    def DFS(self, i: int, sol: str) -> int:
        """
        Performs recursive depth-first search algorithm until a leaf node is
        reached. Along the way, the algorithm will keep track of the lowest
        number of sub-sets found in a viable solution. If the current branch
        will not lead to an equal number, or lower number, of sub-sets in the 
        current solution than in the already found minimum set cover, the branch 
        will be pruned. DFS will also keep track of the best found solutions as 
        the tree is traversed. 

        Args:
            i (int): current depth
            sol (str): current set cover solution

        Returns:
            int: the number of sub-sets in the current set cover solution.
        """

        if (self.optCost != sys.maxsize and len(sol.split()) > self.optCost):
            return sys.maxsize

        if (i == (self.n + 1)):
            if (self.isViable(sol)):
                viableList = sol.split()
                if len(viableList) < self.optCost:
                    self.optCost = len(viableList)
                    self.optSol = [[sol]]
                elif len(viableList) == self.optCost:
                    self.optSol.append([sol])
                return(len(viableList))
            else:
                return sys.maxsize

        self.DFS(i + 1, sol)
        if i == self.n:
            sol += str(i)
        else:
            sol += str(i) + " "
        self.DFS(i + 1, sol)

        return
    
    def isViable(self, sol: str) -> bool:
        """
        Checks if the current solution (sol) is viable. Viable means that the
        union of all the sub-sets in the solution exactly matches the set cover
        problems universe.

        Args:
            sol (str): current set cover solution given as a string. 
            ex: '1 3 4' would mean the current solution is subsets 1, 3 and 4.

        Returns:
            bool: true if solution is viable, otherwise false
        """

        if (sol == ""):
            return False
        solList = sol.split()
        if (len(solList) == 1):
            if (len(self.dict[int(solList[0])]) != len(self.universe)):
                return False
            else:
                if(all(x in self.universe for x in self.dict[int(solList[0])])):
                    return True
                else:
                    return False
        else:
            solUnion = self.dict[int(solList[0])]
            for i in range(1, len(solList)):
                solUnion = solUnion.union(self.dict[int(solList[i])])
            if(all(x in solUnion for x in self.universe)):
                return True
            else:
                return False
                
    

if __name__ == "__main__":
    main()