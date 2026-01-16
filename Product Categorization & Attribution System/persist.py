import sqlite3

def persist_results(df, db_name="product_mappings.db"):
    conn = sqlite3.connect(db_name)

    df[[
        "product_id",
        "client",
        "final_category"
    ]].to_sql(
        "product_category_mapping",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()
