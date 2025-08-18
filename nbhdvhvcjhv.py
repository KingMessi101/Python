x = int(input("Enter the base (x): "))
n = int(input("Enter the number of terms (n): "))

print(f"\nPower series up to {n} terms:")

for i in range(n):
    print(f"{x}^{i} = {x**i}")