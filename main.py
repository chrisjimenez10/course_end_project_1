import funcs as funcs
import os

def clear_screen():
    """Function clears screen/terminal output"""

    # Operating System - 1.Windows = "nt" , 2.Linux, MacOS, Unix = "posix", 3.Jython/JVM = "java"
    os.system("cls" if os.name == "nt" else "clear")


def main_program():
    # Initiate program with geneartion of customers with SINGLE order
    customers_in_session = funcs.generate_customers()
    print("Welcome to the Busienss!")

    while True:
        print(F"""---------- Menu ----------
1. Add orders to customers
2. Display top 3 customers
3. Display business insights
4. Display number of products sold
5. Display customer analysis
6. Exit""")
        
        try:
            user_input = int(input("\nWhat would you like to do? ").strip())
            match user_input:
                case 1:
                    funcs.adding_orders_to_customers(customers=customers_in_session, orders_to_add=1)
                    clear_screen()
                    print("+ An order has ben added +")
                case 2:
                    funcs.top_three_customers(customers=customers_in_session)
                case 3:
                    funcs.generate_business_insights(customers=customers_in_session)
                case 4:
                    funcs.number_of_products_sold(customers=customers_in_session)
                case 5:
                    funcs.analyze_customer_orders(customers=customers_in_session)
                case 6:
                    print("Exiting...")
                    return
                case _:
                    clear_screen()
                    print("Invalid input, please type 1-6.")
                    continue
        except ValueError:
            clear_screen()
            print("Invalid input, please provide a number from menu.")
            continue
        
        input("\nPress ENTER to continue...")
        clear_screen()

if __name__ == "__main__":
    main_program()