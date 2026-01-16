import sqlite3
import pandas as pd

conn = sqlite3.connect("mappings.db")

df = pd.read_csv("data/products.csv")
df[["product_id", "final_category"]].to_sql(
    "product_category_mapping",
    conn,
    if_exists="replace",
    index=False
)
