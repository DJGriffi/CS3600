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
    cst = CST(sys.argv[1])
    # cst = CST("D:\DrewSchool\CS3600\Assignment1\iSet2.txt") #for windows
    # cst = CST("/Users/drewgriffiths/Desktop/CS3600/CS3600/Assignment1/iSet8.txt") #for mac
    # print(cst.n)
    print("The item universe is : ", cst.universe)
    print("The given subsets are : ", cst.dict)
    sol = ""
    cst.costDFS(1, sol)
    print("The optimal cost is : ", cst.optCost)
    print("The optimal solution subset covers: ", cst.optSol)


    



class CST:

    def __init__(self, fileName: str) -> None:
        self.n = None   
        self.universe = None
        self.optSol = []
        self.optCost = sys.maxsize
        self.dict = {}
        self.leftSide = sys.maxsize
        self.rightSide = sys.maxsize
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

        # if (self.isViable(sol)):
        #     viableList = sol.split()
        #     if len(viableList) < self.optCost:
        #         self.optCost = len(viableList)
        #         self.optSol = [[sol]]
        #     elif len(viableList) == self.optCost:
        #         self.optSol.append([sol])
        
        # else:
            # print("left side sol:  ", sol + " i: %d" % i)
        # newLeftSide = self.costDFS(i + 1, sol)
        self.costDFS(i + 1, sol)
        # if newLeftSide < self.leftSide:
        #     self.leftSide = newLeftSide
        if i == self.n:
            sol += str(i)
        else:
            sol += str(i) + " "
            # print("right side sol: ", sol + " i: %d" % i)
        self.costDFS(i + 1, sol)
        # newRightSide = self.costDFS(i + 1, sol)
        # if newRightSide < self.rightSide:
        #     self.rightSide = newRightSide
            # print("new left side = ", newLeftSide)
            # print("new right side = ", newRightSide)
            # print('MIN VALUE RETURNED %d' % min(self.leftSide, self.rightSide))

            # if newRightSide < newLeftSide and newRightSide <= self.optCost:
            #     if newRightSide < self.optCost:
            #         self.optCost = newRightSide
            #         if i == (self.n - 1):
            #             newSol = sol + str(i + 1)
            #         else:
            #             newSol = sol + str(i + 1) 
            #         self.optSol = [[newSol]]
            #     else:
            #         self.optSol.append([sol])
                
            # elif newLeftSide < newRightSide and newLeftSide <= self.optCost:
            #     if newLeftSide < self.optCost:
            #         self.optCost = newLeftSide
            #         self.optSol = [[sol]]
            #     else:
            #         self.optSol.append([sol])

            
        # minVal = min(self.leftSide, self. rightSide)

        # if minVal < self.optCost:
            # self.optSol = [[sol]]
            # self.optCost = minVal
        return 

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
                solUnion = solUnion.union(self.dict[int(solList[i])])
            if(all(x in solUnion for x in self.universe)):
                return True
            else:
                return False
                
    

if __name__ == "__main__":
    main()