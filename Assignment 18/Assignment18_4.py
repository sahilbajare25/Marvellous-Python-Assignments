import sys

def compare(FileName1,FileName2):

    temp1 = []
    temp2 = []

    fb1 = open(FileName1,"r")
    fb2 = open(FileName2,"r")

    for line in fb1:
        temp1.append(line.strip("\n").split(" "))

    for line in fb2:
        temp2.append(line.strip("\n").split(" "))

    if(temp1 == temp2):
        print("Both files have same contents")
    else:
        print("Both files not have same contents")

def main():

    compare(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()