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
      "\n"
      "0 - Exit\n"
      )

while True:
      operator = input("Choose an operator (0-4): ")
      print_divider()

      if operator in ['0', '1', '2', '3', '4']:
            break
      else:
            print("Invalid! Please enter a number between 1 to 4.\n")

if operator == '0':
      print("Exiting...")
      print_divider()
      exit()
elif operator == '1':
      pass
elif operator == '2':
      pass
elif operator == '3':
      pass
elif operator == '4':
      pass