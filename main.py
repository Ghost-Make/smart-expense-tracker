import csv

from expense import Expense

#import expense
from utils import save_expense
from report import category_summary
from utils import search_expense
from utils import delete_expense

def show_menu():
    print("\n1. Add Expense")
    print("2. View Expense")
    print("3. Exit")
    print("4. category summary")
    print("5. Search Expemse")
    print("6. Delete Expense")

def main():
    print("Welcome to Smart Expense Tracker")

    while True:
        show_menu()
        choice = input("Enter Your Choice: ")
            
        if choice == "1":
            try:
                amount = float(input("Enter Amount: "))
            except ValueError:
                print("Invalid Amount")
                continue
            category = input("Enter Category: ")
            description = input("Enter Description: ")
            expense = Expense(amount, category, description)
            save_expense(expense)
            print("Expense saved Successfully")

            print("Expense Added")
            print(expense.date, expense.amount, expense.category, expense.description)

            
             #expense = Expense(amount, category, description)
        elif choice == "2":
            with open("data.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        elif choice == "3":
            print("Exiting the application.")
            break
        elif choice == "4":
            category_summary()
        elif choice == "5":
            category_name = input("Enter category to search: ")
            search_expense(category_name)
        elif choice == "6":
            description = input("Enter description to delete: ")
            delete_expense(description)

        #category = input("Enter Category: ")
        #description = input("Enter Description: ")

        #expense = Expense(amount, category, description)

        #save_expense(expense)
        #print("Expense saved Successfully")

        #print("Expense Added")
        #print(expense.date, expense.amount, expense.category, expense.description)
        #hello

main()