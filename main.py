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
      elif operation == 'area3':
            get_operation = get_shape.area3()
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
      elif operation == 'tsa2':
            get_operation = get_shape.tsa2()
      elif operation == 'lsa2':
            get_operation = get_shape.lsa2()
      elif operation == 'base_area':
            get_operation = get_shape.base_area()
      elif operation == 'base_area2':
            get_operation = get_shape.base_area2()
      elif operation == 'volume':
            get_operation = get_shape.volume()
      elif operation == 'volume2':
            get_operation = get_shape.volume2()
      print_divider()
      print(f"Your answer is {get_operation:.2f}")
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
      elif operation == 'angle4':
            get_operation = get_shape.angle4()
      elif operation == 'angle5':
            get_operation = get_shape.angle5()
      elif operation == 'angle6':
            get_operation = get_shape.angle6()
      elif operation == 'volume':
            get_operation = get_shape.volume()
      elif operation == 'volume2':
            get_operation = get_shape.volume2()
      elif operation == 'volume3':
            get_operation = get_shape.volume3()
      elif operation == 'volume4':
            get_operation = get_shape.volume4()
      elif operation == 'tsa':
            get_operation = get_shape.tsa()
      elif operation == 'tsa2':
            get_operation = get_shape.tsa2()
      elif operation == 'tsa3':
            get_operation = get_shape.tsa3()
      elif operation == 'tsa4':
            get_operation = get_shape.tsa4()
      elif operation == 'csa':
            get_operation = get_shape.csa()
      elif operation == 'csa2':
            get_operation = get_shape.csa2()
      elif operation == 'csa3':
            get_operation = get_shape.csa3()
      elif operation == 'csa4':
            get_operation = get_shape.csa4()
      elif operation == 'base_area3':
            get_operation = get_shape.base_area3()
      elif operation == 'slant_height':
            get_operation = get_shape.slant_height()
      print_divider()
      print(f"Your answer is {get_operation:.2f}")
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
      elif operation == 'volume':
            get_operation = get_shape.volume()
      elif operation == 'tsa':
            get_operation = get_shape.tsa()
      elif operation == 'lsa':
            get_operation = get_shape.lsa()
      elif operation == 'space_diagonal':
            get_operation = get_shape.space_diagonal()
      
      print_divider()
      print(f"Your answer is {get_operation:.2f}")
      print_divider()

