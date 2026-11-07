def process_order(order):
    try:
        item = order["item"]
        price = order["price"]

    except KeyError:
        print("Error: Required order key is missing")

    else:
        print("Order Details:")
        print("Item:", item)
        print("Price:", price)

    finally:
        print("Processing complete")


# Test program
order1 = {
    "item": "computer",
    "price": 50000
}

process_order(order1)
print()

order2 = {
    "item": "Mobile"
}

process_order(order2)