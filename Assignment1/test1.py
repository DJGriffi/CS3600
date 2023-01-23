def main():
    test = ""
    for i in range (5):
        if i == 4:
            test += str(i)
        else:
         test += str(i) + " "
    print(test)
    testlist = [[test]]
    print(testlist)
    listTest = test.split()
    print(listTest)


if __name__ == "__main__":
    main()