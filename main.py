equation = input("Enter an expression: ")

def my_eval(equation):

	equation = rem_whitespace(equation)
	equation = collaps_unary(equation)
	equation = convert_floats(equation)
	equation = club_operators(equation)

	equation = mult_div_collapse(equation)
	equation = add_collapse(equation)
	equation = sub_collapse(equation)
	equation = float(equation[0])

	return equation

def rem_whitespace(equation):
    return list(equation.replace(" ", ""))

def collaps_unary(equation):
	non_unary_symbols = ['.', '*', '/']
	output = []

	plus_cnt = 0
	minus_cnt = 0

	for char in equation:
		if char.isdigit():
			if plus_cnt + minus_cnt == 0:
				output.append(char)
				continue

			elif minus_cnt % 2 == 0:
				output.append("+")

			else:
				output.append("-")

			plus_cnt = 0
			minus_cnt = 0

			output.append(char)
			continue

		elif char in non_unary_symbols:
			output.append(char)

		elif char == '+':
			plus_cnt += 1

		elif char == '-':
			minus_cnt += 1

	res = []
	num = ""
	for char in output:
		if char == '.' or char.isdigit():
			num += char
		elif char in ['*', '/', '-', '+']:
			res.append(num)
			res.append(char)
			num = ""
	res.append(num)

	res = [x for x in res if x != ""]

	return res

def convert_floats(equation):
    for i, char in enumerate(equation):
        if char not in ['+', '-', '*', '/']:
            equation[i] = float(char)
    return equation

def club_operators(equation):
    i = 0
    while i < len(equation) - 1:
        if equation[i] in ('*', '/') and equation[i + 1] in ('+', '-'):
            if equation[i + 1] == '-':
                equation[i + 2] *= -1
            equation.pop(i + 1)
            return club_operators(equation)
        i += 1

    if equation[0] == '-':
    	equation[1] *= -1
    	equation.pop(0)
    elif equation[0] == '+':
    	equation.pop(0)
    return equation

def mult_div_collapse(equation):
	if '*' not in equation and '/' not in equation:
		return equation

	index = 0
	for el in equation:
		if el == "*":
			result = equation[index - 1] * equation[index + 1]
			equation[index] = result
			equation.pop(index + 1)
			equation.pop(index - 1)
			return mult_div_collapse(equation)
		elif el == "/":
			result = equation[index - 1] / equation[index + 1]
			equation[index] = result
			equation.pop(index + 1)
			equation.pop(index - 1)
			return mult_div_collapse(equation)
		index += 1

def add_collapse(equation):
	if '+' not in equation:
		return equation

	index = 0
	for el in equation:
		if el == "+":
			result = equation[index - 1] + equation[index + 1]
			equation[index] = result
			equation.pop(index + 1)
			equation.pop(index - 1)
			return add_collapse(equation)
		index += 1

def sub_collapse(equation):
	if '-' not in equation:
		return equation

	index = 0
	for el in equation:
		if el == "-":
			result = equation[index - 1] - equation[index + 1]
			equation[index] = result
			equation.pop(index + 1)
			equation.pop(index - 1)
			return sub_collapse(equation)
		index += 1

# not correct
# def find_errors(equation):
# 	operators = ["*", "-", "/", "*"]

# 	if equation[0] in ['*', '/'] or equation[-1] in operators:
# 		return True

# 	for i in range(len(equation) - 1):
# 		if equation[i] in operators and operators[i + 1] in operators:
# 			return True
# 	return False

print(my_eval(equation))
print(eval(equation))


