def arithmetic_formatter(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    re_number = []
    re_operator = []
    re_dash = []

    for p in problems:
        number = p.split()
        number1, operator, number2 = number

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not number1.isdigit() or not number2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        maxlength = max(len(number1), len(number2))
        re_number.append(number1.rjust(maxlength + 2))
        re_operator.append(operator + ' ' + number2.rjust(maxlength))
        re_dash.append('-' * (maxlength + 2))
    
    output = '    '.join(re_number) + '\n'
    output += '    '.join(re_operator) + '\n'
    output += '    '.join(re_dash)

    if answer:
        final_answers = []
        for p in problems:
            number = p.split()
            number1, operator, number2 = number
            result = str(eval(p))
            max_length = max(len(number1), len(number2)) + 2
            final_answers.append(result.rjust(max_length))
        output += '\n' + '    '.join(final_answers)
    return output

print(arithmetic_formatter(["32 + 8", "1 - 3801", "9999 + 9999", "531 + 56", "12 + 24"], True))