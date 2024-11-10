class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def main():
    calc = Calculator()

    print("Prosty kalkulator")
    print("Wybierz operację:")
    print("1: Dodawanie")
    print("2: Odejmowanie")
    print("3: Mnożenie")
    print("4: Dzielenie")

    choice = input("Wpisz numer operacji (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Wpisz pierwszą liczbę: "))
            num2 = float(input("Wpisz drugą liczbę: "))

            if choice == '1':
                print("Wynik:", calc.add(num1, num2))
            elif choice == '2':
                print("Wynik:", calc.subtract(num1, num2))
            elif choice == '3':
                print("Wynik:", calc.multiply(num1, num2))
            elif choice == '4':
                print("Wynik:", calc.divide(num1, num2))
        except ValueError:
            print("Wprowadź poprawną liczbę.")
    else:
        print("Nieprawidłowy wybór operacji.")


if __name__ == "__main__":
    main()