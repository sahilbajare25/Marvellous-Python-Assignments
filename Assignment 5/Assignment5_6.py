#Celsius to Fahrenheit Converter

def main():
    print("Enter temperature in celsius :")
    temp = int(input())

    far = (temp*(9/5))+32

    print("Temperature in fahrenheit : ",far," F")

if __name__ == "__main__":
    main()