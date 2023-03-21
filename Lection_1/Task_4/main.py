a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + (discriminant)**0.5) / (2*a)
    x2 = (-b - (discriminant)**0.5) / (2*a)
    print(f"The equation has two roots: {x1} and {x2}")
elif discriminant == 0:
    x = -b / (2*a)
    print(f"The equation has one root: {x}")
else:
    print("The equation has no real roots.")