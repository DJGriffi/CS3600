import sys

def main():

    cst = CST(sys.argv[1])
    print("The item universe is : ", cst.universe)
    print("The given subsets are : ", cst.dict)
    sol = ""
    cst.costDFS(1, sol)
    print("The optimal cost is : ", cst.optCost)
    print("The optimal solution subset covers: ", cst.optSol)


class CST:

    def __init__(self, fileName: str) -> None:
        """_summary_

        Args:
            fileName (str): _description_
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
        """_summary_

        Args:
            filename (str): _description_
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


    def costDFS(self, i: int, sol: str) -> int:
        """_summary_

        Args:
            i (int): _description_
            sol (str): _description_

        Returns:
            int: _description_
        """
        if (self.optCost != sys.maxsize and len(sol.split()) > self.optCost):
            return sys.maxsize

        if (i == (self.n + 1)):
            if (self.isViable(sol)):
                # print(sol)
                viableList = sol.split()
                if len(viableList) < self.optCost:
                    self.optCost = len(viableList)
                    self.optSol = [[sol]]
                elif len(viableList) == self.optCost:
                    self.optSol.append([sol])
                return(len(viableList))
            else:
                return sys.maxsize

        self.costDFS(i + 1, sol)
        if i == self.n:
            sol += str(i)
        else:
            sol += str(i) + " "
        self.costDFS(i + 1, sol)

        return
    
    def isViable(self, sol: str) -> bool:
        """_summary_

        Args:
            sol (str): _description_

        Returns:
            bool: _description_
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