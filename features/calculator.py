
import plotext as plt
import numpy as np
import math
import os as iamatrainin
import base64
from pathlib import Path
import runpy as run



def get_project_root():
    """Detects the root project directory regardless of where this is called from."""
    current_path = Path(__file__).resolve().parent
    # If we are inside 'features', go up one more level to reach root
    if current_path.name == "features":
        return current_path.parent
    return current_path


def get_stored_name():
    root = get_project_root()
    folder = root / "system_files"
    filename = folder / "username.bin"

    if filename.exists():
        try:
            # Modern 2025 way: read_bytes() removes the need for 'with open'
            encoded_data = filename.read_bytes()
            return base64.b64decode(encoded_data).decode("utf-8")
        except Exception:
            return None
    return None


def save_name(name):
    root = get_project_root()
    folder = root / "system_files"
    filename = folder / "username.bin"

    permission = input(f"Ok {name}, Can I save your name locally? (Y/N): ")

    if permission.lower() == 'y':
        # Ensure the directory exists at the root level
        folder.mkdir(parents=True, exist_ok=True)

        encoded_name = base64.b64encode(name.encode("utf-8"))

        # Modern 2025 way: write_bytes() handles the file stream for you
        filename.write_bytes(encoded_name)
        print(f"Name stored securely in {filename}")
    else:
        print("Name will not be saved.")


# --- Use these inside your again() function ---
# Improved Arithmetic Example
def perform_arithmetic():
    try:
        count = int(input('How many numbers? '))
        op = input("Operator (+, -, *, /): ")
        result = float(input("Enter number 1: "))

        for i in range(1, count):
            num = float(input(f"Enter number {i + 1}: "))
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "/":
                if num == 0: return print("Error: Division by zero")
                result /= num
        print(f"The answer is: {result}")
    except ValueError:
        print("Invalid input.")
def get_line_equation(x1, y1, x2, y2):
    """
    Calculates the slope (m) and y-intercept (b) for a line 
    passing through two points (x1, y1) and (x2, y2).
    """
    # Check for vertical line (division by zero)                                                                                                                         ....................................................................vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv...................vvvvvvvvvvvvv;dliposuytyfsyetfuenslddjhgygfusjejgyggyguenkdnjfheufskfjhuycnvnb n n n        foipfw fiuofewiuofew iooooooooooooooooooooooooo eLaksiejeijehwwwwwwwwwwww333333333333wwwwwwwwwwweeeeeeee
    if x2 - x1 == 0:
        return None, None 
    # Calculate the slope (m)
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    return m, b

# This fuction's purpose is to calcualte the sine of a number.
# A sine is the ratio of the length of the side opposite the angle to the length of the hypotenuse
def calculate_sine():
    import math
    try:
        angle_degrees = float(input("Enter an angle in degrees to find its sine: "))
        angle_radians = math.radians(angle_degrees)
        sine_result = math.sin(angle_radians)
        print(f"The sine of {angle_degrees} degrees is: {sine_result}")
    except ValueError:
        print("Invalid input. Please enter a numerical value for the angle.")

    # You can call this function within your main calculator loop or directly
    calculate_sine()

# The purpose of this fuction is to tell the suer if any inputs pur in the code are invalid
# Ex. If you tried to add "e" and"f" it would call Invalid()
def Invalid():
    print("Input is Invalid. Please try again.")
# These list the valid operators used in Arithmetic
def Operators():
    print("addition = +")
    print("subtraction = -")
    print("multiplication = *")
    print("division = /")
# All of this stuff needs answers, this is just telling the user "The answer is...."
def AnswerIs():
    print("The answer is...")
# Idk why this is ehre but itll break the code if i remove it (it has 13 usages) so uh its here i guess
def emptyLine():
    print()
#for fuctions
def plot_function_console(expression, x_min=-10, x_max=10, num_points=100):
    """
    Evaluates and plots a mathematical expression in the console.
    """
    x = np.linspace(x_min, x_max, num_points)
    y = []
    for val in x:
        try:
            # Safely evaluate the expression.
            # Use a dictionary to provide allowed functions and variables
            # to prevent security issues with arbitrary code execution.
            scope = {"x": val, "math": math, "sin": math.sin, "cos": math.cos, "sqrt": math.sqrt, "pi": math.pi}
            result = eval(expression, {"__builtins__": None}, scope)
            y.append(result)
        except Exception as e:
            print(f"Error evaluating expression at x={val}: {e}")
            return

    plt.scatter(x, y)
    plt.title(f"Plot of y = {expression}")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()
