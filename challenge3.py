# "FizzBuzz" (The Interview Classic)
for i in range(1,21):
    if i%3==0 and i%5==0:
        print(f"{i} is FizzBuzz")
    elif i%5==0:
        print(f"{i} is Buzz")
    elif i%3==0:
        print(f"{i} is Fizz")
    else:
        print(f"{i} is numb")