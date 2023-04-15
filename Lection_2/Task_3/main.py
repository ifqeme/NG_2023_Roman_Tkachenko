print("Hello! Enter three sets of elements:")

set1 = set(input(">>> first set: ").split())
set2 = set(input(">>> second set: ").split())
set3 = set(input(">>> third set: ").split())

result = set()

for element in set1:
    if element in set2 or element in set3:
        result.add(element)

for element in set2:
    if element in set1 or element in set3:
        result.add(element)

for element in set3:
    if element in set1 or element in set2:
        result.add(element)

print(f"Set of non-unique elements: {result}")