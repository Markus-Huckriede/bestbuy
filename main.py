import products
import store

def start(store_instance: store.Store):
    while True:
        print("Store Menu")
        print()
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number (1-4): ")

        if choice == "1":
            all_products = store_instance.get_all_products()
            for index, product in enumerate(all_products, start=1):
                print(f"{index}. {product.show()}")
        elif choice == "2":
            print(f"Total quantity in store: {store_instance.get_total_quantity()}")
        elif choice == "3":
            store.make_order(store_instance)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()
