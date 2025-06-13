import sys

def count(FileName):

    fb = open(FileName,"r")

    cntCharacters = 0

    cntWords = 0

    cntSpace = 0

    temp = []

    for line in fb:
        temp.append(line.strip("\n").split(" "))

    cntLines = len(temp)

    fb.seek(0)

    for line in fb:
        a = line.count(" ")
        cntSpace = cntSpace + a

    print("Number of lines in file are : ",len(temp))

    for i in temp:
        for j in i:
            cntWords = cntWords + 1
            for k in j:
                cntCharacters = cntCharacters + 1

    cntCharacters = cntCharacters + cntSpace
        
    print("Number of words in file are : ",cntWords)
    print("Number of characters in the file are : ",cntCharacters)
            
    fb.close()

def main():

    count(sys.argv[1])

if __name__ == "__main__":
    main()