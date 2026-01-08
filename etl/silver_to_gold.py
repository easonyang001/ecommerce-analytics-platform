import pandas as pd
from sqlalchemy import create_engine

# MySQL 連線
engine = create_engine(
    "mysql+pymysql://root:power123@localhost:3306/olist_dw"
)

# 讀 Silver tables
orders = pd.read_sql("""
    SELECT
        order_id,
        order_purchase_timestamp
    FROM silver_orders
""", engine)

items = pd.read_sql("""
    SELECT
        order_id,
        price
    FROM silver_order_items
""", engine)

# 合併訂單與金額
df = orders.merge(items, on="order_id", how="inner")

# 時間處理
df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
df["year_month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)

# 每月營收（Gold 指標）
gold_monthly_revenue = (
    df.groupby("year_month")["price"]
      .sum()
      .reset_index()
      .rename(columns={"price": "monthly_revenue"})
)

# 寫入 Gold table
gold_monthly_revenue.to_sql(
    "gold_monthly_revenue",
    engine,
    if_exists="replace",
    index=False
)

print("ETL completed: Silver → Gold")
