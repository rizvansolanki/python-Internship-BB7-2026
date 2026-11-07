usernames = ["tahir", "rizvan", "sahilmahida", "joni", "yahya"]

result = list(filter(lambda name: len(name) >= 6, usernames))

print("Valid Usernames:", result)
