from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("SparkSQL Example") \
    .getOrCreate()

# Sample data
data = [("John", 25), ("Alice", 30), ("Bob", 35)]

# Define schema
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Register DataFrame as a temporary table
df.createOrReplaceTempView("people")

# Perform SQL queries
result = spark.sql("SELECT * FROM people WHERE Age >= 30")

# Show results
result.show()

# Stop SparkSession
spark.stop()
