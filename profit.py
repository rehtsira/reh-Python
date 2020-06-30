import sys
def profit():
    cost = sys.argv[1]
    sell = sys.argv[2]
    inventory = sys.argv[3]
    total_sales = float(cost) * float(inventory)
    total_cost = float(sell) * float(inventory)
    profit = total_cost - total_sales
    print("Your profit is $ {:0.2f}".format(profit))
profit()
