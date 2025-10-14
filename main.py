def calculation(op: str, a: float, b: float):
    match op:
        case "+":
            return f"Результат сложения = {value_1 + value_2}"
        case "-":
            return f"Результат вычитания = {value_1 - value_2}"
        case "*":
            return f"Результат умножения = {value_1 * value_2}"
        case "/":
            return f"Результат деления = {value_1 / value_2}"
    return None

operation = input("Выберите действие (+, -, *, /): ")

if operation == "+" or operation == "-" or operation == "*" or operation == "/":
    try:
        value_1 = float(input("Введите первое число: "))
        value_2 = float(input("Введите второе число: "))
        result = calculation(operation, value_1, value_2)
    except ValueError:
        print("Введено не корректное значение")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        print(result)
else:
    print("Ввдено некорректная операция")
