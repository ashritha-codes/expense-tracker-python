print("====EXPENSE TRACKER====")

expenses = []

while True:
    print("1. Add Expenses")
    print("2. Search Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    option = input("Enter your option: ")

    if option == "1":
        expense = input("Enter Expense: ")
        amount = int(input("Enter Amount: "))
        category = input("Enter Category: ")
        Date = input("Enter Date: ")

        expenses.append([expense, amount, category, Date])
        print("Expense Added Successfully!")

    elif option == "2":
        search = input("Enter Expense name: ")
        found = False

        for item in expenses:
            if search.lower() in item[0].lower():
                print("Expense Found!")
                print(item)
                found = True

        if found == False:
            print("Expense not found")

    elif option == "3":
        total = 0

        for item in expenses:
            total = total + item[1]

        print("Total expenses:", total)

    elif option == "4":
        print("Program Ended")
        break

    else:
        print("Invalid option")