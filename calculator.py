import math


def print_divider():
      """Prints a consistent visual seperator."""
      print(f"\n{'-' * 50}\n")

print_divider()

print("WELCOME TO OUR CALCULATOR!\n"
      "\n"
      "1 - Standard Calculator\n"
      "2 - Geometry Calculator\n"
      "\n"
      "0 - Exit\n"
      )

while True:
      calculator = input("Choose a Calculator (0-2): ")
      print_divider()

      if calculator in ['0', '1', '2']:
            break
      else:
            print("Invalid! Please enter a number between 0 to 2.\n")

if calculator == '0':
      print("Exiting...")
      print_divider()
      exit()


# STANDARD CALCULATOR

elif calculator == "1":
      print("[Standard Calculator]\n"
            "\n"
            "1 - Add\n"
            "2 - Subtract\n"
            "3 - Multiply\n"
            "4 - Divide\n"
            "\n"
            "5 - Power\n"
            "6 - Square Root\n"
            )

      while True:
            operator = input("Choose an operator (1-6): ")
            print_divider()

            if operator in ['1', '2', '3', '4', '5', '6']:
                  break
            else:
                  print("Invalid! Please enter a number between 1 to 6.\n")

      if operator == '1':
            print("Input two numbers (a + b)\n")
            a = float(input("Input the value of a: "))
            b = float(input("Input the value of b: "))
            value = a + b
            print_divider()
            print(f"Your answer is {value:.2f}")
            print_divider()
      elif operator == '2':
            print("Input two numbers (a - b)\n")
            a = float(input("Input the value of a: "))
            b = float(input("Input the value of b: "))
            value = a - b
            print_divider()
            print(f"Your answer is {value:.2f}")
            print_divider()
      elif operator == '3':
            print("Input two numbers (a * b)\n")
            a = float(input("Input the value of a: "))
            b = float(input("Input the value of b: "))
            value = a * b
            print_divider()
            print(f"Your answer is {value:.2f}")
            print_divider()
      elif operator == '4':
            print("Input two numbers (a / b)\n")
            a = float(input("Input the value of a: "))
            b = float(input("Input the value of b: "))
            value = a / b
            print_divider()
            print(f"Your answer is {value:.2f}")
            print_divider()
      elif operator == '5':
            print("Input two numbers (a^b)\n")
            a = float(input("Input the value of a: "))
            b = float(input("Input the value of b: "))
            value = a ** b
            print_divider()
            print(f"Your answer is {value:.2f}")
            print_divider()
      elif operator == '6':
            print("Input a number (√a)\n")
            a = float(input("Input the value of a: "))
            value = math.sqrt(a)
            print_divider()
            print(f"Your answer is {value:.2f}")
            print_divider()


# GEOMETRY CALCULATOR

elif calculator == "2":
      print("[Geometry Calculator]\n"
            "\n"
            "1 - Rectangle\n"
            "2 - Triangle\n"
            "3 - Circle\n"
            )
      
      while True:
            shape = input("Choose a shape (1-3): ")
            print_divider()

            if shape in ['1', '2', '3']:
                  break
            else:
                  print("Invalid! Please enter a number between 1 to 3.\n")
      
      if shape == '1':
            print("[Geometry Calculator / Rectangle]\n"
                  "\n"
                  "1 - Area\n"
                  "2 - Perimeter\n"
                  "3 - Diagonal Length\n"
                  )
            
            while True:
                  operation = input("Choose an operation (1-3): ")
                  print_divider()

                  if operation in ['1', '2', '3']:
                        break
                  else:
                        print("Invalid! Please enter a number between 1 to 3.\n")

            if operation == '1':
                  pass
            elif operation == '2':
                  pass
            elif operation == '3':
                  pass

      elif shape == '2':
            print("[Geometry Calculator / Triangle]\n"
                  "\n"
                  "1 - Area\n"
                  "2 - Perimeter\n"
                  "3 - Angles\n"
                  )
            while True:
                  operation = input("Choose an operation (1-3): ")
                  print_divider()

                  if operation in ['1', '2', '3']:
                        break
                  else:
                        print("Invalid! Please enter a number between 1 to 3.\n")

            if operation == '1':
                  pass
            elif operation == '2':
                  pass
            elif operation == '3':
                  pass

      elif shape == '3':
            print("[Geometry Calculator / Circle]\n"
                  "\n"
                  "1 - Area\n"
                  "2 - Circumference\n"
                  "3 - Diameter\n"
                  )
            
            while True:
                  operation = input("Choose an operation (1-3): ")
                  print_divider()

                  if operation in ['1', '2', '3']:
                        break
                  else:
                        print("Invalid! Please enter a number between 1 to 3.\n")

            if operation == '1':
                  pass
            elif operation == '2':
                  pass
            elif operation == '3':
                  pass