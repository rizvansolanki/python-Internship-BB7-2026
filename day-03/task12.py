subscribers = {
    "rizvan@gmail.com",
    "samad@gmail.com",
    "sahil@gmail.com",
    "arif@gmail.com"
}

customers = {
    "tahir@gmail.com",
    "raju@gmail.com",
    "yahya@gmail.com",
    "mahir@gmail.com"
}

# Subscribers who never made a purchase
not_purchased = subscribers - customers

# Customers who never subscribed
not_subscribed = customers - subscribers

print("Subscribers who never purchased:")
print(not_purchased)

print("\nCustomers who never subscribed:")
print(not_subscribed)