import sys

def display(Filename):
    
    fb = open(Filename,"r")

    res = fb.read()

    print(res)

    fb.close()

def main():

    display(sys.argv[1])

if __name__ == "__main__":
    main()