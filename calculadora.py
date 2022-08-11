def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for substraction
    * for multiplication
    / for division
    ''')

    number_1 = int(input('Enter yout first number: '))
    number_2 = int(input('Enter yout second number: '))

    # Sum
    def invokeSum(number_1, number_2):
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    # Subtraction
    def invokeSub(number_1, number_2):
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    # Multiplication
    def invokeMult(number_1, number_2):
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    # Division
    def invokeDiv(number_1, number_2):
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    if operation == '+':
        invokeSum(number_1, number_2)
    elif operation == '-':
        invokeSub(number_1, number_2)
    elif operation == '*':
        invokeMult(number_1, number_2)
    elif operation == '/':
        invokeDiv(number_1, number_2)
    else:
        print('You have not typed a valid operator, please run the program again.')
    again()

def again():
    calc_again = input('''
    Do you want to calculate again?
    ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()