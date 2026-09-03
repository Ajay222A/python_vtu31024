
N = int(input("Enter no.f sales: "))

sales = {}
order = []

print("Enter sales: ")
for _ in range(N):
    category, item, amount = input().split()
    amount = int(amount)

    if category not in sales:
        sales[category] = {
            "total": 0,
            "max_item": item,
            "max_amount": amount
        }
        order.append(category)
    sales[category]["total"] += amount
    if amount > sales[category]["max_amount"]:
        sales[category]["max_amount"] = amount
        sales[category]["max_item"] = item

for category in order:
    print(category,
          sales[category]["total"],
          sales[category]["max_item"])
