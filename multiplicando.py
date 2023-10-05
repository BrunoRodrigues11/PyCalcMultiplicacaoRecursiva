def multiplica(num1, num2):
    if (num1 == 0) or (num2 == 0):
        return 0
    elif (num2 == 1):
        return num1
    else:
        return num1 + multiplica(num1, num2 - 1)


x = int(input("Informe um número: "))
y = int(input("Informe mais um número: "))
result = multiplica(x, y)
print(result)
