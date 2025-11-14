print("----- Expense Tracker -----")


food = float(input("Enter food expenses: "))
travel = float(input("Enter travel expenses: "))
shopping = float(input("Enter shopping expenses: "))
others = float(input("Enter other expenses: "))


total = food + travel + shopping + others


budget = float(input("Enter your monthly budget: "))

print("\n----- Expense Summary -----")
print("Total Expenses:", total)
print("Monthly Budget:", budget)


if total > budget:
    print(" You have exceeded your budget!")
elif total == budget:
    print(" You have exactly reached your budget.")
else:
    print(" You are within the budget.")
