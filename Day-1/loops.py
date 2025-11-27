# print("--- Loop 1: Simple ---")
# for i in range(5):
#     print(i)
# print("--- Loop 2: Start & Stop ---")
# for i in range(1,6):
#     print(i)

# Message: I will crack GenAI
# Count: 3
# 1. I will crack GenAI
# 2. I will crack GenAI
# 3. I will crack GenAI
# for i in range(1,4):
#     print(f"{i}. I will crack GenAI")

#make dynamic
message = input("What is the message: ")
count = int(input("How many times you want: "))
for i in range(1, count+1):
    print(f"{i}. {message}")