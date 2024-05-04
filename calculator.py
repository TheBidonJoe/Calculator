# Basic calculator made by TheBidonJoe / 02.05.2024

# This restarts/loops the program while it is set to True.
# Have to figure out a way to let the user choose which style he wants to use!
while True:
    print("Please use spaces, like so: 20 + 5")
    Calculation = input("Enter calculation: ")

    #Split the components, used "Calculation" as the variable.
    components = Calculation.split()
    first_number_str, operator, second_number_str = components

    if len(components) != 3:
        print("Invalid len of components!")
        exit()
    #Checks if input is a negative number (e.g. -2).
    try:
        if first_number_str.startswith("(") and first_number_str.endswith(")"):
            first_number_str = first_number_str[1:-1]
        first_number =  float(first_number_str)
        if second_number_str.startswith("(") and second_number_str.endswith(")"):
            second_number_str = second_number_str[1:-1]
        second_number = float(second_number_str)
    except ValueError:
        print("Invalid input!")
        continue

    #Checks inputted operator and prints the corresponding result.
    if operator == "+":
        result = first_number + second_number
        print("Result is: ", result)
    elif operator == "-":
        result = first_number - second_number
        print("Result is: ", result)
    elif operator == "*":
        result = first_number * second_number
        print("Result is: ", result)
    elif operator == "/":
        if second_number == 0:
            print("Division by zero.")
            continue
        else:
            result = first_number / second_number
            print("Result is: ", result)
    else:
        print("Invalid operator!")
        continue
    #Lets the user restart or end the program.
    restart = input("Again? (y/n): ")
    if restart.lower() != "yes" and restart.lower() != "y":
        print("Goodbye.")
        break

