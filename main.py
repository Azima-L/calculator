import math
import calculators as calc


def print_divider():
      """Prints a consistent visual seperator."""
      print(f"\n{'-' * 100}\n")

def answer_printer_repititor():
      pass

def std_one_input_flow(page_name, context, calculation):
      """Control repetition and consistency for one user input in the standard calculator."""
      print(f"[Standard Calculator / {page_name}]\n"
            "\n"
            f"Input a number ({context})\n"
            )
      num = float(input("Input the value of a: "))

      print_divider()
      print(f"Your answer is {calculation(num):.2f}")
      print_divider()
      
def std_two_inputs_flow(page_name, context, calculation):
      """Control repetition and consistency for two user inputs in the standard calculator."""
      print(f"[Standard Calculator / {page_name}]\n"
            "\n"
            f"Input two numbers ({context})\n"
            )
      num1 = float(input("Input the value of a: "))
      num2 = float(input("Input the value of b: "))

      print_divider()
      print(f"Your answer is {calculation(num1, num2):.2f}")
      print_divider()
      
def geo_one_input_flow(page_name, label1, calculation, arg1, operation):
      """Control repetition and consistency for two user inputs in the geometry calculator."""
      print(f"[Standard Calculator / 2D / {page_name}]\n")
      num = float(input(f"Input the {label1}: "))
      arguments = {arg1: num}
      get_shape = calculation(**arguments)
      
      if operation == 'area':
            get_operation = get_shape.area()
      elif operation == 'area2':
            get_operation = get_shape.area2()
      elif operation == 'circumference':
            get_operation = get_shape.circumference()
      elif operation == 'circumference2':
            get_operation = get_shape.circumference2()
      elif operation == 'diameter':
            get_operation = get_shape.diameter()
      elif operation == 'diameter2':
            get_operation = get_shape.diameter2()
      elif operation == 'diameter3':
            get_operation = get_shape.diameter3()
      
      print_divider()
      print(f"Your answer is {get_operation}")
      print_divider()

def geo_two_inputs_flow(page_name, label1, label2, calculation, arg1, arg2, operation):
      """Control repetition and consistency for two user inputs in the geometry calculator."""
      print(f"[Standard Calculator / 2D / {page_name}]\n")
      num1 = float(input(f"Input the {label1}: "))
      num2 = float(input(f"Input the {label2}: "))
      arguments = {arg1: num1, arg2: num2}
      get_shape = calculation(**arguments)
      
      if operation == 'area':
            get_operation = get_shape.area()
      elif operation == 'perimeter':
            get_operation = get_shape.perimeter()
      elif operation == 'perimeter2':
            get_operation = get_shape.perimeter2()
      elif operation == 'diagonal_length':
            get_operation = get_shape.diagonal_length()
      elif operation == 'diagonal_length2':
            get_operation = get_shape.diagonal_length2()
      elif operation == 'diagonal_length3':
            get_operation = get_shape.diagonal_length3()
      elif operation == 'side_pyt':
            get_operation = get_shape.side_pyt()
      elif operation == 'side_pyt2':
            get_operation = get_shape.side_pyt2()
      elif operation == 'side_sct_opp':
            get_operation = get_shape.side_sct_opp()
      elif operation == 'side_sct_opp2':
            get_operation = get_shape.side_sct_opp2()
      elif operation == 'side_sct_hyp':
            get_operation = get_shape.side_sct_hyp()
      elif operation == 'side_sct_hyp2':
            get_operation = get_shape.side_sct_hyp2()
      elif operation == 'side_sct_adj':
            get_operation = get_shape.side_sct_adj()
      elif operation == 'side_sct_adj2':
            get_operation = get_shape.side_sct_adj2()
      elif operation == 'angle':
            get_operation = get_shape.angle()
      elif operation == 'area_of_sector':
            get_operation = get_shape.area_of_sector()
      elif operation == 'arc_of_sector':
            get_operation = get_shape.arc_of_sector()
      elif operation == 'angle_of_sector':
            get_operation = get_shape.angle_of_sector()
      elif operation == 'angle_of_sector2':
            get_operation = get_shape.angle_of_sector2()
      
      print_divider()
      print(f"Your answer is {get_operation}")
      print_divider()

