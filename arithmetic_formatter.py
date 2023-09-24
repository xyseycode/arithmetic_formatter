def arithmetic_arranger(problems):

    # Error if more than 5 problems
    if len(problems) > 5:
        raise Exception('Error: Too many problems.')

    # for every problem split them into operands and operator
    split_problems = []
    for problem in problems:
        split_problems.append(problem.split())

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    ws = "o"

    for problem in split_problems:

        # check the operator if it's addition or subtraction
        if problem[1] not in ['+', '-']:
            raise Exception("Error: Operator must be '+' or '-'.")

        # check if each operands are numbers
        if not problem[0].isdigit() or not problem[2].isdigit():
            raise Exception("Error: Numbers must only contain digits.")

        # check length of each operand not exceeding 4
        len_operand1 = len(problem[0])
        len_operand2 = len(problem[2])
        if len_operand1 > 4 or len_operand2 > 4:
            raise Exception("Error: Numbers cannot be more than four digits.")

        # max string length of each problem
        max_length = 2 + max(len_operand1, len_operand2)
        first_line += ws * (max_length - len_operand1) + problem[0] + "    "
        second_line += problem[1] + " " * (max_length - len_operand2 -
                                           1) + problem[2] + "    "
        third_line += "-" * max_length + "    "
        total = 0
        if problem[1] == '+':
            total = int(problem[0]) + int(problem[2])
        else:
            total = int(problem[0]) - int(problem[2])

        str_total = str(total)

        fourth_line = ws * (max_length - len(str_total)) + str_total + "    "

    arranged_problems = first_line.strip() + "\n" + second_line.strip(
    ) + "\n" + third_line.strip() + "\n" + fourth_line.strip()

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
