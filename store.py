from products import Product

class Store:
    def __init__(self, products: list[Product]):
        self.products = products


    def add_product(self, product: Product) -> None:
        self.products.append(product)


    def remove_product(self, product: Product) -> None:
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)


    def get_all_products(self) -> list[Product]:
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list) -> float:
       total_price = 0
       if len(shopping_list) == 0:
           raise ValueError("basket empty")
       for product, quantity in shopping_list:
            total_price += product.buy(quantity)
       return total_price


def make_order(store_instance: Store):
    all_products = [p for p in store_instance.get_all_products() if p.is_active()]
    shopping_list = []
    print("------")
    for i, product in enumerate(all_products, start=1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("------")

    while True:
        product_input = input("When you want to finish order, enter empty text.\nWhich product # do you want? ")
        if product_input == "":
            break
        try:
            product_index = int(product_input) - 1
            amount = int(input("What amount do you want? "))
            shopping_list.append((all_products[product_index], amount))
            print("Product added to list!\n")
        except (ValueError, IndexError):
            print("Invalid input, try again.")

    try:
        total = store_instance.order(shopping_list)
        print(f"Order complete! Total price: ${total}")
    except Exception as e:
        print(f"Order failed: {e}")
