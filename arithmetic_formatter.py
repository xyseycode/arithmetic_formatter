def arithmetic_arranger(problems, show_answer=False):

    # Error if more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # for every problem split them into operands and operator
    split_problems = []
    for problem in problems:
        split_problems.append(problem.split())

    # for the lines in the arrangement
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for problem in split_problems:
        # check the operator if it's addition or subtraction
        if problem[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # check if each operands are numbers
        if not problem[0].isdigit() or not problem[2].isdigit():
            return "Error: Numbers must only contain digits."

        # check length of each operand not exceeding 4
        len_operand1 = len(problem[0])
        len_operand2 = len(problem[2])
        if len_operand1 > 4 or len_operand2 > 4:
            return "Error: Numbers cannot be more than four digits."

        # max string length of each problem
        max_length = 2 + max(len_operand1, len_operand2)

        # append every first operand in the first line
        first_line += problem[0].rjust(max_length) + "    "

        # append every second operand and the operator in the 2nd line
        second_line += problem[1] + problem[2].rjust(max_length - 1) + "    "

        # the dashes in the third
        third_line += "-" * max_length + "    "

        # check if answer is to be shown then append the answers on the 4th line
        if show_answer:
            total = 0
            if problem[1] == '+':
                total = int(problem[0]) + int(problem[2])
            else:
                total = int(problem[0]) - int(problem[2])
            str_total = str(total)
            fourth_line += str_total.rjust(max_length) + "    "

    # concatinate all the lines in the arranged_problems variable
    arranged_problems = first_line.rstrip() + "\n" + second_line.strip(
    ) + "\n" + third_line.strip()

    if show_answer:
        arranged_problems += "\n" + fourth_line.rstrip()

    return arranged_problems