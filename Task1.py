print("=====================================    Fibonaaci Series    =====================================")
print("==================================================================== By: Tarun Singh Chauhan  ====")
print("This program will print the fibonacci series upto the number of terms you want.")

def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

n = int(input("Enter the number of terms: "))
fibonacci(n)

for i in range(0, 1):
    print("Fibonacci series printed successfully.")     

while True:
    command = input("Do you want to print the Fibonacci series again? (yes/no): ")
    if command == "yes":
        n = int(input("Enter the number of terms: "))
        fibonacci(n)
        for i in range(0, 1):
            print("Fibonacci series printed successfully.")
    elif command == "no":
        print("Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")                                                                                     