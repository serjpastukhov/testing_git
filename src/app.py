def fibonacci_while_loop(number):
    """
    Returns *number* number of fibonacci sequence
    'while loop'-based algorithm

    input: number, type int
    output: fibonacci_number, type int
    """
    number_1 = 1
    number_2 = 1

    if number == 1 or number == 2:
        fibonacci_number = 1
    else:
        i = 0
        while i < number - 2:
            fibonacci_number = number_1 + number_2
            number_1 = number_2
            number_2 = fibonacci_number
            i = i + 1

    return fibonacci_number

def fibonacci_for_loop(number):
    """
    Returns *number* number of fibonacci sequence
    'for loop'-based algorithm

    input: number, type int
    output: fibonacci_number, type int
    """
    number_1 = 1
    number_2 = 1

    if number == 1 or number == 2:
        fibonacci_number = 1
    else:
        for i in range(2, number):
            number_1, number_2 = number_2, number_1 + number_2
        fibonacci_number = number_2

    return fibonacci_number

def fibonacci_recursive(number):
    """
    Returns *number* number of fibonacci sequence
    Recursion-based algorithm

    input: number, type int
    output: fibonacci_number, type int
    """
    if number in (1, 2):
            return 1
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


if __name__ == '__main__':
    print(fibonacci_while_loop(35))
    print(fibonacci_for_loop(35))
    print(fibonacci_recursive(35))
    print('Hello, World!')
    print('I have registred here!')