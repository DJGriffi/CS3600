def main():
    test = ""
    for i in range (5):
        if i == 4:
            test += str(i)
        else:
         test += str(i) + " "
    print(test)
    listTest = test.split()
    print(listTest)


if __name__ == "__main__":
    main()