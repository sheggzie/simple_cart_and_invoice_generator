# SELF TASK: create a program, where users can order items 
# and get the total price of items ordered,
# also allow implementation of discount and invoice generation.

class Cart:
    def __init__(self):        
        self.products = []
        self.prices = []

    def shop(self):
        self.items = {
            "burger": 50,
            "milk": 30,
            "water": 10,
            "sugar": 20,
            "garri": 100
        }        

        self.name = input("please enter a name: ").upper()
        print("HELLO " + self.name + ", WELCOME TO SAPA MARKET!")
        print("kindly check the available items in the store below!")
        print(self.items)
    
    def add_to_cart(self):
        for self.pick in self.items.items():
            self.x = input("type the name of the item you would like to add to cart: ").lower()
            self.pick = self.x
            
            if self.pick in self.items:
                self.prices.append(self.items[self.x])
                self.products.append(self.pick)
            else:
                print(f"sorry, item {self.x} is not available")

    def count_products(self):
        print(f"you have added {len(self.products)} item(s) to cart.")
    
    def apply_discount(self):
        coupon_code = input("Do you have a coupon code?: ").lower()

        if coupon_code == "yes":
            prices = sum(self.prices)
            self.discount = prices * 50/100
            prices -= self.discount
            self.checkout_price = self.discount
            print("congrats! you have a 50% discount offer")
        else:
            self.discount = 0
            self.checkout_price = sum(self.prices)
            print("sorry, you have entered an incorrect coupon code!")

    def generate_invoice(self):
        print("." * 30)
        print("." * 30)
        print("Generating Invoice, please hold on a sec...")
        print("." * 30)
        print("." * 30)
        print("." * 30)
        print("-" * 30)

        #FIRST METHOD IMPLEMENTED: THE WHILE LOOP
        # a = 0
        # while a <= len(self.products) - 1:
        #     print(f"{self.prices[a]:<15}{self.products[a]:>15}")
        #     a += 1

        #OR

        # SECOND METHOD IMPLEMENTED: THE ZIP METHOD - (SHORTER AND BETTER)
        for price, item in zip(self.prices, self.products):
            print(f"{item:<15}{price:>15}")
        print("-" * 30)
        print(f"{'CHECKOUT TOTAL:':<15}{int(self.checkout_price):>15}")
        print("-" * 30)

def run():
    a = Cart()
    a.shop()
    a.add_to_cart()
    a.apply_discount()
    a.count_products()
    a.generate_invoice()
run()