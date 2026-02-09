

def my_eval(equation):
	equation = rem_whitespace(equation)
	equation = collaps_unary(equation)


def rem_whitespace(equation):
	return equation.replace(" ", "").split("")

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

			elif plus_cnt < minus_cnt:
				output.append("-")

			else:
				output.append("+")

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

	print(output)

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




print(collaps_unary("+--33.3*-2-+2*--3.55/-2"))

