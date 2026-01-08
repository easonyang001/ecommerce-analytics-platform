import pandas as pd
from sqlalchemy import create_engine

# ===== MySQL 連線設定 =====
MYSQL_USER = "root"
MYSQL_PASSWORD = "olist1234"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "olist_dw"

engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

#  讀取 CSV 
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")
sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")

#  時間欄位轉型 
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])

# 欄位對齊 Silver Schema 
customers = customers[["customer_id","customer_unique_id","customer_city","customer_state"]]
sellers = sellers[["seller_id","seller_city","seller_state"]]
products = products[["product_id","product_category_name","product_weight_g"]]
orders = orders[["order_id","customer_id","order_status","order_purchase_timestamp","order_delivered_customer_date"]]
items = items[["order_id","product_id","seller_id","price","freight_value"]]
payments = payments[["order_id","payment_type","payment_value"]]

#寫入 MySQL（Silver Layer）
customers.to_sql("customers", engine, if_exists="append", index=False)
sellers.to_sql("sellers", engine, if_exists="append", index=False)
products.to_sql("products", engine, if_exists="append", index=False)
orders.to_sql("orders", engine, if_exists="append", index=False)
items.to_sql("order_items", engine, if_exists="append", index=False)
payments.to_sql("payments", engine, if_exists="append", index=False)

print("ETL completed: Raw → Silver loaded.")
