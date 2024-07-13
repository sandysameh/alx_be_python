class ValueTooHighError(Exception):
   
   def __init__(self,value):
      self.value = value
   def __str__(self):
      return f"Sorry, the value {self.value} is too high"


def numbersFunction():
      number =int(input("enter a number "))
      if (number>100):
         raise ValueTooHighError(number)
      else: 
         print("el7 number 3adi gedan")

try : 
    numbersFunction()
except ValueTooHighError as e: 
   print(e)

def divide():
    num1 = float(input("enter a num"))
    num2 = float(input("enter another num"))

    try: 
       result = num1 / num2
    except ZeroDivisionError:
        print("YOu can't divide a number by zero")


def open_file():
   try:
      filename = input("enter file name ")
      f =open(filename)
   except FileNotFoundError:
      print("sorry this file doesn't exist")

    
   