def geo_three_inputs_flow(page_name, label1, label2, label3, calculation, arg1, arg2, arg3, operation):
      """Control repetition and consistency for three user inputs in the geometry calculator."""
      print(f"[Standard Calculator / 2D / {page_name}]\n")
      num1 = float(input(f"Input the {label1}: "))
      num2 = float(input(f"Input the {label2}: "))
      num3 = float(input(f"Input the {label3}: "))
      arguments = {arg1: num1, arg2: num2, arg3: num3}
      get_shape = calculation(**arguments)
      
      if operation == 'area':
            get_operation = get_shape.area()
      elif operation == 'area2':
            get_operation = get_shape.area2()
      elif operation == 'area3':
            get_operation = get_shape.area3()
      elif operation == 'perimeter':
            get_operation = get_shape.perimeter()
      elif operation == 'angle2':
            get_operation = get_shape.angle2()
      elif operation == 'angle3':
            get_operation = get_shape.angle3()
      
      print_divider()
      print(f"Your answer is {get_operation}")
      print_divider()


# STARTING POINT

print_divider()

print("WELCOME TO OUR CALCULATOR!\n"
      "\n"
      "1 - Standard Calculator\n"
      "2 - Geometry Calculator\n"
      "\n"
      "0 - Exit\n"
      )

while True:
      calculator = input("Choose a calculator (0-2): ")
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

elif calculator == '1':
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
            std_two_inputs_flow("Add", "a + b", calc.add)
      elif operator == '2':
            std_two_inputs_flow("Subtract", "a - b", calc.sub)
      elif operator == '3':
            std_two_inputs_flow("Multiply", "a * b", calc.mul)
      elif operator == '4':
            std_two_inputs_flow("Divide", "a / b", calc.div)
      elif operator == '5':
            std_two_inputs_flow("Power", "a + b", calc.exp)
      elif operator == '6':
            std_one_input_flow("Square Root", "√a", calc.sqrt)


# GEOMETRY CALCULATOR

