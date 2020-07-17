import re

def arithmetic_arranger(problems, answers=False):

    # Accept up to 5 problems
    if len(problems) > 5:
        error = 'Error: Too many problems.'
        print(error)
        return error

    row1 = list()
    row2 = list()
    row3 = list()
    row4 = list()

    for problem in problems:
        # Check the operator
        operator = re.search('[+-]', problem)
        if operator is None:
            error = 'Error: Operator must be \'+\' or \'-\'.'
            print(error)
            return error

        # Separate operands and operator
        operator = operator.group()
        numbers = problem.split(operator)

        # Check if operands are both numeric
        if not numbers[0].strip().isnumeric() or not numbers[1].strip().isnumeric():
            error = 'Error: Numbers must only contain digits.'
            print(error)
            return error
        numTop = numbers[0].strip()
        numBot = numbers[1].strip()

        # Operand length has a max of four digits
        lenTop = len(numTop)
        lenBot = len(numBot)
        if lenTop > 4 or lenBot > 4:
            error = 'Error: Numbers cannot be more than four digits.'
            print(error)
            return error
        
        # Determine longer number in each pair
        diff = lenTop - lenBot
        if diff > 0:                        # Top is longer
            adjustedNum1 = '  ' + numTop
            adjustedNum2 = ' '*diff + ' ' + numBot
        elif diff < 0:                      # Bottom is longer
            adjustedNum1 = ' '*-diff + '  ' + numTop
            adjustedNum2 = ' ' + numBot
        else:                               # Equal length
            adjustedNum1 = '  ' + numTop
            adjustedNum2 = ' ' + numBot

        row1.append('    ' + adjustedNum1)
        row2.append('    ' + operator + adjustedNum2)

        # Bottom Line
        if lenTop > lenBot or lenTop == lenBot:
            dashes = lenTop + 2
        elif lenBot > lenTop:
            dashes = lenBot + 2
        row3.append ('    ' + '-'*dashes)

        if answers is True:
            numTop = int(numTop)
            numBot = int(numBot)
            if operator == '+':
                answer = numTop + numBot
            else:
                answer = numTop - numBot
            answer = str(answer)
            row4.append('    ' + ' '*(dashes-len(answer)) + answer)

    # Print the problems 
    result = ''
    first = True
    for num in row1:
        if first:
            num = num[4:]
            first = False
        result += num
    result += '\n'
    first = True
    for num in row2:
        if first:
            num = num[4:]
            first = False
        result += num
    result += '\n'
    first = True
    for dash in row3:
        if first:
            dash = dash[4:]
            first = False
        result += dash
    result += '\n'
    first = True
    if row4: 
        for answer in row4:
            if first:
                answer = answer[4:]
                first = False
            result += answer

    result = result.rstrip()    # Remove trailing newline...
    print(result)
    return(result)