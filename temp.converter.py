
unit = input('is this temperature in celsius or fahrenheit (C/F): ')
temp = input('enter the temperature: ')

if unit == 'C':
   temp = round(9 * float(temp) / 5 + 32, 1)
   print(f'your provided temperature is {temp} Fahrenheit ')
elif unit == 'F':
    temp = round(5 * float(temp) / 9 - 32, 2)
    print(f'your provided temperature is {temp} Celsius ')
else :
    print(f'{unit} ix invalid unit, please enter valid one')