elif calculator == '2':
      print("[Geometry Calculator]\n"
            "\n"
            "1 - 2D\n"
            "2 - 3D\n"
            )
      while True:
            geo_dimension = input("Choose a shape dimension (1-2): ")
            print_divider()

            if geo_dimension in ['1', '2']:
                  break
            else:
                  print("Invalid! Please enter a number between 1 to 2.\n")

      if geo_dimension == '1':
            print("[Geometry Calculator / 2D]\n"
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
            

            # GEO 2D - Rectangle

            if shape == '1':
                  print("[Geometry Calculator / 2D / Rectangle]\n"
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
                        geo_two_inputs_flow("Rectangle / Area", "length", "width", calc.Rectangle, "num1", "num2", "area")

                  elif operation == '2':
                        print("[Geometry Calculator / 2D / Rectangle / Perimeter]\n"
                              "\n"
                              "How do you want to calculate the perimeter?\n"
                              "\n"
                              "1 - Length and Width\n"
                              "2 - Length and Area\n"
                              )
                        
                        while True:
                              option = input("Choose an option (1-2): ")
                              print_divider()

                              if option in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")

                        if option == '1':
                              geo_two_inputs_flow("Rectangle / Perimeter", "length", "width", calc.Rectangle, "num1", "num2", "perimeter")
                        elif option == '2':
                              geo_two_inputs_flow("Rectangle / Perimeter", "length", "area", calc.Rectangle, "num1", "num2","perimeter2")
                              
                  elif operation == '3':
                        print("[Geometry Calculator / 2D / Rectangle / Perimeter]\n"
                              "\n"
                              "How do you want to calculate the diagonal length?\n"
                              "\n"
                              "1 - Length and Width\n"
                              "2 - Length and Area\n"
                              "3 - Length and Perimeter\n"
                              )

                        while True:
                              option = input("Choose an option (1-3): ")
                              print_divider()

                              if option in ['1', '2', '3']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")

                        if option == '1':
                              geo_two_inputs_flow("Rectangle / Diagonal Length", "length", "width", calc.Rectangle, "num1", "num2", "diagonal_length")
                        elif option == '2':
                              geo_two_inputs_flow("Rectangle / Diagonal Length", "length", "area", calc.Rectangle, "num1", "num2", "diagonal_length2")
                        elif option == '3':
                              geo_two_inputs_flow("Rectangle / Diagonal Length", "length", "perimeter", calc.Rectangle, "num1", "num2", "diagonal_length3")


            # GEO 2D - Triangle

            elif shape == '2':
                  print("[Geometry Calculator / 2D / Triangle]\n"
                        "\n"
                        "1 - Right-angle Triangle\n"
                        "2 - General Triangle\n"
                        )
                  
                  while True:
                        triangle = input("Choose a triangle (1-2): ")
                        print_divider()

                        if triangle in ['1', '2']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 2.\n")

                  if triangle == '1':
                        print("[Geometry Calculator / 2D / Triangle / Right-angle]\n"
                              "\n"
                              "1 - Area\n"
                              "2 - Perimeter\n"
                              "3 - Side\n"
                              "4 - Angle\n"
                              )
                        
                        while True:
                              operation = input("Choose an operation (1-4): ")
                              print_divider()

                              if operation in ['1', '2', '3', '4']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 4.\n")
                                    
                        
                        # Dude, u forgot to do the Area for triangle
                        if operation == '1':
                              pass

                        # ...and Perimeter
                        elif operation == '2':
                              pass

                        elif operation == '3':
                              print("[Geometry Calculator / 2D / Triangle / Right-angle / Side]\n"
                                    "\n"
                                    "1 - Pythagoras Theorem (2 known sides)\n"
                                    "2 - SOHCAHTOA Formula (1 side, 1 angle)\n"
                                    )

                              while True:
                                    method = input("Choose a method (1-2): ")
                                    print_divider()

                                    if method in ['1', '2']:
                                          break
                                    else:
                                          print("Invalid! Please enter a number between 1 to 4.\n")

                              if method == '1':
                                    print("[Geometry Calculator / 2D / Triangle / Right-angle / Side / Pythagoras Theorem]\n"
                                          "\n"
                                          "Which side are you calculating?\n" 
                                          "\n"
                                          "1 - Hypotenuse\n" 
                                          "2 - Opposite or Adjacent\n"
                                          )

                                    while True:
                                          pythagoras_choice = input("Choose a side (1-2): ")
                                          print_divider()

                                          if pythagoras_choice in ['1', '2']:
                                                break
                                          else:
                                                print("Invalid! Please enter a number between 1 to 2.\n")

                                    if pythagoras_choice == '1':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / Pythagoras Theorem / Hypotenuse", "length of side a", "length of side b", calc.Triangle, "num1", "num2", "side_pyt")

                                    elif pythagoras_choice == '2':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / Pythagoras Theorem / Opp or Adj", "length of hypotenuse", "length of side b", calc.Triangle, "num1", "num2", "side_pyt2")

                              if method == '2':
                                    print("[Geometry Calculator / 2D / Triangle / Right-angle / Side / SOHCAHTOA Formula]\n"
                                          "\n"
                                          "Which sides are involved (your known and unknown sides)?\n"
                                          "\n"
                                          "1 - Hypotenuse & Opposite\n" 
                                          "2 - Hypotenuse & Adjacent\n"
                                          "3 - Opposite & Adjacent\n"
                                          ) 

                                    while True:
                                          inv_sides = input("Choose involved sides (1-3): ")
                                          print_divider()

                                          if inv_sides in ['1', '2', '3']:
                                                break
                                          else:
                                                print("Invalid! Please enter a number between 1 to 3.\n")
                                                
                                                
                                    print("[Geometry Calculator / 2D / Triangle / Right-angle / Side / SOHCAHTOA Formula]\n"
                                          "\n"
                                          "State the known side\n"
                                          "\n"
                                          "1 - Hypotenuse\n" 
                                          "2 - Opposite\n"
                                          "3 - Adjacent\n"
                                          )

                                    while True:
                                          known_side = input("Choose a known side (1-3): ")
                                          print_divider()

                                          if (inv_sides == '1' and known_side == '3') or (inv_sides == '2' and known_side == '2') or (inv_sides == '3' and known_side == '1'):
                                                if known_side == '1':
                                                      known_side_name = 'hypotenuse'
                                                elif known_side == '2':
                                                      known_side_name = 'opposite'
                                                elif known_side == '3':
                                                      known_side_name = 'adjacent'
                                                print(f"Invalid! The {known_side_name} is not involved\n")
                                          elif known_side in ['1', '2', '3']:
                                                break
                                          else:
                                                print(f"Invalid! {known_side} is not in the option\n")

                                    if inv_sides == '1' and known_side == '1':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of hypotenuse", "angle", calc.Triangle, "num1", "num2", "side_sct_opp")
                                          # hyp = float(input("Enter length of hypotenuse: "))
                                          # angle = float (input("Enter angle (in degrees): "))
                                          # opp = math.sin(math.radians(angle)) * hyp
                                          # print(f"Opposite length = {opp:.2f}")
                                    elif inv_sides == '1' and known_side == '2':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of opposite", "angle", calc.Triangle, "num1", "num2", "side_sct_hyp")
                                          # opp = float(input("Enter length of opposite: "))
                                          # angle = float (input("Enter angle (in degrees): "))
                                          # hyp = opp / math.sin(math.radians(angle))
                                          # print(f"Hypotenuse length = {hyp:.2f}")
                                    elif inv_sides == '2' and known_side == '1':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of hypotenuse", "angle", calc.Triangle, "num1", "num2", "side_sct_adj")
                                          # hyp = float(input("Enter length of hypotenuse: "))
                                          # angle = float (input("Enter angle (in degrees): "))
                                          # adj = math.cos(math.radians(angle)) * hyp
                                          # print(f"Adjacent length = {adj:.2f}")
                                    elif inv_sides == '2' and known_side == '3':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of adjacent", "angle", calc.Triangle, "num1", "num2", "side_sct_hyp2")
                                          # adj = float(input("Enter length of adjacent: "))
                                          # angle = float (input("Enter angle (in degrees): "))
                                          # hyp = adj / math.cos(math.radians(angle))
                                          # print(f"Hypotenuse length = {hyp:.2f}")
                                    elif inv_sides == '3' and known_side == '2':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of opposite", "angle", calc.Triangle, "num1", "num2", "side_sct_adj2")
                                          # opp = float(input("Enter length of opposite: "))
                                          # angle = float (input("Enter angle (in degrees): "))
                                          # adj = opp / math.tan(math.radians(angle))
                                          # print(f"Adjacent length = {adj:.2f}")
                                    elif inv_sides == '3' and known_side == '3':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of adjacent", "angle", calc.Triangle, "num1", "num2", "side_sct_opp2")
                                          # adj = float(input("Enter length of adjacent: "))
                                          # angle = float (input("Enter angle (in degrees): "))
                                          # opp = math.tan(math.radians(angle)) * adj
                                          # print(f"Opposite length = {opp:.2f}")

                        # ...and Angle
                        elif operation == '4':
                              pass

                  elif triangle == '2':
                        print("[Geometry Calculator / 2D / Triangle / General]\n"
                              "\n"
                              "1 - Area\n"
                              "2 - Perimeter\n"
                              "3 - Angle\n"
                              )
                        
                        while True:
                              operation = input("Choose an operation (1-3): ")
                              print_divider()

                              if operation in ['1', '2', '3']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")

                        if operation == '1':
                              print("[Geometry Calculator / 2D / Triangle / General / Area]\n"
                                    "\n"
                                    "State a calculation method\n"
                                    "\n"
                                    "1 - Base and Height\n"
                                    "2 - Trigonometry (2 sides, 1 angle in between)\n"
                                    "3 - Heron's Formula (3 sides)\n"
                                    "\n"
                                    )
                              
                              while True:
                                    calc_method = input("Choose calculation method (1-3): ")
                                    print_divider()

                                    if calc_method in ['1', '2', '3']:
                                          break
                                    else:
                                          print("Invalid! Please enter a number between 1 to 3.\n")

                              if calc_method == '1':
                                    geo_two_inputs_flow("Triangle / General / Area / Base & Height", "base", "height", calc.Triangle, "num1", "num2", "area")
                                    # base = float(input("Enter base = "))
                                    # height = float(input("Enter height = "))
                                    # area = 0.5 * base * height
                                    # print(f"area = {area:.2f}")
                              elif calc_method == '2':
                                    geo_three_inputs_flow("Triangle / General / Area / Trigonometry", "length of a", "length of b", "angle", calc.Triangle, "num1", "num2", "num3", "area2")
                                    # side = float(input("Enter length on a = "))
                                    # side2 = float(input("Enter length of b = "))
                                    # angle = float(input("Enter angle between a and b (in degrees) = "))
                                    # area = 0.5 * side * side2 * math.sin(math.radians(angle))
                                    # print(f"area = {area:.2f}")
                              elif calc_method == '3':
                                    geo_three_inputs_flow("Triangle / General / Area / Heron's Formula", "length of a", "length of b", "length of c", calc.Triangle, "num1", "num2", "num3", "area3")
                                    # side = float(input("Enter length on a = "))
                                    # side2 = float(input("Enter length of b = "))
                                    # side3 = float(input("Enter length of c = "))
                                    # s = (side + side2 + side3) / 2
                                    # area = math.sqrt(s * (s - side) * (s - side2) * (s - side3))
                                    # print(f"area = {area:.2f}")

                        elif operation == '2':
                              geo_three_inputs_flow("Triangle / General / Perimeter", "length of a", "length of b", "length of c", calc.Triangle, "num1", "num2", "num3", "perimeter")
                              # side = float(input("Enter length on a = "))
                              # side2 = float(input("Enter length of b = "))
                              # side3 = float(input("Enter length of c = "))
                              # perimeter = side + side2 + side3
                              # print(f"perimeter = {perimeter:.2f}")

                        elif operation == '3':
                              print("[Geometry Calculator / 2D / Triangle / General / Area]\n"
                                    "\n"
                                    "State a calculation method\n"
                                    "\n"
                                    "1 - 2 Angles\n"
                                    "2 - Trigonometry (2 sides, 1 angle in between)\n"
                                    )
                              
                              while True:
                                    calc_method = input("Choose calculation method (1-2): ")
                                    print_divider()

                                    if calc_method in ['1', '2']:
                                          break
                                    else:
                                          print("Invalid! Please enter a number between 1 to 2.\n")

                              if calc_method == '1':
                                    geo_two_inputs_flow("Triangle / General / Angle", "angle a", "angle b", calc.Triangle, "num1", "num2", "angle")
                                    # angle1 = float(input("Enter angle 1 (in degrees) = "))
                                    # angle2 = float(input("Enter angle 2 (in degrees) = "))
                                    # angle = 180 - (angle1 + angle2)
                                    # print(f"Missing angle = {angle}")
                              elif calc_method == '2':
                                    print("[Geometry Calculator / 2D / Triangle / General / Angle]\n"
                                          "\n"
                                          "State a calculation rule\n"
                                          "\n"
                                          "1 - Sin Rule (2 sides, one angle)\n"
                                          "2 - Cosine Rule (3 sides)\n"
                                          )
                                    
                                    while True:
                                          calc_rule = input("Choose calculation rule (1-2): ")
                                          print_divider()

                                          if calc_method in ['1', '2']:
                                                break
                                          else:
                                                print("Invalid! Please enter a number between 1 to 2.\n")
                                    if calc_rule == "a":
                                          geo_three_inputs_flow("Triangle / General / Angle", "length of a", "length of b", "angle a", calc.Triangle, "num1", "num2", "num3", "angle2")
                                          # side = float(input("Enter length of a = "))
                                          # side2 = float(input("Enter length of b = "))
                                          # angle1 = float(input("Enter angle A = "))
                                          # angle = (math.sin(math.radians(angle1)) / side) * side2
                                          # print(f"Angle B = {angle}")
                                    elif calc_rule == "b":
                                          geo_three_inputs_flow("Triangle / General / Angle", "length of a", "length of b", "length of c", calc.Triangle, "num1", "num2", "num3", "angle3")
                                          # side = float(input("Enter length of a = "))
                                          # side2 = float(input("Enter length of b = "))
                                          # side3 = float(input("Enter length of c = "))
                                          # angle = math.degrees(math.acos((pow(side2, 2) + pow(side3, 2) - pow(side, 2)) / (2 * side2 * side3)))
                                          # print(f"angle A = {angle}")


            # GEO 2D - Circle

            elif shape == '3':
                  print("[Geometry Calculator / 2D / Circle]\n"
                        "\n"
                        "1 - Area\n"
                        "2 - Circumference\n"
                        "3 - Diameter\n"
                        "4 - Area of a sector\n"
                        "5 - Arc of a sector\n"
                        "6 - Angle of a sector\n"
                        )
                  
                  while True:
                        operation = input("Choose an operation (1-6): ")
                        print_divider()

                        if operation in ['1', '2', '3', '4', '5', '6']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 6.\n")

                  if operation == '1':
                        print("[Geometry Calculator / 2D / Circle / Area]\n"
                              "\n"
                              "State a calculation method\n"
                              "\n"
                              "1 - Radius\n"
                              "2 - Circumference\n"
                              )
                        
                        while True:
                              calc_method = input("Choose calculation method (1-2): ")
                              print_divider()

                              if calc_method in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")

                        if calc_method == '1':
                              geo_one_input_flow("Circle / Area", "radius", calc.Circle, "num1", "area")
                              # radius = float(input("Enter radius = "))
                              # area = math.pi * pow(radius, 2)
                              # print(f"Area = {area:.2f}")
                        elif calc_method == '2':
                              geo_one_input_flow("Circle / Area", "circumference", calc.Circle, "num1", "area2")
                              # circumference = float(input("Enter circumference = "))
                              # radius = circumference / (2 * math.pi)
                              # area = math.pi * pow(radius, 2)
                              # print(f"Area = {area:.2f}")

                  elif operation == '2':
                        print("[Geometry Calculator / 2D / Circle / Circumference]\n"
                              "\n"
                              "State a calculation method\n"
                              "\n"
                              "1 - Radius\n"
                              "2 - Area\n"
                              )
                        
                        while True:
                              calc_method = input("Choose calculation method (1-2): ")
                              print_divider()

                              if calc_method in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")

                        if calc_method == '1':
                              geo_one_input_flow("Geometry Calculator / 2D / Circle / Circumference", "radius", calc.Circle, "num1", "circumference")
                              # radius = float(input("Enter radius = "))
                              # circumference = 2 * math.pi * radius
                              # print(f"Circumference = {circumference:.2f}")
                        elif calc_method == '2':
                              geo_one_input_flow("Geometry Calculator / 2D / Circle / Circumference", "area", calc.Circle, "num1", "circumference2")
                              # area = float(input("Enter area = "))
                              # radius = math.sqrt(area / (math.pi))
                              # circumference = 2 * math.pi * radius
                              # print(f"Circumference = {circumference:.2f}")
                  elif operation == '3':
                        print("[Geometry Calculator / 2D / Circle / Diameter]\n"
                              "\n"
                              "State a calculation method\n"
                              "\n"
                              "1 - Radius\n"
                              "2 - Circumference\n"
                              "3 - Area\n"
                              )
                        
                        while True:
                              calc_method = input("Choose calculation method (1-3): ")
                              print_divider()

                              if calc_method in ['1', '2', '3']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")

                        if calc_method == '1':
                              geo_one_input_flow("Geometry Calculator / 2D / Circle / Diameter", "radius", calc.Circle, "num1", "diameter")
                              # radius = float(input("Enter radius = "))
                              # diameter = radius * 2
                              # print(f"diameter = {diameter:.2f}")
                        elif calc_method == '2':
                              geo_one_input_flow("Geometry Calculator / 2D / Circle / Diameter", "circumference", calc.Circle, "num1", "diameter2")
                              # circumference = float(input("Enter circumference = "))
                              # radius = circumference / (2 * math.pi)
                              # diameter = radius * 2
                              # print(f"diameter = {diameter:.2f}")
                        elif calc_method == '3':
                              geo_one_input_flow("Geometry Calculator / 2D / Circle / Diameter", "area", calc.Circle, "num1", "diameter3")
                              # area = float(input("Enter area = "))
                              # radius = math.sqrt(area / (math.pi))
                              # diameter = radius * 2
                              # print(f"diameter = {diameter:.2f}")

                  elif operation == '4':
                        geo_two_inputs_flow("Circle / Area of a Sector", "radius", "angle of sector", calc.Circle, "num1", "num2", "area_of_sector")
                        # radius = float(input("Enter radius = "))
                        # angle = float(input("Enter angle of sector (in degrees)= "))
                        # area = (angle / 360) * math.pi * pow(radius, 2)
                        # print(f"Area of sector = {area}")

                  elif operation == '5':
                        geo_two_inputs_flow("Circle / Arc of a Sector", "radius", "angle of sector", calc.Circle, "num1", "num2", "arc_of_sector")
                        # radius = float(input("Enter radius = "))
                        # angle = float(input("Enter angle of sector (in degrees)= "))
                        # arc = (angle / 360) * 2 * math.pi * pow(radius, 2)
                        # print(f"Arc of sector = {arc}")

                  elif operation == '6':
                        print("[Geometry Calculator / 2D / Circle / Angle of a Sector]\n"
                              "\n"
                              "State a calculation method\n"
                              "\n"
                              "1 - Radius & Area of sector\n"
                              "2 - Radius & Arc of sector\n"
                              )
                        
                        while True:
                              calc_method = input("Choose calculation method (1-2): ")
                              print_divider()

                              if calc_method in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")

                        if calc_method == '1':
                              geo_two_inputs_flow("Circle / Angle of a Sector", "radius", "area", calc.Circle, "num1", "num2", "angle_of_sector")
                              # radius = float(input("Enter radius = "))
                              # area = float(input("Enter area = "))
                              # angle = (area * 360) / (math.pi * pow(radius, 2))
                              # print(f"angle of sector = {angle} degrees")
                        elif calc_method == '2':
                              geo_two_inputs_flow("Circle / Angle of a Sector", "radius", "arc", calc.Circle, "num1", "num2", "angle_of_sector2")
                              # radius = float(input("Enter radius = "))
                              # arc = float(input("Enter arc = "))
                              # angle = (arc * 360) / (2 * math.pi * radius)
                              # print(f"angle of sector = {angle} degrees")
      
      elif geo_dimension == '2':
            print("[Geometry Calculator / 3D]\n"
                  "\n"
                  "1 - Cuboid\n"
                  "2 - Cone\n"
                  "3 - Pyramid\n"
                  "4 - Sphere\n"
                  "5 - Cylinder\n"
                  )
            
            while True:
                  shape = input("Choose a shape (1-5): ")
                  print_divider()

                  if shape in ['1', '2', '3', '4', '5']:
                        break
                  else:
                        print("Invalid! Please enter a number between 1 to 5.\n")


            # GEO 3D - Cuboid

            if shape == '1':
                  print("[Geometry Calculator / 3D / Cuboid]\n"
                        "\n"
                        "1 - Volume\n"
                        "2 - Total Surface Area (TSA)\n"
                        "3 - Lateral Surface Area (LSA)\n"
                        "4 - Space Diagonal\n"
                        )
                  
                  while True:
                        operation = input("Choose an operation (1-4): ")
                        print_divider()

                        if operation in ['1', '2', '3', '4']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 4.\n")

                  if operation == '1':
                        pass
                  elif operation == '2':
                        pass
                  elif operation == '3':
                        pass
                  elif operation == '4':
                        pass


            # GEO 3D - Cone
            
            if shape == '2':
                  print("[Geometry Calculator / 3D / Cone]\n"
                        "\n"
                        "1 - Volume\n"
                        "2 - Total Surface Area (TSA)\n"
                        "3 - Curved Surface Area (CSA)\n"
                        "4 - Slant Height\n"
                        )
                  
                  while True:
                        operation = input("Choose an operation (1-4): ")
                        print_divider()

                        if operation in ['1', '2', '3', '4']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 4.\n")

                  if operation == '1':
                        pass
                  elif operation == '2':
                        pass
                  elif operation == '3':
                        pass
                  elif operation == '4':
                        pass
            
            
            # GEO 3D - Pyramid
            
            if shape == '3':
                  print("[Geometry Calculator / 3D / Pyramid]\n"
                        "\n"
                        "1 - Volume\n"
                        "2 - Total Surface Area (TSA)\n"
                        "3 - Lateral Surface Area (LSA)\n"
                        "4 - Slant Height\n"
                        )
                  
                  while True:
                        operation = input("Choose an operation (1-4): ")
                        print_divider()

                        if operation in ['1', '2', '3', '4']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 4.\n")

                  if operation == '1':
                        pass
                  elif operation == '2':
                        pass
                  elif operation == '3':
                        pass
                  elif operation == '4':
                        pass
            
            
            # GEO 3D - Sphere
            
            if shape == '4':
                  print("[Geometry Calculator / 3D / Sphere]\n"
                        "\n"
                        "1 - Volume\n"
                        "2 - Surface Area (SA)\n"
                        "3 - Diameter\n"
                        "4 - Circumference\n"
                        )
                  
                  while True:
                        operation = input("Choose an operation (1-4): ")
                        print_divider()

                        if operation in ['1', '2', '3', '4']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 4.\n")

                  if operation == '1':
                        pass
                  elif operation == '2':
                        pass
                  elif operation == '3':
                        pass
                  elif operation == '4':
                        pass
            
            
            # GEO 3D - Cylinder
            
            if shape == '2':
                  print("[Geometry Calculator / 3D / Cylinder]\n"
                        "\n"
                        "1 - Volume\n"
                        "2 - Total Surface Area (TSA)\n"
                        "3 - Curved Surface Area (CSA)\n"
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