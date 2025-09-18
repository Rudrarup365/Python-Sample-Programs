import pandas as pd
import random
from faker import Faker

# Initialize faker
fake = Faker()
Faker.seed(4321)
# Number of records
NUM_CUSTOMERS = 10
NUM_PRODUCTS = 8
NUM_ORDERS = 15
NUM_ORDER_ITEMS = 30

# Customers Table
customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address()
    })
df_customers = pd.DataFrame(customers)

# Products Table
products = []
for i in range(1, NUM_PRODUCTS + 1):
    products.append({
        "product_id": i,
        "product_name": fake.word().capitalize(),
        "price": round(random.uniform(10, 500), 2)
    })
df_products = pd.DataFrame(products)

# Orders Table (linked to Customers)
orders = []
for i in range(1, NUM_ORDERS + 1):
    orders.append({
        "order_id": i,
        "customer_id": random.choice(df_customers["customer_id"]),  # foreign key
        "order_date": fake.date_this_year()
    })
df_orders = pd.DataFrame(orders)

# Order Items Table (linked to Orders and Products)
order_items = []
for i in range(1, NUM_ORDER_ITEMS + 1):
    order_items.append({
        "order_item_id": i,
        "order_id": random.choice(df_orders["order_id"]),   # foreign key
        "product_id": random.choice(df_products["product_id"]),  # foreign key
        "quantity": random.randint(1, 5)
    })
df_order_items = pd.DataFrame(order_items)

# Display results
print("\n--- Customers ---")
print(df_customers.to_string())
print("\n--- Products ---")
print(df_products.to_string())
print("\n--- Orders ---")
print(df_orders.to_string())
print("\n--- Order Items ---")
print(df_order_items.to_string())

df_customers.to_csv("datasetcustomers.csv")
df_products.to_csv("datasetproducts.csv")
df_orders.to_csv("datasetorders.csv")
df_order_items.to_csv("datasetorder_items.csv")

df_customers.to_json("datasetcustomers.json")
df_products.to_json("datasetproducts.json")
df_orders.to_json("datasetorders.json")
df_order_items.to_json("datasetorder_items.json")