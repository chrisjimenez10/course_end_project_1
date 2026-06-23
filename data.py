# Customer Names
customer_names: list[str] = ["Alex Quiroz", "Chris Jimenez", "Wendy Barajaz", "Ashi Gupta", "Nataly Jimenez", "Luis Ortiz", "Guillermo Ochoa", "Cristiano Ronaldo", "Gloria Jimenez", "Alejandro Jimenez"]

# Products
products: dict[str, dict[str, float]] = {
    "electronics": {
        "wireless mouse": 35.99,
        "bluetooth earbuds": 68.99,
        "webcam": 85.99,
        "power bank": 175.99,
    },
    "clothing": {
        "mens shirt": 15.99,
        "womens hoodie": 23.99,
        "athletic joggers": 32.99,
    },
    "home essentials": {
        "bath towel": 10.99,
        "air purifier": 276.99,
        "couch": 157.99,
    }
}

# Total Orders -> We will use this to map out/increment product count and perform dictionary lookup to display which products were bought and quantity = Easier for inventory management
total_orders: dict[str, dict[str, float]] = {
    "electronics": {
        "wireless mouse": 0,
        "bluetooth earbuds": 0,
        "webcam": 0,
        "power bank": 0,
    },
    "clothing": {
        "mens shirt": 0,
        "womens hoodie": 0,
        "athletic joggers": 0,
    },
    "home essentials": {
        "bath towel": 0,
        "air purifier": 0,
        "couch": 0,
    }
}

# Rank Values - Using a dictionary for faster lookup time to determine customer rank value
rank_value: dict[int, str] = {
    3: "high-value buyer",
    2: "moderate buyer",
    1: "low-value buyer"
}

# Revenue by Category 
# -> We will increment value for each category key WITHIN main program after extracting money spent by each customer in each category
revenue_categories: dict[str, float] = {
    "electronics": 0,
    "clothing": 0,
    "home essentials": 0
}

# Categories -> set data structure of unique categories
unique_categories = set(list(products.keys()))

if __name__ == "__main__":
    print(unique_categories)