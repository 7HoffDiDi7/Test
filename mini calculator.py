def Arithmetics(a, z, b):
    if z == "+":
        return (a + b)
    elif z == "-":
        return (a - b)
    elif z == "*":
        return (a * b)
    elif a == "/":
        return (a / b)
    else:
        print("Неизвестная операция!")

print("Это мини калькулятор, который умеет слогать(+), вычитать(-), умножать(*) и делить(/)\n")
while True:
    A, Z, B = input("Введите первое число, затем арифметическое действие из доступных, через пробел, и второе число: ").split()
    A = float(A)
    B = float(B)
    Deystvie = Arithmetics(A, Z, B)
    print(Deystvie)
