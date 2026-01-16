import pandas as pd
from preprocess import preprocess
from rules import rule_based_tag
from attribution import run_attribution
from persist import persist_results

df = pd.read_csv("data/products.csv")
df = preprocess(df)

result = run_attribution(df, client="Client_A")
persist_results(result)

print(result[["product_id", "client", "final_category"]])

print(df[["product_id", "clean_text"]])

df["rule_category"] = df["clean_text"].apply(rule_based_tag)
print(df[["product_id", "rule_category"]])
