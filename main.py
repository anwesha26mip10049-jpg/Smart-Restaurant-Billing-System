# Smart Restaurant Billing System

menu={
    1: ("Burger", 80),
    2: ("Pizza", 150),
    3: ("Pasta", 120),
    4: ("Coke", 40),
    5: ("Ice Cream", 60)
}

customer_name=input("Enter Customer Name: ")

total_bill=0
order_list=[]

more="y"

while more.lower()=="y":

    print("\n===== MENU =====")

    for key in menu:
        print(key, ".", menu[key][0], "- ₹", menu[key][1])

    choice=int(input("\nEnter item number: "))
    qty=int(input("Enter quantity: "))

    if choice in menu:

        item_name=menu[choice][0]
        price=menu[choice][1]

        item_total=price * qty

        total_bill+=item_total

        order_list.append([item_name, qty, item_total])

        print(item_name, "added successfully!")

    else:
        print("Invalid Choice")

    more=input("\nDo you want to order more? (y/n): ")

# Discount
discount=0

if total_bill>=500:
    discount=total_bill * 0.10

bill_after_discount=total_bill - discount

# GST
gst=bill_after_discount * 0.05

final_bill=bill_after_discount + gst

# Print Bill

print("\n")
print("=" * 35)
print("      RESTAURANT BILL")
print("=" * 35)

print("Customer :", customer_name)

print("\nItems Ordered:")

for item in order_list:
    print(item[0], "x", item[1], "= ₹", item[2])

print("\nSubtotal : ₹", total_bill)
print("Discount : ₹", discount)
print("GST (5%) : ₹", round(gst, 2))
print("Final Bill : ₹", round(final_bill, 2))

print("\nThank You For Visiting!")
print("\nCome again😊!")
print("=" * 35)


from billing import (
    take_order,
    calculate_bill,
    print_bill
)

import analytics


while True:

    print("\n")
    print("=" * 40)
    print(" SMART RESTAURANT SYSTEM ")
    print("=" * 40)

    print("1. New Customer")
    print("2. Daily Report")
    print("3. Exit")

    choice=input("\nEnter Choice: ")

    if choice=="1":

        customer_name=input(
            "\nEnter Customer Name: "
        )

        order_list, total_bill=take_order()

        discount, gst, final_bill=calculate_bill(
            total_bill
        )

        print_bill(
            customer_name,
            order_list,
            total_bill,
            discount,
            gst,
            final_bill
        )

        analytics.customers_served+=1

        analytics.total_revenue += final_bill

    elif choice=="2":

        analytics.daily_report()

    elif choice=="3":

        print("\nThank You!")
        break

    else:

        print("Invalid Choice")


from billing import (
    take_order,
    calculate_bill,
    print_bill
)

import analytics


while True:

    print("\n")
    print("=" * 40)
    print(" SMART RESTAURANT SYSTEM ")
    print("=" * 40)

    print("1. New Customer")
    print("2. Daily Report")
    print("3. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        customer_name = input(
            "\nEnter Customer Name: "
        )

        
        order_list, total_bill = take_order()

        discount, gst, final_bill = calculate_bill(
            total_bill
        )

        print_bill(
            customer_name,
            order_list,
            total_bill,
            discount,
            gst,
            final_bill
        )

        analytics.customers_served += 1

        analytics.total_revenue += final_bill

    elif choice == "2":

        analytics.daily_report()

    elif choice == "3":

        print("\nThank You!")
        break

    else:

        print("Invalid Choice")
