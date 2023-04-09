def count_elements():
    n = int(input("Enter elements count: "))
    elements = []
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        elements.append(element)

    find_element = input("Enter an element to count its quantity: ")
    result = elements.count(find_element)
    print(f"Count of elements `{find_element}`: {result}")

count_elements()