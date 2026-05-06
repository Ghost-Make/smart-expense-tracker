import csv
def save_expense(expense):
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense.date, expense.amount, expense.category, expense.description])

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_expense(category_name):
    with open("data.csv", "r") as file:
        reader = csv.reader(file)

        found = False

        for row in reader:
            if row[2].lower() == category_name.lower():
                print(row)
                found = True

            if not found:
                print("No matching category found")


def delete_expense(description):
    rows = []

    with open("data.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[3] != description:
                rows.append(row)

    with open("data.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Expense deleted if match not found")