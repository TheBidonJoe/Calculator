# Basic calculator made by TheBidonJoe 05/24 ^_^

# This restarts/loops the program while True.
while True:
    A = input("Enter expression (e.g., 5 + 5): ")

    # We split our components. As the variable, I used "A".
    components = A.split()
    first_number, operator, second_number = components

    if len(components) != 3:
        print("Invalid len of components!")
        exit()

    # Here we type cast our Strings to Integers.
    first_number = int(first_number)
    second_number = int(second_number)

    # This checks the operator and prints the result.
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
            print("Division by zero is not possible!")
            continue
        else:
            result = first_number / second_number
            print("Result is: ", result)
    else:
        print("Invalid operator!")
        continue
    # This lets the user restart or end the program.
    restart = input("Again? (yes/no): ")
    if restart.lower() != "yes":
        print("Goodbye!")
        break
