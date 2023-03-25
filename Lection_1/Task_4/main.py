a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + (discriminant)**0.5) / (2*a)
    x2 = (-b - (discriminant)**0.5) / (2*a)
    result = f"two roots: {x1} and {x2}"
elif discriminant == 0:
    x = -b / (2*a)
    result = f"one root: {x}"
else:
    result = f"no real roots"
print(f"The equation has {result}.")