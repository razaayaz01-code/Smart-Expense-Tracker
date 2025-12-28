import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import os

FILE_NAME = "expenses.csv"

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    today = date.today()

    df = pd.DataFrame([[today, category, amount, description]],
                      columns=["date", "category", "amount", "description"])

    if not os.path.exists(FILE_NAME):
        df.to_csv(FILE_NAME, index=False)
    else:
        df.to_csv(FILE_NAME, mode='a', header=False, index=False)

    print("✅ Expense added")

def view_total():
    if not os.path.exists(FILE_NAME):
        print("No data found")
        return
    df = pd.read_csv(FILE_NAME)
    print("Total Expense:", df["amount"].sum())

def category_analysis():
    df = pd.read_csv(FILE_NAME)
    print("\nCategory-wise Expense:")
    print(df.groupby("category")["amount"].sum())

def budget_check():
    budget = float(input("Enter monthly budget: "))
    df = pd.read_csv(FILE_NAME)
    total = df["amount"].sum()

    if total > budget:
        print("⚠ Budget Exceeded!")
    else:
        print("✅ You are within the budget")

def show_chart():
    df = pd.read_csv(FILE_NAME)
    df.groupby("category")["amount"].sum().plot(
        kind="pie", autopct="%1.1f%%"
    )
    plt.title("Expense Distribution")
    plt.ylabel("")
    plt.show()


def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Total Expense")
        print("3. Category-wise Analysis")
        print("4. Budget Check")
        print("5. Show Expense Chart")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            category_analysis()
        elif choice == "4":
            budget_check()
        elif choice == "5":
            show_chart()
        else:
            break

main()
