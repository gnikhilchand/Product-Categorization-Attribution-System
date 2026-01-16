from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, when

spark = SparkSession.builder \
    .appName("ProductAttribution") \
    .getOrCreate()

df = spark.read.csv("products.csv", header=True)

df = df.withColumn(
    "clean_text",
    lower(col("title"))
)

df = df.withColumn(
    "rule_category",
    when(col("clean_text").rlike("energy drink"), "Energy Drinks")
    .when(col("clean_text").rlike("protein bar"), "Protein Snacks")
    .when(col("clean_text").rlike("soft drink|cola"), "Soft Drinks")
    .when(col("clean_text").rlike("tea"), "Tea & Coffee")
    .otherwise(None)
)

df_final = df.withColumn(
    "final_category",
    when(col("rule_category").isNotNull(), col("rule_category"))
    .otherwise("MANUAL_REVIEW_REQUIRED")
)

df_final.write.mode("overwrite").saveAsTable("product_category_mapping")
