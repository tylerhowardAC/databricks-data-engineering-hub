from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, to_date
from delta.tables import DeltaTable

# Databricks Medallion Architecture: Bronze to Silver Delta Ingestion

def init_spark():
    return SparkSession.builder \
        .appName("Databricks-Medallion-ETL") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .getOrCreate()

def process_bronze_to_silver(spark, raw_landing_path, silver_table_path):
    print("[*] Ingesting raw JSON events into Silver Delta Table via Auto Loader...")
    
    # Auto Loader (cloudFiles) streaming ingestion simulation
    streaming_df = spark.readStream \
        .format("cloudFiles") \
        .option("cloudFiles.format", "json") \
        .option("cloudFiles.schemaLocation", f"{silver_table_path}/_checkpoint/schema") \
        .load(raw_landing_path)

    # Clean and enrich data
    enriched_df = streaming_df \
        .filter(col("user_id").isNotNull()) \
        .withColumn("ingestion_timestamp", current_timestamp()) \
        .withColumn("event_date", to_date(col("timestamp")))

    # Write to Silver Delta Table using Append mode with Checkpointing
    query = enriched_df.writeStream \
        .format("delta") \
        .outputMode("append") \
        .option("checkpointLocation", f"{silver_table_path}/_checkpoint/data") \
        .start(silver_table_path)
    
    return query

def optimize_delta_table(spark, silver_table_path):
    print("[*] Running OPTIMIZE and Z-ORDER on Silver Delta Table...")
    # Delta Table Maintenance
    spark.sql(f"OPTIMIZE delta.`{silver_table_path}` ZORDER BY (event_date, user_id)")

if __name__ == "__main__":
    spark_sess = init_spark()
    landing_dir = "/mnt/datalake/landing/events"
    silver_dir = "/mnt/datalake/silver/events"
    
    print("=== Databricks Enterprise Pipeline Initiated ===")
    # Query streaming handle execution placeholder
    # process_bronze_to_silver(spark_sess, landing_dir, silver_dir)
