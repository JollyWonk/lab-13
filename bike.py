class Bike:
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.color}, ${self.price}"

bikes = []

def add_bike(brand, model, year, color, price):
    bike = Bike(brand, model, year, color, price)
    bikes.append(bike)
    print(f"Велосипед '{bike.model}' додано до списку.")

def remove_bike(model):
    global bikes
    for bike in bikes:
        if bike.model == model:
            bikes.remove(bike)
            print(f"Велосипед '{model}' видалено з списку.")
            return
    print(f"Велосипед '{model}' не знайдено.")

def find_bikes_by_color(color):
    found_bikes = [bike for bike in bikes if bike.color == color]
    if found_bikes:
        print(f"Велосипеди з кольором '{color}':")
        for bike in found_bikes:
            print(bike)
    else:
        print(f"Велосипедів з кольором '{color}' не знайдено.")

def display_menu():
    print("\nМеню:")
    print("1. Додати велосипед")
    print("2. Видалити велосипед")
    print("3. Знайти велосипеди за кольором")
    print("4. Вивести список велосипедів")
    print("5. Вийти")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Виберіть опцію (1-5): ")

        if choice == '1':
            brand = input("Введіть бренд: ")
            model = input("Введіть модель: ")
            year = int(input("Введіть рік: "))
            color = input("Введіть колір: ")
            price = float(input("Введіть ціну: "))
            add_bike(brand, model, year, color, price)

        elif choice == '2':
            model = input("Введіть модель велосипеда для видалення: ")
            remove_bike(model)

        elif choice == '3':
            color = input("Введіть колір для пошуку: ")
            find_bikes_by_color(color)

        elif choice == '4':
            print("\nСписок велосипедів:")
            for bike in bikes:
                print(bike)

        elif choice == '5':
            print("Вихід з програми.")
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")
