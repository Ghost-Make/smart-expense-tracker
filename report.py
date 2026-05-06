import csv

def category_summary():
    categories = {}
    
    with open("data.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            category = row[2]
            amount = float(row[1])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
    
    print("category_summery")

    for category, total in categories.items():
        print(category, "=", total)


