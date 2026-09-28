# Smart Restaurant Billing System

menu={
    1: ("Burger", 80),
    2: ("Pizza", 150),
    3: ("Pasta", 120),
    4: ("Coke", 40),
    5: ("Ice Cream", 60)
}


def show_menu():
    print("\n===== MENU =====")

    for key in menu:
        print(key, ".", menu[key][0], "- ₹", menu[key][1])


def take_order():

    
    total_bill=0
    order_list=[]

    more = "y"

    
    while more.lower()=="y":

        show_menu()

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

    return order_list, total_bill


def calculate_bill(total_bill):

    discount=0

    if total_bill>=500:
        discount=total_bill * 0.10

    
    subtotal=total_bill - discount

    gst=subtotal * 0.05

    final_bill=subtotal + gst

    return discount, gst, final_bill


def print_bill(customer_name, order_list,
               total_bill, discount,
               gst, final_bill):

    print("\n")
    print("=" * 40)
    print("      RESTAURANT BILL")
    print("=" * 40)

    print("Customer :", customer_name)

    print("\nItems Ordered:")

    for item in order_list:
        print(item[0], "x", item[1], "= ₹", item[2])

    print("\nSubtotal : ₹", total_bill)
    print("Discount : ₹", discount)
    print("GST (5%) : ₹", round(gst, 2))
    print("Final Bill : ₹", round(final_bill, 2))

    print("\nThank You For Visiting!")
    print("=" * 40)


# Main Program

customer_name=input("Enter Customer Name: ")


order_list, total_bill=take_order()

discount, gst, final_bill=calculate_bill(total_bill)


print_bill(customer_name,
           order_list,
           total_bill,
           discount,
           gst,
           final_bill)
