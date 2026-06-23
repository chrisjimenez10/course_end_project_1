from customer_class import Customer
import random
from data import products, customer_names, rank_value, revenue_categories, total_orders


# Functions
def generate_customers() -> list[Customer]:
    """This function generates customers with a single order for each and returns a list of customer objects"""

    total_customers: list[Customer] = []
    for customer_name in customer_names:
        customer = Customer(name=customer_name)
        # We need to extract each individual key and value, so we can pass it to the addOrder() method and ADD orders with unique details to the order list for each customer object
        category = random.choice(list(products.keys())) # Get random category name from the products dictionary (it has a nested dicitonary as the value)
        product_name = random.choice(list(products[category].keys())) # Get random product from within selected category through a direct dictionary lookup
        customer.add_order(category=category, product_name=product_name) # FIRST order added for each customer
        total_customers.append(customer)
        
    return total_customers


def get_random_product() -> tuple[str, str]:
    """Helper funciton to GET random product"""
    random_category = random.choice(list(products.keys()))
    random_product_name = random.choice(list(products[random_category].keys()))
    return random_category, random_product_name # Python automatically returns variables separated by a comma into a tuple (we can also explicitly return a tuple using parenthesis)


def adding_orders_to_customers(customers: list[Customer], orders_to_add: int) -> None:
    for customer in customers:
        for _ in range(orders_to_add):
            category_random, product_random = get_random_product() # <- Here, we unpack the tuple returned by the function and assign individual values to pass to the customer object's add_order() method
            customer.add_order(category=category_random, product_name=product_random)


def analyze_customer_orders(customers: list[Customer]) -> None:
    for customer in customers:
        _, _, _, total = customer.total_spending()
        rank: int = customer.rank_value()
        products_bought = [order.display_order_id()['product_name'] for order in customer.orders]
        if rank == 3:
            print(F"{customer.name} is a {rank_value[3]}\nTotal Spent: ${total}\nProducts Purchased: {products_bought}\n------------------------")
        elif rank == 2:
            print(F"{customer.name} is a {rank_value[2]}\nTotal Spent: ${total}\nProducts Purchased: {products_bought}\n-------------------------")
        else:
            print(F"{customer.name} is a {rank_value[1]}\nTotal Spent: ${total}\nProducts Purchased: {products_bought}\n-------------------------")


def top_three_customers(customers: list[Customer]) -> None:
    # Here, we use list comprehension to create customer_totals, which is a list with tuples as its items -> each item is a tuple and has the customer object and the total money spent (float) for that unique customer - NOTE: we use customer.total_spending[3] to look at the 4th value that the total_spending() method returns (it returns a tuple with 4 values and index #3 contains the total money spent) -> We keep the entire customer object as the first item in the tuple as well to access the attribtes and methods
    customer_totals = [(customer, customer.total_spending()[3]) for customer in customers]
    # Here, we use sort() to rearrange the customer_totals list -> 1.We pass the lambda function to the key parameter to instruct sort() to USE the second item in the tuple item - which is located at index #1 and it's the number/float for total money spent per customer -> 2.We set reverse=True to change order to DESCENDING, which is the same as saying from LARGEST to SMALLEST
    customer_totals.sort(key=lambda x: x[1], reverse=True)

    print("+ Top Spending Customers +\n")
    # Here, we are allowed to use "tuple unpacking" for the items in the iterable "customer_totals" -> That's because each item is a tuple (but it can be a list and we can use square brackets as well - Python does not care) with nth number of items inside that tuple. In our case here, we have 2 items, so we need to declare 2 variables by position
    for i, (customer, total) in enumerate(customer_totals[:3], start=1):
        print(F"{i}. {customer.name} = ${total:.2f}")


def generate_business_insights(customers: list[Customer]) -> None:

    # RESET values to prevent adding revenue WITHOUT adding more orders if function is ran more than once
    revenue_categories['electronics'] = 0.0
    revenue_categories['clothing'] = 0.0
    revenue_categories['home essentials'] = 0.0

    unique_products: set[str] = set()
    multi_category_customers: list[tuple[str, int]] = []
    customers_bought_ele_cloth: list[str] = []
    for customer in customers:
        categories_bought = set()

        for order in customer.orders:
            unique_products.add(order.product_name)
            categories_bought.add(order.category)
        # Conditional logic after full iteration over a single customer and its order list -> ONLY unique categories were added to the categories_bought set, so we check if the length is > 1
        if len(categories_bought) > 1:
            multi_category_customers.append((customer.name, len(categories_bought)))

        # Here, we use the issubset() method for sets to check if both "electronics" and "clothing" are both present in the set that holds the total and unique types of categories bought by each individual customer object
        if {'electronics', 'clothing'}.issubset(categories_bought):
            customers_bought_ele_cloth.append(customer.name)
                
        # Unpack tuple return value from total_spending() method
        electronics, clothing, home_essentials, _ = customer.total_spending()
        revenue_categories['electronics'] += electronics
        revenue_categories['clothing'] += clothing
        revenue_categories['home essentials'] += home_essentials

    print("--------------------------")
    print(F"+ Total Revenue per Category +\n\nElectronics = ${revenue_categories['electronics']:.2f}\nClothing = ${revenue_categories['clothing']:.2f}\nHome Essentials = ${revenue_categories['home essentials']:.2f}")


    print(F"""------------------------------------
Unique Products Sold: {unique_products}""")

    customers_bought_electronics = list({
        # In list comprehension, the sytnax to write nested loop logic is from TOP -> BOTTOM = OUTER -> INNER
        customer.name # <- 4th = The value we are collecting
        for customer in customers # <- 1st = outer loop
        for order in customer.orders # <- 2nd = inner loop
        if order.category == 'electronics' # <- 3rd = filter
    })

    print(F"""------------------------------------
Customer(s) who purchased Electronics: {customers_bought_electronics}""")
    print(F"""------------------------------------
Customer(s) who purchased Electronics + Clothing: {customers_bought_ele_cloth}
------------------------------------""")
    print("+ Customers who purchased from Multiple Categories +\n")
    for multi_category_customer in multi_category_customers:
        print(F"""{multi_category_customer[0]} - Categories: {multi_category_customer[1]}""")
    

def number_of_products_sold(customers: list[Customer]):

    # Reset product value count to ZERO, in case this function is ran again in main program -> Because if we don't call the "adding_orders_to_customers" to add orders, it will be counting non-existing products
    for category in total_orders:
        for product in total_orders[category]:
            total_orders[category][product] = 0
    
    for customer in customers:
        for order in customer.orders:
            if order.product_name in total_orders[order.category]:
                total_orders[order.category][order.product_name] += 1
    
    print("+ Products sold count +")
    descending_product_count = []
    for category, products in total_orders.items():
        for product, count in products.items():
            descending_product_count.append((product, count))
    descending_product_count.sort(key=lambda x: x[1], reverse=True)

    # Here, we wanted access to the index value to display ranking in descending order (most bought to least bought). Using tuple unpacking, we assign those values into a single tuple (product, count) to satisfy the rules to use the for loop with enumerate()
    for i, (product, count) in enumerate(descending_product_count, start=1):
        print(F"{i}. {product} = {count}")
