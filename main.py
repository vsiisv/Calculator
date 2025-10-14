def calculation(op: str, a, b):
    match op:
        case "+":
            return f"Результат сложения = {a + b}"
        case "-":
            return f"Результат вычитания = {a - b}"
        case "*":
            return f"Результат умножения = {a * b}"
        case "/":
            try:
                return f"Результат деления = {a / b}"
            except ZeroDivisionError:
                return  "На ноль делить нельзя"
    return None

def get_operator():
    operator = input("Выберите действие (+, -, *, /): ")
    while operator not in ["+", "-", "*", "/"]:
        print("Введен некорректный оператор. Попробуйте еще раз.")
        operator = input("Выберите действие (+, -, *, /): ")
    return operator

def get_value(message):
    while True:
        value = input(message)
        try:
            value = float(value)
            return value
        except ValueError:
            print("Введите числовое значение.")

def main():
    operator = get_operator()
    value_1 = get_value("Введите первое число: ")
    value_2 = get_value("Введите второе число: ")
    result = calculation(operator, value_1, value_2)
    print(result)

main()