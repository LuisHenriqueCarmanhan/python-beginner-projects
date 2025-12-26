from math import sqrt

print('=' * 30 )
print('   ADVANCED CALCULATOR v1.0   ')
print('=' * 30 )

print('''Available Operations:
[ + ] Sum
[ - ] Subtract
[ * ] Multiply
[ / ] Divide
[ P ] Power (Potenciação)
[ R ] Square Root (Raiz Quadrada)''')

options = input('Choose your operation: ').strip().upper()

if options in ['+', '-', '*', '/', 'P', 'R']:
    # Specific logic for single-number operations
    if options == 'R':
        num = float(input('Enter the number: '))
        if num >= 0:
            print(f'Result: √{num} = {sqrt(num):.2f}')
        else:
            print('Error: Cannot calculate square root of a negative number.')
    # Logic for two-number operations
    else:
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
    
    if options == '+':
        print(f'Result: {n1} + {n2} = {n1 + n2 }')
    elif options == '-':
        print(f'Result: {n1} - {n2} = {n1 - n2 }')
    elif options == '*':
        print(f'Result: {n1} * {n2} = {n1 * n2 }')
    elif options == '/':
        # Defensive programming against division by zero
        if n2 != 0:
            print(f'Result: {n1} / {n2} = {n1 / n2}')
        else:
            print('Error: Division by zero is not allowed.')
    elif options == 'P':
        print(f'Result {n1} ^ {n2} = {n1 ** n2}')
else:
    print('Invalid operation! Please run the program again.')

print('\n--- Calculation Finished ---')
        
        
