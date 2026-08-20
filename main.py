
def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        # Split the problem
        parts = problem.split()

        first = parts[0]
        operator = parts[1]
        second = parts[2]
    #operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
    #digits
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'
    #length
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        width = max(len(first), len(second)) + 2

        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        dashes_line.append("-" * width)
        if show_answers:
            if operator == "+":
                answer = int(first) + int(second)
            else:
                answer = int(first) - int(second)
            answers_line.append(str(answer).rjust(width))

    arranged_problems = "    ".join(first_line)
    arranged_problems += "\n" + "    ".join(second_line)
    arranged_problems += "\n" + "    ".join(dashes_line)
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers_line)
    return arranged_problems

    print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')