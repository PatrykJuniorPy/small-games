if __name__ == '__main__':
    pass

expenses = []


def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')


def add_expense(month):
    print()
    expense_amount = int(input("enter the amount [zł]: "))
    expense_type = input("enter type: (food, entertainment, home, other): ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amount_this_month = sum(
        expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    average_expense_this_month = total_amount_this_month / number_of_expenses_this_month

    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    average_expense_all = total_amount_all / len(expenses)

    print()
    print("stats")
    print("total amount this month [zł]: ", total_amount_this_month)
    print("average expense this month [zł]: ", average_expense_this_month)
    print("total amount [zł]: ", total_amount_all)
    print("average expense [zł]: ", average_expense_all)


while True:
    print()
    month = int(input("choose month [1-12]: "))

    if month == 0:
        break

    while True:
        print()
        print("0. back to month choose")
        print("1. display expenses")
        print("2. add expenditure")
        print("3. stats")
        choice = int(input("choose option: "))

        if choice == 0:
            break

        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)

        if choice == 3:
            show_stats(month)
