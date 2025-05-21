import csv
goods = {}
print("IMPORT AND EXPORT\n")
class Shop:
    def owner():
        global goods
        print("\n1. Create Inventory\n2. Update Inventory\n3. Delete Item\n4. Display Inventory")
        choice = int(input("Enter your choice: "))
        if choice == 1:  
            n = int(input("Enter number of goods: "))
            for i in range(n):
                item = input("Item: ")
                quantity = int(input("Quantity: "))
                price = float(input("Price per unit: "))
                goods[item] = {"quantity": quantity, "price": price}
            with open("import.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Item", "Quantity", "Price"])
                for key, value in goods.items():
                    writer.writerow([key, value["quantity"], value["price"]])
            print("Inventory stored in import.csv.")
        elif choice == 2: 
            item = input("Enter item name to update: ")
            if item in goods:
                quantity = int(input("New Quantity: "))
                price = float(input("New Price: "))
                goods[item] = {"quantity": quantity, "price": price}
            else:
                print("Item not found!")
        elif choice == 3:  
            item = input("Enter item name to delete: ")
            if item in goods:
                del goods[item]
                print(f"{item} removed from inventory.")
            else:
                print("Item not found!")
        elif choice == 4:  
            with open("import.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
def dealer():
    print("\nDealer entering items to warehouse:")
    n = int(input("Enter number of goods to store: "))
    for i in range(n):
        item = input("Item: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price per unit: "))
        goods[item] = {"quantity": quantity, "price": price}
    with open("import.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Quantity", "Price"])
        for key, value in goods.items():
            writer.writerow([key, value["quantity"], value["price"]])
    print("Dealer has updated import.csv with stored items.")
def customer():
    global goods
    customer_name = input("Enter customer name: ")
    print("\nAvailable Goods:")
    for item, details in goods.items():
        print(f"{item}: {details['quantity']} units, ₹{details['price']} per unit")

    print("\nEnter customer needs:")
    m = int(input("Enter number of items customer needs: "))
    customer_needs = {}
    for i in range(m):
        item = input(f"Enter Item {i+1}: ")
        quantity = int(input(f"Quantity {i+1}: "))
        if item in goods and goods[item]["quantity"] >= quantity:
            customer_needs[item] = quantity
        else:
            print(f"Error: {item} is not available in storage or insufficient quantity.")
    exported_items = []
    total_cost = 0
    for item, quantity in customer_needs.items():
        price = goods[item]["price"]
        total_cost += price * quantity
        goods[item]["quantity"] -= quantity
        exported_items.append([item, quantity, price, price * quantity])
    with open("export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Quantity Sold", "Price per unit", "Total Price"])
        writer.writerows(exported_items)
    print("Items are delivered")
    with open("billing.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Customer Name", "Item", "Quantity", "Price per unit", "Total Price"])
        for item, quantity, price, total_price in exported_items:  
            writer.writerow([customer_name, item, quantity, price, total_price])
        writer.writerow(["", "", "", "Total Amount", total_cost])
    print("Bill generated")
if __name__ == "__main__":
    while True:
        print("\n1. Owner\n2. Dealer\n3. Customer\n4. Exit")
        choice = int(input("Choose role: "))

        if choice == 1:
            Shop.owner()
        elif choice == 2:
            dealer()
        elif choice == 3:
            customer_needs = customer()
        elif choice == 4:
            break