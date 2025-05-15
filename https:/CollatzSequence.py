print("Sanio Frederic,1AY24AI099,SEC-O")
def collatz_sequence(n):
    while n != 1:
        print(n, end=' -> ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

def main():
    print("Collatz Sequence Generator")
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a number greater than zero.")
        else:
            collatz_sequence(num)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
