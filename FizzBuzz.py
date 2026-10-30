# FizzBuzz: de 1 a 50, mostra "Fizz" nos múltiplos de 3,
# "Buzz" nos múltiplos de 5 e "FizzBuzz" nos múltiplos de ambos

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)