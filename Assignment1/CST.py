import sys
import os

def main():
    # print(len(sys.argv))
    # print(sys.argv)
    # cst = CST(sys.argv[0], int(sys.argv[1]))
    # print(cst.file, cst.num)
    # print(type(cst.file), type(cst.num))
    # print(cst.myFunc())
    # with open(sys.argv[1], 'r') as reader:
        # Read and print the entire file line by line
        # line = reader.readline().strip()
        # while line != '':  # The EOF char is an empty string
        #     # line.strip()
    #         print(line)
    #         line = reader.readline().strip()
    
    # file = open(sys.argv[1], 'r')
    # print(list(file))
    # file.close()

    # with open(sys.argv[1], 'r') as file:
    #     nm = file.readline().strip().split() #makes array
    #     lineArr = [line.strip() for line in file]
    # print(nm)
    # print(lineArr)
    # for i in range(len(nm)):
    #     nm[i] = int(nm[i])
    # universe = [str(i) for i in range(1, nm[0] + 1)]
    # print(universe)
    # print(nm)
    # print(type(nm[0]), type(nm[1]))

    # subSetArr = []
    # for ele in lineArr:
    #     subSetArr.append(ele.split())
    # print(subSetArr)
    # mydict ={}

    # for i in range(1, nm[1] + 1):
    #     subSetArr[i - 1].pop(0)
    #     for ele in subSetArr[i - 1]:
    #         mydict[i] = set(subSetArr[i - 1])
    # union = mydict[3].union(mydict[4], mydict[1])
    # print(type(union))
    # print(len(union))
    # print(os.getcwd())
    # cst = CST(sys.argv[1])
    cst = CST("D:\DrewSchool\CS3600\Assignment1\iSet2.txt")
    print(cst.n)
    print(cst.universe)
    print(cst.dict)
    sol = ""
    print(cst.costDFS(1, sol))


    



class CST:

    def __init__(self, fileName: str) -> None:
        self.n = None   
        self.universe = None
        self.optSol = []
        self.optCost = []
        self.dict = {}
        self.load(fileName)

    def load(self, filename) -> None:
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

    # def addEle(self, sol: str, i: int) -> list:
    #     sol.append(i)
    #     return sol

    def costDFS(self, i: int, sol: str) -> int:
        if (i == (self.n + 1)):
            if (self.isViable(sol)):
                return(len(sol))
            else:
                return float('inf')
        else:
            leftSide = self.costDFS(i + 1, sol)
            if i == self.n:
                sol += str(i)
            else:
                sol += str(i) + " "
            rightSide = self.costDFS(i + 1, sol)
            return min(leftSide, rightSide)

    def isViable(self, sol: str) -> bool:
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
                solUnion.union(self.dict[int(solList[i])])
            if(all(x in self.universe for x in solUnion)):
                return True
            else:
                return False
                
    

if __name__ == "__main__":
    main()