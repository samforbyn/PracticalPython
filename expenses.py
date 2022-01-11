# expenses = [10.50, 8,5 ,15 ,20, 5, 3]
# sum = 0
# for x in expenses:
#     sum = sum + x

# total = sum(expenses)
# print(f"You spent ${total}")

# adding input / range

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:\n"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:\n")))
total = sum(expenses)
print(f"You spent ${total} this week")