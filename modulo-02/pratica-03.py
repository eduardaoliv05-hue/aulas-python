temp = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (temp * 9/5) + 32
kelvin = temp + 273.15
print (f"{temp} = {fahrenheit: .1f}°F")
print (f"{temp} = {kelvin: .2f}K")