print('┌' + '─' * 38 + '┐')
print('│   TRIANGLE VALIDATOR AND CLASSIFIER  │')
print('└' + '─' * 38 + '┘')
print('Scanning segments in the Construct...\n')

# Input for the three sides
a = float(input('Enter first segment (a): '))
b = float(input('Enter second segment (b): '))
c = float(input('Enter third segment (c): '))

# Check if the segments can form a triangle
if a < c + b and b < a + c and c < a + b:
    print(f'\n[ ANALYSIS ]: Segments CAN FORM a triangle!')
    
    # Classification logic
    if a == b == c:
        print('>> Type: EQUILATERAL (Full symmetry detected)')
    elif a != b and a != c and b != c:
        print('>> Type: SCALENE (No matching sides found)')
    else:
        print('>> Type: ISOSCELES (Partial symmetry detected)')
else:
    print('\n[ ANALYSIS ]: Segments CANNOT FORM a triangle!')
    print("System Error: These lines exist in different realities.")
    
print('\n' + '─' * 32)
print('       Analysis Complete.       ')
print('─' * 32)