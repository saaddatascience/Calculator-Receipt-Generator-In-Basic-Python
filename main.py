# Simple Python program to calculate the total sum of prices entered by the user
# The program continues to accept inputs until the user presses "q" to quit.

items = []
total_sum = 0

while True:
    # Collect item details
    item_name = input("Enter the item name (or 'q' to quit): ")
    
    if item_name.lower() == "q":
        break

    try:
        # Collect item price
        item_price = float(input(f"Enter the price for {item_name}: "))
        # Collect item quantity (optional)
        item_quantity = int(input(f"Enter the quantity for {item_name}: "))

        # Calculate the total for this item (price * quantity)
        item_total = item_price * item_quantity
        
        # Store item details
        items.append({
            'name': item_name,
            'price': item_price,
            'quantity': item_quantity,
            'total': item_total
        })
        
        # Add to overall total
        total_sum += item_total
    except ValueError:
        print("Please enter valid price and quantity.")

# Display the bill summary
print("\n--- Bill Summary ---")
for item in items:
    print(f"{item['quantity']}x {item['name']} @ {item['price']} each = {item['total']:.2f}")
print("---------------------")
print(f"Total: {total_sum:.2f}")