def calculate_cart_total(*prices):
    """Calculate total for any number of items
    Parameters: variable number of price values
    Returns: Total sum of all prices rounded to 2 decimals
    """
    # Check if cart is empty
    if not prices:
        return 0.00
    # sum all prices
    subtotal = sum(prices)
    # round to 2 decimals and return
    return round(subtotal, 2)
print(f"Empty Cart:${calculate_cart_total()}")
print(f"1 Item:${calculate_cart_total(19.99)}")
print(f"3 Item:${calculate_cart_total(19.99, 12.34, 2.99)}")
print(f"4 Item:${calculate_cart_total(19.99, 4.50, 7.99, 8.65)}")

def creat_order(customer_name, **items):
    """Create an order with any menu item"""
    order = {
        "customer": customer_name,
        "items": items,
        "item_count": len(items)
    }
    return order

# Different cusomers, different orders
order1 = creat_order("Alex", pizza = 2, soda = 1, wings = 12)
order2 = creat_order("John", burger = 1, soda = 1, fries = 2, nuggets = 6)
order3 = creat_order("Alice", salad = 1)

print(order1)
print(order2)
print(order3)


# Parameter order is strict
def funtion(required, *args, default=10, **kwargs):
    pass