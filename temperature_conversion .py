# this is a program for Temperature conversion: 
# Between Celsius and Kelvin, Between Fahrenheit and Kelvin, and
# Between Celsius and Fahrenheit.

# Here are the temperature conversion formulas: 
# Celsius to Kelvin: K = C + 273.15 
# Kelvin to Celcius: C = K - 273.15
# Fahrenheit to Celcius: C = (F-32) (5/9)
# Celsius to Fahrenheit: F = C(9/5) + 32
# Fahrenheit to Kelvin: K = (F-32) (5/9) + 273.15 
# Kelvin to Fahrenheit: F = (K-273.15) (9/5) + 32

print("This a program to conversion the value of temperature from one unit to another. There can be three main conversions of temperature which are possible: \n Between Celsius and Kelvin, Between Fahrenheit and Kelvin, and Between Celsius and Fahrenheit.")

while True:
    from_unit = input("Enter the unit you want conversion from (C for Celsius, F for Fahrenheit, and k for Kelvin) or type Q or q to quit:")
    
    if from_unit.lower() == 'q':
        break

    if from_unit not in 'CFK':
        print("That is not a valid unit!")
        continue

    temp = float(input("Enter the temperature: "))
    to_unit = input("Enter the unit you want to conversion to (C for Celsius, F for Fahrenheit, and k for Kelvin): ")

    if to_unit not in 'CFK':
        print("That is not a valid unit!")
        continue

    if from_unit == 'C' and to_unit == 'C': # in case the user Enter the same unit
        print(f'{temp} °C')
    elif from_unit =='F' and to_unit == 'F':
        print(f'{temp}°F')
    elif from_unit =='K' and to_unit == 'K':
        print(f'{temp} K')
    elif from_unit =='C' and to_unit == 'F':
        new_temp = temp * (9/5) + 32
        round_temp = round(new_temp,3)
        print(f'{round_temp} °F')
    elif from_unit =='C' and to_unit == 'K':
        new_temp = temp + 273.15
        round_temp = round(new_temp,3)
        print(f'{round_temp} K')
    elif from_unit =='F' and to_unit == 'C':
        new_temp = (temp - 32) * 5/9
        round_temp = round(new_temp,3)
        print(f'{round_temp} °C') 
    elif from_unit =='F' and to_unit == 'K':
        new_temp = (temp - 32)*(5/9) + 273.15
        round_temp = round(new_temp,3)
        print(f'{round_temp} K')
    elif from_unit =='K' and to_unit == 'C':
        new_temp = temp - 273.15
        round_temp = round(new_temp,3)
        print(f'{round_temp} °C')
    elif from_unit =='K' and to_unit == 'F':
        new_temp = (temp - 273.15)*(9/5) + 32
        round_temp = round(new_temp,3)
        print(f'{round_temp} °F')

print('Have a good day')        



        

