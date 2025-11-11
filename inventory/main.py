from inventory import Inventory

def main():
    store = Inventory()

    while True:
        print("\n🛒 Inventory Management System")
        print("1. Add Product")
        print("2. Purchase Product")
        print("3. Show Stock")
        print("4. Show Earnings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Product Name: ")
            price = float(input("Price (₹): "))
            quantity = int(input("Quantity: "))
            store.add_product(name, price, quantity)

        elif choice == "2":
            name = input("Product Name: ")
            quantity = int(input("Quantity to Purchase: "))
            store.purchase_product(name, quantity)

        elif choice == "3":
            store.show_stock()

        elif choice == "4":
            store.show_earnings()

        elif choice == "5":
            print("👋 Exiting system. Thank you!")
            break

        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
