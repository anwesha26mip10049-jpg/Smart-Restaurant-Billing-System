# billing.py
from menu import menu, show_menu

import analytics 

def take_order():

    total_bill=0
    order_list=[]

    more="y"

    while more.lower()=="y":

        show_menu()

        try:
            choice=int(input("\nEnter item number: "))
            qty=int(input("Enter quantity: "))

        except ValueError:
            print("Please enter numbers only!")
            continue

        if choice in menu:

            if choice==1:
                analytics.burger_count+=qty

            elif choice==2:
                analytics.pizza_count+=qty

            elif choice==3:
                analytics.pasta_count+=qty

            elif choice==4:
                analytics.coke_count+=qty

            elif choice==5:
                analytics.icecream_count+=qty

            item_name=menu[choice][0]
            price=menu[choice][1]

            item_total=price * qty

            total_bill+=item_total

            order_list.append(
                [item_name, qty, item_total]
            )

            print(item_name, "added successfully!")

        else:
            print("Invalid Choice")

        more=input(
            "\nDo you want to order more? (y/n): "
        )

    return order_list, total_bill


def calculate_bill(total_bill):

    discount=0

    if total_bill>=500:
        discount=total_bill * 0.10

    subtotal=total_bill - discount

    gst=subtotal * 0.05

    final_bill=subtotal + gst

    return discount, gst, final_bill


def print_bill(customer_name,
               order_list,
               total_bill,
               discount,
               gst,
               final_bill):

    print("\n")
    print("=" * 40)
    print("         THALI WALA")
    print("=" * 40)

    print("Customer :", customer_name)

    print("\nItems Ordered")

    for item in order_list:

        print(
            item[0],
            "x",
            item[1],
            "= ₹",
            item[2]
        )

    print("\nSubtotal : ₹", total_bill)

    if discount > 0:
        print("Discount : ₹", discount)

    print("GST (5%) : ₹", round(gst, 2))

    print(
        "Final Bill : ₹",
        round(final_bill, 2)
    )

    print("\nThank You For Visiting!")

    print("=" * 40)
