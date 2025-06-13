import sys

def checkAndDisplay(FileName):

    fb = open(FileName,"r")

    temp = {}
    demo = []

    for line in fb:
        demo.append(line.strip("\n").split(" "))

    temp = dict(demo)

    for key,value in temp.items():
        marks = int(value)
        if marks > 75:
            print("Student ",key," has scored ",value," marks")

    fb.close()
        
def main():

    checkAndDisplay(sys.argv[1])

if __name__ == "__main__":
    main()