''' This is the fuction contining the src code, allowing it to be repeated. If you have
a better idea, create a pull rq.'''
def again():
    import math
    import time
    import plotext as plt
    import numpy as np
    arithnum = 0
    # Try to load existing name
    name = get_stored_name()

    if name:
        print(f"Welcome back, {name}!")
    else:
        name = input("What's your name? ")
        save_name(name)
        print(f"Hello, {name}!")
    time.sleep(0.47567)
    print('Welcome to to the snake calculator!')
    time.sleep(0.376786777777777777887669814)
    print('How may I help you today? ')
    print('The following is case sensitive.')
    emptyLine()
    time.sleep(0.67)
    print('Please write your choice as a number from 1-13, determined by the order of the following')
    print("1 - Arithmetic (Still trying to find out how to do division here)")
    print("2 - square root")
    print("3 - exponents")
    print("4 - Fraction to Decimal Conversion")
    print('5 - cube root ')
    print("6 - abs value")
    print("7 - factorial")
    print("8 - logarithm")
    print("9 - Floor Division")
    print("10 - area (Square, Triangle)")
    print("11 - perimeter")
    print("12 - sine")
    print("13 - triangle angles")
    print("14 - Greatest Common Factor")
    print("15 - equations (one-variable)")
    print("16 - Rounding")
    print("17 - functions")
    print("18 - Go back")
    print("19 - Switch to games menu")
    while True:
        try:
            choice = int(input("Please enter your number "))
            break
        except ValueError:
            Invalid()
    if choice == 1:
        perform_arithmetic()
    elif choice == 2:
        square_root = int(input('What number would you like me to get the square root of? '))
        square_root2 = str(math.sqrt(square_root))
        print(square_root2 + ' is the square root of ' + str(square_root))
    elif choice == 3:
        exponents = int(input('What number would to like me to find the ___ power of? '))
        exponents2 = int(input('What power would you like me to raise your number to? '))
        emptyLine()
        emptyLine()
        print(exponents ** exponents2, " is your answer!")
        time.sleep(2)
    elif choice == 4:
        F_to_Dnum = input('numerator? ')
        F_to_Dden = input("Denominator? ")
        F_to_Dans = int(F_to_Dnum)/int(F_to_Dden)
        print(F_to_Dans)
        print(" ")
        print("answer is above!")
        
        print(f" {F_to_Dans} Is the decimal equivalent of {F_to_Dnum}" )
    elif choice == 5:
        croot = float(input("What number would you like me to get the cube root of? "))
        emptyLine()
        emptyLine()
        print(f"The cube root of  {str(croot)} is...")
        print(croot ** (1 / 3))
    elif choice == 6:
        emptyLine()
        absval = int(input("What would you like the absolute value of? "))
        absval2 = abs(absval)
        print(f"the absolute value of {str(absval)} is {absval2}")
    elif choice == 7:
        emptyLine()
        factorialvalue = input("what number would you like me to get the factorial of? ")
        print("The facotrial of " + str(factorialvalue) + " is...")
        emptyLine()
        emptyLine()
        print(math.factorial(int(factorialvalue)))
    elif choice == 8:
        emptyLine()
        logbase = input("what is the base of your logarithm? ")
        logexpo = input("what is the exponent of your logarithm? ")
        print("the anser to your logarithm with base " + str(logbase) + " and exponent " + str(logexpo) + " is...")
        print(math.log(int(logexpo), int(logbase)))
    elif choice == 9:
        emptyLine()
        print("So you have chosen floor division.")
        print("If you didn't know, floor division is")
        print("just division, but rounding down to")
        print("a whole number.")
        floordivend = int(input("What is the dividend? "))
        floordivisor = int(input("What is the divisor? "))
        print("Your answer is...")
        print(".")
        time.sleep(0.54)
        print(".")
        print(floordivend//floordivisor)
    elif choice == 10:
        while True:
            shape = input("Square or Triangle? ")
            if shape == "Square":
                try:
                    squ_sides = int(input("what is the side length of the square? "))
                    print(squ_sides * squ_sides)
                    print("The answer is above!")
                    break
                except ValueError:
                    Invalid()
            elif shape == "square":
                while True:
                    try:
                        squ_sidesl = int(input("what is the side length of the square?"))
                        print(squ_sidesl * squ_sidesl)
                        print("The answer is above!    ")
                        break
                    except ValueError:
                        Invalid()
                    
            elif shape == "triangle":
                while True:
                    try:
                        basetri = int(input("base? "))
                        heighttri = int(input("height? "))
                        bplush = basetri * heighttri
                        triarea = bplush / 2
                        AnswerIs()
                        print(str(triarea))
                        break
                    except ValueError:
                        Invalid() 
            elif shape == "Triangle":
                while True:
                    try:
                        basetri = int(input("base? "))
                        heighttri = int(input("height? "))
                        bplush = basetri * heighttri
                        triarea = bplush / 2
                        AnswerIs()
                        print(str(triarea))
                        break
                    except ValueError:
                        Invalid()
    elif choice == 11 :
        while True:
            try:    
                sidescount = int(input("how many sides does your shape have? "))
                sidesunit = str(input("what unit would you like me to use?"))
                break
            except ValueError:
                Invalid()
        perimeter = 0
        for guysyallneedtostopwiththe67brainrotitssoweirsandweneedtofixtheworldandlucianogetoffrobloxpleaseyourelectricitybillissocookedman in range(sidescount):
            while True:
                try:
                    num = int(input(f"Enter side number {guysyallneedtostopwiththe67brainrotitssoweirsandweneedtofixtheworldandlucianogetoffrobloxpleaseyourelectricitybillissocookedman + 1}: "))
                    perimeter += num
                    break
                except ValueError:
                    Invalid()
        AnswerIs()
        print(str(perimeter) + sidesunit + "!")
    elif choice == 12:
        calculate_sine()
    elif choice == 13:
        print("Give me two angles of a triangle and i will give you the third one.")
        while True:
            try:
                randangle1 = int(input("Enter side number 1: "))
                randangle2 = int(input("Enter side number 2: "))
                break
            except ValueError:
                print("Sorry, invalid input")
        calcangle = randangle1 + randangle2
        thirdangle = 180 - calcangle
        print("The third angle is...")
        time.sleep(0.4)
        print(str(calcangle) + '°!')    
    elif choice == 14:
        print("Greatest Common Factor = GCF")
        firstgcf = input("What is the first number you would like to get the GCF of? ")
        secgcf = input("what is your second number? ")
        import math

# Calculate the GCF (GCD)
        gcf_value = math.gcd(int(firstgcf), int(secgcf))

# Print the result
        

        print("The result of the GCF of " + firstgcf + " and " + secgcf + " is..")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(str(gcf_value) + "!")
    elif choice == 15:
        print("Enter the coordinates for the first point:")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        print("Enter the coordinates for the second point:")
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))

        slope, y_intercept = get_line_equation(x1, y1, x2, y2)
        if slope is None:
            print(f"This is a vertical line with the equation: x = {x1}")
        else:
            # Indentation corrected for the 'else' block content
            sign = " + " if y_intercept >= 0 else " - "
            formatted_intercept = abs(y_intercept) 
            print(f"The equation of the line is: y = {slope}x{sign}{formatted_intercept}")
    elif choice == 16:
        try:
            # Get the number to be rounded
            number_to_round = float(input("Enter the number you want to round: "))

            # Display the rounding sub-menu
            print("\n--- Rounding Options ---")
            print("1. Nearest Integer")
            print("2. Nearest Tenth (1 decimal place)")
            print("3. Nearest Hundredth (2 decimal places)")
            print("4. Nearest Thousandth (3 decimal places)")

        # Get the user's choice for rounding
            round_choice = input("Enter your choice (1, 2, 3, or 4): ")
        
            rounded_result = None

            if round_choice == '1':
                rounded_result = round(number_to_round, 0)
                print(f"Result rounded to nearest integer: {rounded_result}")
            elif round_choice == '2':
                rounded_result = round(number_to_round, 1)
                print(f"Result rounded to nearest tenth: {rounded_result}")
            elif round_choice == '3':
                rounded_result = round(number_to_round, 2)
                print(f"Result rounded to nearest hundredth: {rounded_result}")
            elif round_choice == '4':
                rounded_result = round(number_to_round, 3)
                print(f"Result rounded to nearest thousandth: {rounded_result}")
            else:
                print("Invalid rounding choice. Please select from 1, 2, 3, or 4.")
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == 17:
            user_input = input("Enter a function to plot (e.g., 'math.sin(x)' or 'x**2') or 'quit': ")
            if user_input.lower() == 'quit':
                quit()
            plot_function_console(user_input)
    elif choice == 18:
        run.run_path("./main.py")
    elif choice == 19:
        print("Switching to games menu...")
        run.run_path("./features/GameHub/games.py")
    elif choice == 67:
        # Indentation corrected
        print("6-6-6-6-6-6-7-7-- SIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENvSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVEN")
        quit()
    elif choice == 21:
        # Indentation corrected
        print("I would be very good friends with you lol")
    else:
        # Indentation corrected
        print("what you have entered has not been added yet, is invalid, or has a typo. Please try again. Thank you.")
        again()
    



    time.sleep(1.3141592653859)
    emptyLine()
    emptyLine()
    calcagain = input("Wanna use this program again? (Y/N) ")
    if calcagain == "Y" or calcagain == "y":
        again()
    elif calcagain == "n" or calcagain == "N":
        print('Thank you for using snake calculator, ' + name + '! I wish you a great day!')

#----------main script---------

# calls the fuction to start the code.
again()





