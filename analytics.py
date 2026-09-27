# analytics.py

customers_served = 0
total_revenue = 0

burger_count = 0
pizza_count = 0
pasta_count = 0
coke_count = 0
icecream_count = 0


def daily_report():

    print("\n")
    print("=" * 40)
    print("        DAILY REPORT")
    print("=" * 40)

    print("Customers Served :", customers_served)

    print("Total Revenue : ₹", round(total_revenue, 2))

    print("\nItems Sold")

    print("Burger     :", burger_count)
    print("Pizza      :", pizza_count)
    print("Pasta      :", pasta_count)
    print("Coke       :", coke_count)
    print("Ice Cream  :", icecream_count)

    print("=" * 40)
