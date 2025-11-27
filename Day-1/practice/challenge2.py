# The "Sum of Evens" (logic + accumulator)
N = int(input("Enter a number: "))
total = 0
for i in range(1,N+1):
    if i%2 == 0:
        total += i
        print(f"{i}")