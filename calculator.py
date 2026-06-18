import math

# comments to partner:
# make a definition where hyp > adj or opposite side

def print_divider():
      """Prints a consistent visual seperator."""
      print(f"\n{'-' * 50}\n")

def positive_valid_check(a, b, c, d, e, f, g):  #yo partner, i need a positive value checker here
      while True:
            while a <= 0:
                  print("Invalid length can't be (-)")
                  a = float(input("re-enter length: "))
            while b <= 0:
                  print("Invalid width can't be (-)")
                  b = float(input("re-enter width: "))
            while c <= 0:
                  print("Invalid diameter can't be (-)")
                  c = float(input("re-enter diameter: "))
            while d <= 0:
                  print("Invalid area can't be (-)")
                  d = float(input("re-enter area: "))
            while e <= 0:
                  print("Invalid volume can't be (-)")
                  e = float(input("re-enter volume: "))
            while f <= 0:
                  print("Invalid base can't be (-)")
                  f = float(input("re-enter base: "))
            while g <= 0:
                  print("Invalid height can't be (-)")
                  g = float(input("re-enter height: "))
            break



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
      while True:
            print("select your shape dimension\n"
                  "1. 2D\n"
                  "2. 3D")
            geo_type = input("type your choice: ")
            if geo_type in ['1', '2']:
                  break
            else:
                print(f"INVALID, {geo_type} is not in the option\n"
                      "please re-select a valid option")
                print("1. 2D\n"
                  "2. 3D")
                geo_type = input("type your choice: ")  

      if geo_type == "1":
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
                        length = float(input("Enter length = "))
                        width = float(input("Enter width = "))

                        area = width * length
                        print(f"area = {area}")
                  elif operation == '2':
                        print("how will you calculate?\n"
                              "  a. width and length"
                              "  b. area and one length")
                        start = input("enter selection: ").lower().replace(" ","")
                        while True:
                              if start in ["a", "b"]:
                                    break
                              else:
                                    print(f"{start} is INVALID!\n")
                                    start = input("Enter either a or b: ").lower().replace(" ","")
                        if start == "a":
                              length = float(input("Enter length = "))
                              width = float(input("Enter width = "))
                              perimeter = (length * 2) + (width * 2)
                              print(f"perimeter = {perimeter}")
                        elif start == "b":
                              length = float(input("Enter length = "))
                              area = float(input("Enter area = "))
                              width = area / length
                              perimeter = (2 * length) + (2 * width)
                              print(f"Perimeter = {perimeter}")

                  elif operation == '3':
                        print("how will you calculate?\n"
                              "  a. width and length"
                              "  b. area and one length"
                              "  c. perimeter and one length")
                        start = input("enter selection: ").lower().replace(" ","")
                        while True:
                              if start in ["a", "b", "c"]:
                                    break
                              else:
                                    print(f"{start} is INVALID!\n")
                                    start = input("Enter either a, b, or c: ").lower().replace(" ","")
                        if start == "a":
                              length = float(input("Enter length = "))
                              width = float(input("Enter width = "))
                              diagonal = math.sqrt(pow(length, 2) + pow(width, 2))
                              print(f"Diagonal length = {diagonal}")
                        elif start == "b":
                              area = float(input("Enter area = "))
                              length = float(input("Enter length"))
                              width = area / length
                              diagonal = math.sqrt(pow(length, 2) + pow(width, 2))
                              print(f"Diagonal length = {diagonal}")
                        elif start == "c":
                              perimeter = float(input("Enter perimeter = "))
                              length = float(input("Enter length = "))
                              width = (perimeter - (2 * length)) / 2
                              diagonal = math.sqrt(pow(length, 2) + pow(width, 2))
                              print(f"Diagonal length = {diagonal}")


            elif shape == '2':
                  right_angle = input("Is is right angle triangle? (Y/N): ").lower().replace(" ", "")
                  while True:
                        if right_angle in ["y", "n"]:
                              break
                        else:
                              input("INVALID!")
                              right_angle = input("Is is right angle triangle? Enter only (Y/N): ").lower().replace(" ", "")
                  if right_angle == "y":
                        print("[Geometry Calculator / Right - Triangle]\n"
                              "\n"
                              "1 - a side\n"
                              "2 - Perimeter\n"
                              "3 - Area\n"
                              "4 - angles\n"
                              )
                        while True:
                              operation = input("Choose an operation (1-5): ")
                              print_divider()

                              if operation in ['1', '2', '3', '4', '5',]:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")
                        if operation == '1':
                              print("how will you calculate?\n"
                              "  a. pythagoras theorem - 2 known side\n"
                              "  b. SOHCAHTOA formula - 1 angle (not the 90 degree) and 1 side\n")
                              start = input("enter selection: ").lower().replace(" ","")
                              while True:
                                    if start in ["a", "b"]:
                                          break
                                    else:
                                          print(f"{start} is INVALID!\n")
                                          start = input("Enter either a or b: ").lower().replace(" ","")
                              if start == "a":
                                    print("What side are you calculating?\n" 
                                          "  a. hypotenuse\n" 
                                          "  b. Opposite / adjacent\n")
                                    goal = input("Enter selection: ").lower().replace(" ","") 
                                    while True: #
                                          if goal in ['a', 'b']: 
                                                break 
                                          else: 
                                                print(f"{goal} is INVALID!\n") #
                                                goal = input("Enter either a or b: ").lower().replace(" ","") #
                                    if goal == "a":
                                          side = float(input("Enter length of side a = "))
                                          side2 = float(input("Enter length of side b = "))
                                          hyp = math.sqrt(pow(side, 2) + pow(side2, 2))
                                          print(f"Hypotenuse length = {hyp:.2f}")
                                    elif goal == "b":
                                          hyp = float(input("Enter length of longest side (hypotenuse) = "))
                                          side2 = float(input("Enter length of side b = "))
                                          side = math.sqrt(pow(hyp, 2) - pow(side2, 2))
                                          print(f"side length = {side:.2f}")
                              if start == "b":
                                    print("What side is involved?\n"
                                          "  a. Hypotenuse & Opposite\n" 
                                          "  b. Hypotenuse & adjacent\n"
                                          "  c. Opposite & adjacent") 
                                    goal = input("Enter selection: ").lower().replace(" ","") 
                                    while True: 
                                          if goal in ['a', 'b', 'c']: 
                                                print("state the known side: \n"
                                                "  a. Hypotenuse\n" 
                                                "  b. Opposite\n"
                                                "  c. adjacent\n")
                                                known_side = input("Enter selection: ")
                                                while True:
                                                      if (goal == "a" and known_side == "c") or (goal == "b" and known_side == "b") or (goal == "c" and known_side == "a"):
                                                            print(f"{known_side} is not invloved")
                                                            known_side = input("Re-enter and involved side: ")
                                                      elif known_side in ['a', 'b', 'c']:
                                                            break
                                                      else:
                                                            print(f"{known_side} is INVALID!\n") #
                                                known_side = input("Enter either a, b, or c: ").lower().replace(" ","")
                                                break
                                          else: 
                                                print(f"{goal} is INVALID!\n") #
                                                goal = input("Enter either a, b, or c: ").lower().replace(" ","") 
                                    if goal == "a" and known_side == "a":
                                          hyp = float(input("Enter length of hypotenuse = "))
                                          angle = float (input("Enter angle (in degrees) = "))
                                          opp = math.sin(math.radians(angle)) * hyp
                                          print(f"Opposite length = {opp:.2f}")
                                    elif goal == "a" and known_side == "b":
                                          opp = float(input("Enter length of opposite = "))
                                          angle = float (input("Enter angle (in degrees) = "))
                                          hyp = opp / math.sin(math.radians(angle))
                                          print(f"Hypotenuse length = {hyp:.2f}")
                                    elif goal == "b" and known_side == "a":
                                          hyp = float(input("Enter length of hypotenuse = "))
                                          angle = float (input("Enter angle (in degrees) = "))
                                          adj = math.cos(math.radians(angle)) * hyp
                                          print(f"Adjacent length = {adj:.2f}")
                                    elif goal == "b" and known_side == "c":
                                          adj = float(input("Enter length of adjacent = "))
                                          angle = float (input("Enter angle (in degrees) = "))
                                          hyp = adj / math.cos(math.radians(angle))
                                          print(f"Hypotenuse length = {hyp:.2f}")
                                    elif goal == "c" and known_side == "b":
                                          opp = float(input("Enter length of opposite = "))
                                          angle = float (input("Enter angle (in degrees) = "))
                                          adj = opp / math.tan(math.radians(angle))
                                          print(f"Adjacent length = {adj:.2f}")
                                    elif goal == "c" and known_side == "c":
                                          adj = float(input("Enter length of adjacent = "))
                                          angle = float (input("Enter angle (in degrees) = "))
                                          opp = math.tan(math.radians(angle)) * adj
                                          print(f"Opposite length = {opp:.2f}")

                  elif right_angle == "n":
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
                              print("how will you calculate?\n"
                              "  a. base and height\n"
                              "  b. trigonometry (2 sides, angle in between)\n"
                              "  c. heron's formula (3 sides)")
                              start = input("enter selection: ").lower().replace(" ","")
                              while True:
                                    if start in ["a", "b", "c"]:
                                          break
                                    else:
                                          print(f"{start} is INVALID!\n")
                                          start = input("Enter either a, b, or c: ").lower().replace(" ","")
                              if start == "a":
                                    base = float(input("Enter base = "))
                                    height = float(input("Enter height = "))
                                    area = 0.5 * base * height
                                    print(f"area = {area:.2f}")
                              elif start == "b":
                                    side = float(input("Enter length on a = "))
                                    side2 = float(input("Enter length of b = "))
                                    angle = float(input("Enter angle between a and b (in degrees) = "))
                                    area = 0.5 * side * side2 * math.sin(math.radians(angle))
                                    print(f"area = {area:.2f}")
                              elif start == "c":
                                    side = float(input("Enter length on a = "))
                                    side2 = float(input("Enter length of b = "))
                                    side3 = float(input("Enter length of c = "))
                                    s = (side + side2 + side3) / 2
                                    area = math.sqrt(s * (s - side) * (s - side2) * (s - side3))
                                    print(f"area = {area:.2f}")
                        elif operation == '2':
                              side = float(input("Enter length on a = "))
                              side2 = float(input("Enter length of b = "))
                              side3 = float(input("Enter length of c = "))
                              perimeter = side + side2 + side3
                              print(f"perimeter = {perimeter:.2f}")
                        elif operation == '3':
                              print("how will you calculate?\n"
                              "  a. 2 angles\n"
                              "  b. trigonometry")
                              start = input("enter selection: ").lower().replace(" ","")
                              while True:
                                    if start in ["a", "b"]:
                                          break
                                    else:
                                          print(f"{start} is INVALID!")
                                          start = input("Enter either a or b: ").lower().replace(" ","")
                              if start == "a":
                                    angle1 = float(input("Enter angle 1 (in degrees) = "))
                                    angle2 = float(input("Enter angle 2 (in degrees) = "))
                                    angle = 180 - (angle1 + angle2)
                                    print(f"Missing angle = {angle}")
                              elif start == "b":
                                    print("how will you calculate?\n"
                                    "  a. sin rule (2 sides, one angle)\n"
                                    "  b. cosine rule (3 sides)")
                                    rule = input("enter selection: ").lower().replace(" ","")
                                    while True:
                                          if rule in ["a", "b"]:
                                                break
                                          else:
                                                print(f"{start} is INVALID!")
                                                start = input("Enter either a or b: ").lower().replace(" ","")
                                    if rule == "a":
                                          side = float(input("Enter length of a = "))
                                          side2 = float(input("Enter length of b = "))
                                          angle1 = float(input("Enter angle A = "))
                                          angle = (math.sin(math.radians(angle1)) / side) * side2
                                          print(f"Angle B = {angle}")
                                    elif rule == "b":
                                          side = float(input("Enter length of a = "))
                                          side2 = float(input("Enter length of b = "))
                                          side3 = float(input("Enter length of c = "))
                                          angle = math.degrees(math.acos((pow(side2, 2) + pow(side3, 2) - pow(side, 2)) / (2 * side2 * side3)))
                                          print(f"angle A = {angle}")


            elif shape == '3':
                  print("[Geometry Calculator / Circle]\n"
                        "\n"
                        "1 - Area\n"
                        "2 - Circumference\n"
                        "3 - Diameter\n"
                        "4 - Area of a sector\n"
                        "5 - Arc of a sector\n"
                        "6 - Angle of a sector"
                        )
                  
                  while True:
                        operation = input("Choose an operation (1-3): ")
                        print_divider()

                        if operation in ['1', '2', '3', '4', '5', '6']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 3.\n")

                  if operation == '1':
                        print("how will you calculate?\n"
                              "  a. radius\n"
                              "  b. circumference")
                        start = input("enter selection: ").lower().replace(" ","")
                        while True:
                              if start in ["a", "b"]:
                                    break
                              else:
                                    print(f"{start} is INVALID!")
                                    start = input("Enter either a or b: ").lower().replace(" ","")
                        if start == "a":
                              radius = float(input("Enter radius = "))
                              area = math.pi * pow(radius, 2)
                              print(f"Area = {area:.2f}")
                        elif start == "b":
                              circumference = float(input("Enter circumference = "))
                              radius = circumference / (2 * math.pi)
                              area = math.pi * pow(radius, 2)
                              print(f"Area = {area:.2f}")
                  elif operation == '2':
                        print("how will you calculate?\n"
                              "  a. radius\n"
                              "  b. area")
                        start = input("enter selection: ").lower().replace(" ","")
                        while True:
                              if start in ["a", "b"]:
                                    break
                              else:
                                    print(f"{start} is INVALID!\n")
                                    start = input("Enter either a or b: ").lower().replace(" ","")
                        if start == "a":
                              radius = float(input("Enter radius = "))
                              circumference = 2 * math.pi * radius
                              print(f"Circumference = {circumference:.2f}")
                        elif start == "b":
                              area = float(input("Enter area = "))
                              radius = math.sqrt(area / (math.pi))
                              circumference = 2 * math.pi * radius
                              print(f"Circumference = {circumference:.2f}")
                  elif operation == '3':
                        print("how will you calculate?\n"
                              "  a. radius\n"
                              "  b. circumference\n"
                              "  c. area")
                        start = input("enter selection: ").lower().replace(" ","")
                        while True:
                              if start in ["a", "b"]:
                                    break
                              else:
                                    print(f"{start} is INVALID!\n")
                                    start = input("Enter either a or b: ").lower().replace(" ","")
                        if start == "a":
                              radius = float(input("Enter radius = "))
                              diameter = radius * 2
                              print(f"diameter = {diameter:.2f}")
                        elif start == "b":
                              circumference = float(input("Enter circumference = "))
                              radius = circumference / (2 * math.pi)
                              diameter = radius * 2
                              print(f"diameter = {diameter:.2f}")
                        elif start == "c":
                              area = float(input("Enter area = "))
                              radius = math.sqrt(area / (math.pi))
                              diameter = radius * 2
                              print(f"diameter = {diameter:.2f}")
                  elif operation == '4':
                        radius = float(input("Enter radius = "))
                        angle = float(input("Enter angle of sector (in degrees)= "))
                        area = (angle / 360) * math.pi * pow(radius, 2)
                        print(f"Area of sector = {area}")
                  elif operation == '5':
                        radius = float(input("Enter radius = "))
                        angle = float(input("Enter angle of sector (in degrees)= "))
                        arc = (angle / 360) * 2 * math.pi * pow(radius, 2)
                        print(f"Arc of sector = {arc}")
                  elif operation == '6':
                        print("how will you calculate?\n"
                              "  a. Radius & Arc of sector\n"
                              "  b. Radius & Area of sector")
                        start = input("Enter selection: ").lower().replace(" ", "")
                        while True:
                              if start in ["a", "b"]:
                                    break
                              else:
                                    print(f"{start} is INVALID!")
                                    start = input("Enter either a, b, or c: ").lower().replace(" ","")
                        if start == "a":
                              radius = float(input("Enter radius = "))
                              area = float(input("Enter area = "))
                              angle = (area * 360) / (math.pi * pow(radius, 2))
                              print(f"angle of sector = {angle} degrees")
                        elif start == "b":
                              radius = float(input("Enter radius = "))
                              arc = float(input("Enter arc = "))
                              angle = (arc * 360) / (2 * math.pi * radius)
                              print(f"angle of sector = {angle} degrees")