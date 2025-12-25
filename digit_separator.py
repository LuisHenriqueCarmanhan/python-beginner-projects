# Read a number as string to make it easier to iterate
num = input('Enter a number from 0 to 9999: ').zfill(4)
# zfill ensures it has 4 digits

print(f'Units: {num[3]}')
print(f'Tens: {num[2]}')
print(f'Hundreds: {num[1]}')
print(f'Thousands: {num[0]}')