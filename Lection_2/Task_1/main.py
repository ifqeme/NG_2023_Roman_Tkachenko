def count_elements():
    elements_count = int(input("Enter elements count: "))
    elements = []
    for index in range(elements_count):
        element = input(f"Enter element {index+1}: ")
        elements.append(element)

    find_element = input("Enter an element to count its quantity: ")
    result = elements.count(find_element)
    print(f"Count of elements `{find_element}`: {result}")

count_elements()