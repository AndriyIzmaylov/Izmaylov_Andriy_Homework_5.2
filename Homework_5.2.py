# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного
# обчислення - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

from decimal import Decimal, InvalidOperation


def get_input_number(enter_phrase):
    while True:
        user_input_number = input(enter_phrase)
        try:
            return Decimal(user_input_number)
        # We can't change this InvalidOperation error to another builtin error like ValueError
        # because in that case when the user will try to enter a letter for example instead of a number
        # the program will be stopped by error. In caso of InvalidOperation error - program continue his work.
        except InvalidOperation:
            print("Error: Please, enter the correct number of Integer or Decimal")


def get_calculation_operator():
    while True:
        calculation_operator = input("Please, choose the calculation operation (+, -, *, /): ")
        if calculation_operator in ('+', '-', '*', '/'):
            return calculation_operator
        else:
            print("Error: Please, enter the right calculation operation!")


def calculate():
    print("***************** Updated Simple Calculator *****************")
    result = 0
    while True:
        first_entered_number = get_input_number("Please, enter the first number: ")

        chosen_calculation_operator = get_calculation_operator()

        if chosen_calculation_operator == '/':
            while True:
                second_entered_number = get_input_number("Please, enter the second number (the number should not be 0): ")
                if second_entered_number != 0:
                    break
                print("Error: Cannot divide by zero!")
        else:
            second_entered_number = get_input_number("Please, enter the second number: ")

        if chosen_calculation_operator == '+':
            result = first_entered_number + second_entered_number
        elif chosen_calculation_operator == '-':
            result = first_entered_number - second_entered_number
        elif chosen_calculation_operator == '*':
            result = first_entered_number * second_entered_number
        elif chosen_calculation_operator == '/':
            result = first_entered_number / second_entered_number

        print(f"Result: {result}")

        continue_calculation = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if continue_calculation != 'y':
            print("End of program, closing the calculator")
            print("*"*60)
            break


calculate()
