def is_disarium(num):
    num_str = str(num)
    total = 0
    for i in range(len(num_str)):
        digit = int(num_str[i])
        total += digit ** (i + 1)
    return total == num

def main():
    number = int(input("Enter a number: "))
    if is_disarium(number):
        print(f"{number} is a Disarium number.")
    else:
        print(f"{number} is not a Disarium number.")
main()