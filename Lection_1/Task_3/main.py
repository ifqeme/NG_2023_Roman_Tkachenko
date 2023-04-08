first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

operation = input("Input operation: «+, -, *, /, ^, sqrt»: ")

match operation:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        result = first_number / second_number
    case "^":
        result = first_number ** second_number
    case "sqrt":
        select_number = input("Choose from which number you want to get the root (1 or 2): ")
        if select_number == "1":
            result = first_number ** (0.5)
        elif select_number == "2":
            result = second_number ** (0.5)
    case _:
        result = "NaN"

print(f"Result: {result}")