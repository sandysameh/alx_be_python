FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    print(f"{fahrenheit}°F is {(fahrenheit-32)* FAHRENHEIT_TO_CELSIUS_FACTOR}°C")

def convert_to_fahrenheit(celsius):
    print(f"{celsius}°C is {(celsius* CELSIUS_TO_FAHRENHEIT_FACTOR)+32}°F")


def main():
    while True: 
        temp = input("Enter the temperature to convert:")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F)").upper()
        unitCondition = unit in ('C','F')
        if temp.isdigit() and unitCondition: 
            temp=float(temp)

            if unit == 'C':
                convert_to_fahrenheit(temp)
            else: 
                convert_to_celsius(temp)
            break
        elif not temp.isdigit() and not unitCondition:
            print("Invalid temp or unit ")
        elif  not temp.isdigit():
            print("Invalid temperature. Please enter a numeric value.")
        else:
            print("Invalid unit")





if __name__ == "__main__":
    main()