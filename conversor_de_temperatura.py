# Conversor de temperatura entre Celsius e Fahrenheit

print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C = {fahrenheit:.1f}°F")
elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius:.1f}°C")
else:
    print("Opção inválida.")