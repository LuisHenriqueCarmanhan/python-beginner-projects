print('-=' * 15)
print('   TRAVEL COST CALCULATOR   ')
print('-=' * 15)

dist = float(input('What is the distance of your trip in Km?'))
print(f'You are about to start a trip of {dist}Km.')

# Logic: R$ 0.50 per Km for trips up to 200Km, and R$ 0.45 for longer trips
if dist <= 200:
    price = dist * 0.5
else:
    price = dist * 0.45

print(f'And the price of your ticket will be R$ {price:.2f}')
print('--- Have a safe trip! ---')