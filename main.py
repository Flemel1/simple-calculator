def calculation(expression):
    operand_1 = int(expression[0])
    operand_2 = int(expression[2])
    operator = expression[1]

    if operator == "*":
        return operand_1 * operand_2
    elif operator == "+":
        return operand_1 + operand_2
    elif operator == "-":
        return operand_1 - operand_2
    elif operator == "/":
        return operand_1 / operand_2
    elif operator == "%":
        return operand_1 % operand_2


user_input = input("Input your expression (Example: 4 * 2): ")
expression = user_input.strip().split()

result = calculation(expression=expression)


print(result)
