import sys

def displayLines(FileName):

    fb = open(FileName,"r")

    temp = []

    for line in fb:
        temp.append(line.strip("\n").split(" "))

    for i in temp:
        cnt = 0
        for j in i:
            cnt = cnt + 1
        
        if cnt > 5:
            print(" ".join(i))

def main():

    displayLines(sys.argv[1])

if __name__ == "__main__":
    main()