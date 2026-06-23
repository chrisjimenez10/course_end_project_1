from data import products

class Order:
    """Order class to generate a single order and method for displaying order details"""
    def __init__(self, category: str, product_name: str) -> None:
        self.category = category
        self.product_name = product_name
        self.price: float = products[category][product_name]
    

    # Method to display order details
    def display_order_id(self):
        return {
            "category": self.category,
            "product_name": self.product_name,
            "price": self.price
        }
    


class Customer:
    """Customer class to generate a single customer and methods for displaying customer details and adding a single order to shopping cart (list of orders)"""
    def __init__(self, name: str) -> None:
        self.name = name
        self.orders: list[Order] = []


    def display_customer_details(self) -> dict[str, str | list[dict[str, str | float]]]:
        return {
            "customer_name": self.name,
            "orders": [order.display_order_id() for order in self.orders] # <- Here, we are using list comprehension to iterate over the list of orders in each customer object and we ACCESS the _orderId() method for each because we defined it within the Order class to return a dictionary with the order details
        }


    def add_order(self, category: str, product_name: str) -> None:
        """Add single order to customer object orders list"""
        self.orders.append(Order(category=category, product_name=product_name))
    

    def total_spending(self) -> tuple[float, ...]:
        """Calculate total money spent by each customer object"""
        total: float = 0

        # For Business Insights, we need total revenue for each category
        electronics_total = 0
        clothing_total = 0
        home_essentials = 0
        for order in self.orders:
            if order.category == "electronics":
                electronics_total += order.price
            elif order.category == "clothing":
                clothing_total += order.price
            else:
                home_essentials += order.price
        
        total = electronics_total + clothing_total + home_essentials

        # Debug/Check print() statement
        # print(F"{self.name} spent -> \nElectronics = ${electronics_total}\nClothing = ${clothing_total}\nHome Essentials = ${home_essentials}\nTotal = ${total}")
        
        return (round(electronics_total, 2), round(clothing_total, 2), round(home_essentials, 2), round(total, 2))

    
    def rank_value(self) -> int:
        """Rank customer's value based on total money spent"""

        # Unpack tuple return value into individual variables to use "total" -> We can use the underscore for unused values
        _, _, _, total = self.total_spending()
        if total >= 100:
            return 3
        elif total > 50 and total < 100:
            return 2
        else:
            return 1 