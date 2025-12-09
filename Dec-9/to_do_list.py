Todo_List = {
    "Workout" : "Pending",
    "Eating" : "Done"
}
while True:
    print("\n--TODO LIST--")
    print("1. Create/Add Task")
    print("2. Show all task")
    print("3. update the task")
    print("4. Exit")
    choice = input("Enter todo list number 1-4: ")
    if choice == "4":
        print("Goodbye!")
        break
    elif choice == "1":
        task_name = input("Enter a Task: ")
        Todo_List[task_name] = "Pending"
        print(f"Added {task_name}!")
    elif choice == "2":
        print("\n--- Current Tasks ---")
        for key,value in Todo_List.items():
            print(f"{key}:{value}")
    elif choice == "3":
        name = input("Which task is done? ")
        Todo_List[name] = "Done"
        if __name__ in Todo_List:
            Todo_List[name] = "Done"
            print(f"Great job! {name} is marked Done.")
        else:
            print(f"Task not found! Check spelling")
        