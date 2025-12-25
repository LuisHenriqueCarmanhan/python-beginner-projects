full_name = str(input('Enter your full name: ')).strip()
names = full_name.split()

print('Nice to meet you!')
print(f'Your fist name is {names[0]}')
print(f'Your last name is {names[-1]}')
