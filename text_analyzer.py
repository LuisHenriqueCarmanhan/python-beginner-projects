# Read the full name and remove leading/trailing spaces
full_name =  str(input('Enter your full name: ')).strip()

print(f'Uppercase: {full_name.upper()}')
print(f'Lowercase: {full_name.lower()}')

# Total letters without counting internal spaces
total_letters = len(full_name) - full_name.count(' ')
print(f'total letters (no spaces): {total_letters}')

# Length of the first name using split
first_name = full_name.split()[0]
print(f'our first name is {first_name} and it has {len(first_name)} letters')