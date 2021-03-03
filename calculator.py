class Calculator:

    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


def main():
    calculator = Calculator(input('a'), input('b'))
    operation = input(' ')
    if operation == '+':
        y = calculator.addition()
        print(y)
    elif operation == '-':
        y = calculator.subtraction()
    elif operation == '/':
        y = calculator.division()
    elif operation == '*':
        y = calculator.multiplication()
        print(y)


main()

