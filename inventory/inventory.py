class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price          # Encapsulated
        self.__quantity = quantity    # Encapsulated

    def get_details(self):
        return f"{self.name} - ₹{self.__price} - Stock: {self.__quantity}"

    def purchase(self, amount):
        if amount <= self.__quantity:
            self.__quantity -= amount
            return self.__price * amount
        else:
            return -1  # Not enough stock

    def get_stock(self):
        return self.__quantity

    def get_price(self):
        return self.__price


class Inventory:
    def __init__(self):
        self.__products = []          # Encapsulated
        self.__earnings = 0.0         # Encapsulated

    def add_product(self, name, price, quantity):
        self.__products.append(Product(name, price, quantity))

    def purchase_product(self, name, quantity):
        for product in self.__products:
            if product.name == name:
                cost = product.purchase(quantity)
                if cost != -1:
                    self.__earnings += cost
                    print(f"✅ Purchased {quantity} x {name} for ₹{cost}")
                else:
                    print("❌ Not enough stock.")
                return
        print("❌ Product not found.")

    def show_stock(self):
        print("\n📦 Available Stock:")
        for product in self.__products:
            print("-", product.get_details())

    def show_earnings(self):
        print(f"\n💰 Total Earnings: ₹{self.__earnings}")
