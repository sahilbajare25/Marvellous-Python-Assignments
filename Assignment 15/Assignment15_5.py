import sys

def main():

    FileName = sys.argv[1]
    strName = sys.argv[2]

    fb = open(FileName,"r")

    counter = 0
    temp = []

    for line in fb:
        temp.append(line.strip("\n").split(" "))

    for i in temp:
        for j in i:
            if strName == j:
                counter = counter + 1
                
    print(counter)

    fb.close()
    
if __name__ == "__main__":
    main()