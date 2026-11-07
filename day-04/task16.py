def access_element(my_list, index):

    try:
        return my_list[index]

    except IndexError:
        return None


numbers = [10, 20, 30, 40, 50]

print(access_element(numbers, 2))
print(access_element(numbers, 10))