def geo_four_inputs_flow(page_name, label1, label2, label3, label4, calculation, arg1, arg2, arg3, arg4, operation):
      """Control repetition and consistency for four user inputs in the geometry calculator."""
      print(f"[Standard Calculator / 2D / {page_name}]\n")
      num1 = float(input(f"Input the {label1}: "))
      num2 = float(input(f"Input the {label2}: "))
      num3 = float(input(f"Input the {label3}: "))
      num4 = float(input(f"Input the {label4}: "))
      arguments = {arg1: num1, arg2: num2, arg3: num3, arg4: num4}
      get_shape = calculation(**arguments)
      
      if operation == 'tsa':
            get_operation = get_shape.area()
      
      print_divider()
      print(f"Your answer is {get_operation:.2f}")
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
                                    
                        if operation == '1':
                              print("[Geometry Calculator / 2D / Triangle / Right-angle]\n"
                                          "\n"
                                          "How would you like to calculate?\n"
                                          "1 - Base and height\n"
                                          "2 - a hypotenuse + leg side"
                                          )
                              while True:
                                          approach = input("Enter your approach (1-2): ")
                                          print_divider()

                                          if approach in ['1', '2']:
                                                break
                                          else:
                                                print("Invalid! Please enter 1 or 2.\n")
                              if approach == '1':
                                    base = float(input('Enter length of Base: '))
                                    height = float(input('Enter length of Height: '))
                                    area = 0.5 * base * height
                                    print(f'Area = {area:.2f}')
                              elif approach == '2':
                                    hyp = float(input('Enter length of Hyp: '))
                                    side = float(input("Enter length of 'leg': "))
                                    side2 = math.sqrt(pow(hyp, 2)- pow(side, 2))
                                    area = 0.5 * side * side
                                    print(f'Area = {area:.2f}')

                        elif operation == '2':
                              print("[Geometry Calculator / 2D / Triangle / Right-angle]\n"
                                          "\n"
                                          "How would you like to calculate?\n"
                                          "1 - Two 'leg' sides\n"
                                          "2 - a hypotenuse + leg side"
                                          )
                              while True:
                                          approach = input("Enter your approach (1-2): ")
                                          print_divider()

                                          if approach in ['1', '2']:
                                                break
                                          else:
                                                print("Invalid! Please enter 1 or 2.\n")
                              if approach == '1':
                                    side = float(input("Enter length of leg 1: "))
                                    side2 = float(input("Enter length of leg 2: "))
                                    hyp = math.sqrt(pow(side, 2) + pow(side2, 2))
                                    perimeter = side + side2 + hyp
                                    print(f'Perimeter = {perimeter:.2f}')
                              elif approach == '2':
                                    side = float(input("Enter length of known leg: "))
                                    hyp = float(input("Enter length of hyp: "))
                                    side2 = math.sqrt(pow(hyp, 2) - pow(side, 2))
                                    perimeter = side + side2 + hyp
                                    print(f'Perimeter = {perimeter:.2f}') #Hi gang can you integrate this to your function

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
                                    elif inv_sides == '1' and known_side == '2':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of opposite", "angle", calc.Triangle, "num1", "num2", "side_sct_hyp")
                                    elif inv_sides == '2' and known_side == '1':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of hypotenuse", "angle", calc.Triangle, "num1", "num2", "side_sct_adj")
                                    elif inv_sides == '2' and known_side == '3':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of adjacent", "angle", calc.Triangle, "num1", "num2", "side_sct_hyp2")
                                    elif inv_sides == '3' and known_side == '2':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of opposite", "angle", calc.Triangle, "num1", "num2", "side_sct_adj2")
                                    elif inv_sides == '3' and known_side == '3':
                                          geo_two_inputs_flow("Triangle / Right-angle / Side / SOHCAHTOA Formula", "length of adjacent", "angle", calc.Triangle, "num1", "num2", "side_sct_opp2")

                        elif operation == '4':
                              print("[Geometry Calculator / 2D / Triangle / Right-angle / Angle]\n"
                                          "\n"
                                          "Which sides are involved?\n"
                                          "\n"
                                          "1 - Hypotenuse & Opposite (SOH)\n" 
                                          "2 - Hypotenuse & Adjacent (CAH\n"
                                          "3 - Opposite & Adjacent (TOA)\n"
                                          ) 

                              while True:
                                    inv_sides = input("Choose involved sides (1-3): ")
                                    print_divider()

                                    if inv_sides in ['1', '2', '3']:
                                          break
                                    else:
                                          print("Invalid! Please enter a number between 1 to 3.\n")
                              if inv_sides == '1':
                                    geo_two_inputs_flow("Triangle / Right-angle / Angle / SOH", "length of hypotenuse", "length of opposite", calc.Triangle, "num1", "num2", "angle4")
                                    # hyp = float(input('Enter length of hypotenuse: '))
                                    # opp = float(input('Enter length of opposite: '))
                                    # angle = math.degrees(math.asin(opp/hyp))
                                    # print(f'Angle = {angle:.2f} deg')
                              elif inv_sides == '2':
                                    geo_two_inputs_flow("Triangle / Right-angle / Angle / CAH", "length of hypotenuse", "length of adjacent", calc.Triangle, "num1", "num2", "angle5")
                                    # hyp = float(input('Enter length of hypotenuse: '))
                                    # adj = float(input('Enter length of adjacent: '))
                                    # angle = math.degrees(math.acos(adj/hyp))
                                    # print(f'Angle = {angle:.2f} deg')
                              elif inv_sides == '3':
                                    geo_two_inputs_flow("Triangle / Right-angle / Angle / TOA", "length of opposite", "length of adjacent", calc.Triangle, "num1", "num2", "angle6")
                                    # opp = float(input('Enter length of opposite: '))
                                    # adj = float(input('Enter length of adjacent: '))
                                    # angle = math.degrees(math.atan(opp/adj))
                                    # print(f'Angle = {angle:.2f} deg')

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
                                    "1 - Two Angles\n"
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
                              "Select calculation approach\n"
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
                        elif calc_method == '2':
                              geo_two_inputs_flow("Circle / Angle of a Sector", "radius", "arc", calc.Circle, "num1", "num2", "angle_of_sector2")
      
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
                        print("[Geometry Calculator / 3D / Cuboid / Volume]\n"
                              "\n"
                              "Select calculation approach\n"
                              "\n"
                              "1 - Length & Width & Height\n"
                              "2 - Face area & Height\n"
                              )
                        while True:
                              approach = input("Choose an operation (1-2): ")
                              print_divider()

                              if approach in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")
                        if approach == '1':
                              geo_three_inputs_flow("Cuboid / Volume", "Length", "width", "height", calc.Cuboid, "num1", "num2", "num3", "volume")
                        elif approach == '2':
                              geo_two_inputs_flow("Cuboid / Volume", "Face Area", "Height", calc.Cuboid, "num1", "num2", "volume2")
                  elif operation == '2':
                        print("[Geometry Calculator / 3D / Cuboid / TSA]\n"
                              "\n"
                              "Select calculation approach\n"
                              "\n"
                              "1 - Length & Width & Height (cuboid)\n"
                              "2 - (for cube) a length\n"
                              )
                        while True:
                              approach = input("Choose an operation (1-2): ")
                              print_divider()

                              if approach in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")
                        if approach == '1':
                              geo_three_inputs_flow("Cuboid / TSA", "Length", "Width", "Height", calc.Cuboid, "num1", "num2", "num3", "tsa")
                        elif approach == '2':
                              geo_one_input_flow("Cuboid / TSA", "Length", calc.Cuboid, "num1", "tsa2")
                  elif operation == '3': #LSA
                        print("[Geometry Calculator / 3D / Cuboid / LSA]\n"
                              "\n"
                              "Select calculation approach\n"
                              "\n"
                              "1 - Length & Width & Height (cuboid)\n"
                              "2 - (for cube) a length\n"
                              )
                        while True:
                              approach = input("Choose an operation (1-2): ")
                              print_divider()

                              if approach in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")
                        if approach == '1':
                              geo_three_inputs_flow("Cuboid / LSA", "Length", "Width", "Height", calc.Cuboid, "num1", "num2", "num3", "lsa")
                        elif approach == '2':
                              geo_one_input_flow("Cuboid / LSA", "side Length", calc.Cuboid, "num1", "lsa2")
                  elif operation == '4':
                        geo_three_inputs_flow("Cuboid / Space Diagonal", "Length", "Width", "Height", calc.Cuboid, "num1", "num2", "num3", "space_diagonal")


            # GEO 3D - Cone
            
            if shape == '2':
                  print("[Geometry Calculator / 3D / Cone]\n"
                        "\n"
                        "1 - Volume\n"
                        "2 - Total Surface Area (TSA)\n"
                        "3 - Curved Surface Area (CSA)\n"
                        "4 - Base Area\n"
                        "5 - Slant Height\n"
                        )
                  
                  while True:
                        operation = input("Choose an operation (1-7): ")
                        print_divider()

                        if operation in ['1', '2', '3', '4', '5', '6', '7']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 7.\n")

                  if operation == '1':
                        print("[Geometry Calculator / 3D / Cone / Volume]\n"
                              "\n"
                              "Select calculation approach\n"
                              "\n"
                              "1 - Radius & Height\n"
                              "2 - Base Area & Height\n"
                              "3 - Radius & Slant Height\n"
                              "4 - Height & Slant Height\n"
                              )
                        while True:
                              approach = input("Choose an operation (1-4): ")
                              print_divider()

                              if approach in ['1', '2', '3', '4']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 4.\n")
                        if approach == '1':
                              geo_two_inputs_flow("Cone / Volume", "Radius", "Height", calc.Cone, "num1", "num2", "volume")
                        elif approach == '2':
                              geo_two_inputs_flow("Cone / Volume", "Height", "Base Area", calc.Cone, "num1", "num2", "volume2")
                        elif approach == '3':
                              geo_two_inputs_flow("Cone / Volume", "Radius", "Slant height", calc.Cone, "num1", "num2", "volume3")
                        elif approach == '4':
                              geo_two_inputs_flow("Cone / Volume", "Height", "Slant height", calc.Cone, "num1", "num2", "volume4")
                                    
                  elif operation == '2':
                        print("[Geometry Calculator / 3D / Cone / TSA]\n"
                              "\n"
                              "Select calculation approach\n"
                              "\n"
                              "1 - Radius & Slant height\n"
                              "2 - Radius & Height\n"
                              "3 - Base Area & Slant Height\n"
                              "4 - Base Area & Height\n"
                              )
                        while True:
                              approach = input("Choose an operation (1-4): ")
                              print_divider()

                              if approach in ['1', '2', '3', '4']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 4.\n")
                        if approach == '1':
                              geo_two_inputs_flow("Cone / TSA", "Radius", "Slant Height", calc.Cone, "num1", "num2", "tsa")
                        elif approach == '2':
                              geo_two_inputs_flow("Cone / TSA", "Radius", "Height", calc.Cone, "num1", "num2", "tsa2")
                        elif approach == '3':
                              geo_two_inputs_flow("Cone / TSA", "Base Area", "Slant height", calc.Cone, "num1", "num2", "tsa3")
                        elif approach == '4':
                              geo_two_inputs_flow("Cone / TSA", "Base Area", "height", calc.Cone, "num1", "num2", "tsa4")
                  elif operation == '3':
                        print("[Geometry Calculator / 3D / Cone / CSA]\n"
                              "\n"
                              "Select calculation approach\n"
                              "\n"
                              "1 - Radius & Slant height\n"
                              "2 - Radius & Height\n"
                              "3 - Base Area & Slant Height\n"
                              "4 - Base Area & Height\n"
                              )
                        while True:
                              approach = input("Choose an operation (1-4): ")
                              print_divider()

                              if approach in ['1', '2', '3', '4']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 4.\n")
                        if approach == '1':
                              geo_two_inputs_flow("Cone / CSA", "Radius", " Slant Height", calc.Cone, "num1", "num2", "csa")
                        elif approach == '2':
                              geo_two_inputs_flow("Cone / CSA", "Radius", "Height", calc.Cone, "num1", "num2", "csa2")
                        elif approach == '3':
                              geo_two_inputs_flow("Cone / CSA", "Base Area", "Slant Height", calc.Cone, "num1", "num2", "csa3")
                        elif approach == '4':
                              geo_two_inputs_flow("Cone / CSA", "Base Area", "Height", calc.Cone, "num1", "num2", "csa4")
                  elif operation == '4':
                        print("[Geometry Calculator / 3D / Cone / Base Area]\n"
                              "\n"
                              "Select calculation approach\n"
                              "\n"
                              "1 - Radius\n"
                              "2 - Circumference\n"
                              "3 - Height and slant height\n"
                              )
                        while True:
                              approach = input("Choose an operation (1-3): ")
                              print_divider()

                              if approach in ['1', '2', '3',]:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")
                        if approach == '1':
                              geo_one_input_flow("Cone / Base Area", "Radius", calc.Cone, "num1", "base_area")
                        if approach == '2':
                              geo_one_input_flow("Cone / Base Area", "Circumference", calc.Cone, "num1", "base_area2")
                        if approach == '3':
                              geo_two_inputs_flow("Cone / Base Area", "Height", "Slant Height", calc.Cone, "num1", "num2", "base_area3")
                  elif operation == '5':
                        geo_two_inputs_flow("Cone / Slant Height", "Radius", "Height", calc.Cone, "num1", "num2", "slant_height")
            
            
            # GEO 3D - Pyramid
            
            if shape == '3':
                  print("[Geometry Calculator / 3D / Pyramid]\n"
                        "\n"
                        "1 - Square/Rectangular Pyramid\n"
                        "2 - Triangular Pyramid\n"
                        )
                  while True:
                              type = input("Choose pyramid type (1-2): ")
                              print_divider()

                              if operation in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")
                  if type == '1':
                        print("[Geometry Calculator / 3D / Pyramid / Square-Rectangular Pyramid]\n"
                              "\n"
                              "1 - Volume\n"
                              "2 - Total Surface Area (TSA)\n"
                              "3 - Lateral Surface Area (LSA)\n"
                              "5 - Slant Height\n"
                              )
                        
                        while True:
                              operation = input("Choose an operation (1-4): ")
                              print_divider()

                              if operation in ['1', '2', '3', '4']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 4.\n")

                        if operation == '1':
                              print("[Geometry Calculator / 3D / Pyramid / Square-Rectangualar Pyramid / Volume]\n"
                                    "\n"
                                    "Select calculation approach\n"
                                    "\n"
                                    "1 - Base Area & Height\n"
                                    "2 - Lenght & Width & Height "
                                    )
                              while True:
                                    approach = input("Choose an operation (1-2): ")
                                    print_divider()

                                    if approach in ['1', '2']:
                                          break
                                    else:
                                          print("Invalid! Please enter a number between 1 to 2.\n")
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
                        "3 - Cross-Sectional: Area, Circumference, diameter\n"
                        )
                  
                  while True:
                        operation = input("Choose an operation (1-4): ")
                        print_divider()

                        if operation in ['1', '2', '3', '4']:
                              break
                        else:
                              print("Invalid! Please enter a number between 1 to 4.\n")

                  if operation == '1':
                        print("[Geometry Calculator / 3D / Sphere / Volume]\n"
                              "\n"
                              "1 - radius\n"
                              "2 - Circumference\n"
                              )
                        
                        while True:
                              approach = input("Choose an calculation approach (1-2): ")
                              print_divider()

                              if approach in ['1', '2']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 2.\n")
                        if approach == '1':
                              geo_one_input_flow("Geometry Calculator / 3D / Sphere / Volume", "Radius", calc.Sphere, "num1", "volume")
                        elif approach == '2':
                              geo_one_input_flow("Geometry Calculator / 3D / Sphere / Volume", "Circumference", calc.Sphere, "num1", "volume2")
                  elif operation == '2':
                        print("[Geometry Calculator / 3D / Sphere / Surface Area]\n"
                              "\n"
                              "1 - radius\n"
                              "2 - Circumference\n"
                              "3 - Volume\n"
                              )
                        
                        while True:
                              approach = input("Choose an calculation approach (1-3): ")
                              print_divider()

                              if approach in ['1', '2', '3']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")
                        if approach == '1':
                              geo_one_input_flow("Geometry Calculator / 3D / Sphere / Surface Area", "Radius", calc.Sphere, "num1", "area")
                        elif approach == '2':
                              geo_one_input_flow("Geometry Calculator / 3D / Sphere / Surface Area", "Circumference", calc.Sphere, "num1", "area2")
                        elif approach == '3':
                              geo_one_input_flow("Geometry Calculator / 3D / Sphere / Surface Area", "Volume", calc.Sphere, "num1", "area3")
                  elif operation == '3':
                        radius = float('Input The Radius: ')
                        diameter = radius * 2
                        circumference = 2 * math.pi * radius
                        area = math.pi * (radius**2)
                        print(f'Diameter: {diameter}'
                              f'Circumference: {circumference}'
                              f'Cross-section Area: {area}')
            
            
            # GEO 3D - Cylinder
            
            if shape == '5':
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
                        print("[Geometry Calculator / 3D / Cylinder / Volume]\n"
                              "\n"
                              "1 - Radius & Height\n"
                              "2 - Base Area & Height\n"
                              "3 - Circumference & Height\n"
                              )                      
                        while True:
                              approach = input("Choose an calculation approach (1-3): ")
                              print_divider()

                              if approach in ['1', '2', '3']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")
                        if approach == '1':
                              geo_two_inputs_flow("Cylinder / Volume", "Radius", "Height", calc.Cylinder, "num1", "num2", "volume")
                        elif approach == '2':
                              geo_two_inputs_flow("Cylinder / Volume", "Base Area", "Height", calc.Cylinder, "num1", "num2", "volume2")
                        elif approach == '3':
                              geo_two_inputs_flow("Cylinder / Volume", "Circumference", "Height", calc.Cylinder, "num1", "num2", "volume3")
                  elif operation == '2':
                        print("[Geometry Calculator / 3D / Cylinder / TSA]\n"
                              "\n"
                              "1 - Radius & Height\n"
                              "2 - Base Area & Height\n"
                              "3 - Circumference & Height\n"
                              )                      
                        while True:
                              approach = input("Choose an calculation approach (1-3): ")
                              print_divider()

                              if approach in ['1', '2', '3']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")
                        if approach == '1':
                              geo_two_inputs_flow("Cylinder / TSA", "Radius", "Height", calc.Cylinder, "num1", "num2", "tsa")
                        elif approach == '2':
                              geo_two_inputs_flow("Cylinder / TSA", "Base Area", "Height", calc.Cylinder, "num1", "num2", "tsa2")
                        elif approach == '3':
                              geo_two_inputs_flow("Cylinder / TSA", "Circumference", "Height", calc.Cylinder, "num1", "num2", "tsa3")
                  elif operation == '3':
                        print("[Geometry Calculator / 3D / Cylinder / CSA]\n"
                              "\n"
                              "1 - Radius & Height\n"
                              "2 - Base Area & Height\n"
                              "3 - Circumference & Height\n"
                              )                      
                        while True:
                              approach = input("Choose an calculation approach (1-3): ")
                              print_divider()

                              if approach in ['1', '2', '3']:
                                    break
                              else:
                                    print("Invalid! Please enter a number between 1 to 3.\n")
                        if approach == '1':
                              geo_two_inputs_flow("Cylinder / CSA", "Radius", "Height", calc.Cylinder, "num1", "num2", "csa")
                        elif approach == '2':
                              geo_two_inputs_flow("Cylinder / CSA", "Base Area", "Height", calc.Cylinder, "num1", "num2", "csa2")
                        elif approach == '3':
                              geo_two_inputs_flow("Cylinder / CSA", "Circumference", "Height", calc.Cylinder, "num1", "num2", "csa3")