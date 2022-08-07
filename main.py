def calculater(trulala: int, second_input: int, char):

    if char == '+':
        total = trulala + second_input
    elif char == '-':
        total = trulala - second_input
    elif char == '*':
        total = trulala * second_input
    elif char == '/':
        total = trulala / second_input
    return total

first_input = input('Enter a number: ')
char = input('Enter a char: ')
second_input = input('Enter a number: ')

my_list = ['+', '-', '*', '/']
# if char == '+' or char == '-' or char == '*' or char == '/':
if char in my_list:
    if first_input.isnumeric() == True and second_input.isnumeric() == True:
        result = calculater(int(first_input), int(second_input), char)
    else:
        result = 'ты лошара по числам'
else:
        result = 'ты лошара по знакам'

print(result)
