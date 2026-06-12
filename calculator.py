import math
def print_divider():
      """Prints a consistent visual seperator."""
      print(f"\n{'-' * 50}\n")

print_divider()
print("Welcome to Our Calculator!\n"
      "\n"
      "1 - Add\n"
      "2 - Subtract\n"
      "3 - Multiply\n"
      "4 - Divide\n"
      "5 - power\n"
      "6 - square root\n"
      "\n"
      "0 - Exit\n"
      )

while True:
      operator = input("Choose an operator (0-6): ")
      print_divider()

      if operator in ['0', '1', '2', '3', '4', '5', '6']:
            break
      else:
            print("Invalid! Please enter a number between 1 to 4.\n")


if operator == '0':
      print("Exiting...")
      print_divider()
      exit()
elif operator == '1':
      print("select two number (a + b)")
      a = float(input("input value of a: "))
      b = float(input("input value of b: "))
      value = a + b
      print(f"your answer is {value:.2f}")
elif operator == '2':
      print("select two number (a + b)")
      a = float(input("input value of a: "))
      b = float(input("input value of b: "))
      value = a - b
      print(f"your answer is {value:.2f}")
elif operator == '3':
      print("select two number (a * b)")
      a = float(input("input value of a: "))
      b = float(input("input value of b: "))
      value = a * b
      print(f"your answer is {value:.2f}")
elif operator == '4':
      print("select two number (a / b)")
      a = float(input("input value of a: "))
      b = float(input("input value of b: "))
      value = a / b
      print(f"your answer is {value:.2f}")
elif operator == '5':
      print("select two number (a^b)")
      a = float(input("input value of a: "))
      b = float(input("input value of b: "))
      value = a ** b
      print(f"your answer is {value:.2f}")
elif operator == '6':
      print("select a number (√a)")
      a = float(input("input value of a: "))
      value = math.sqrt(a)
      print(f"your answer is {value:.2f}")