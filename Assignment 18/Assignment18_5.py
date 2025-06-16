import sys

def checkAndCompare(FileName,stringName):

    temp = []
    cnt = 0

    fb = open(FileName,"r")

    for line in fb:
        temp.append(line.strip("\n").split(" "))

    for i in temp:
        for j in i:
            if stringName == j:
                cnt = cnt + 1

    print(cnt)

def main():

    checkAndCompare(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()