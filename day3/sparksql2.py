from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("SparkSQL Example") \
    .getOrCreate()

# Sample data for employees
employees_data = [
    ("1", "John", 25, "HR"),
    ("2", "Alice", 30, "Finance"),
    ("3", "Bob", 35, "Engineering")
]

# Sample data for departments
departments_data = [
    ("HR", "Human Resources"),
    ("Finance", "Finance Department"),
    ("Engineering", "Engineering Department")
]

# Define schemas for employees and departments
employees_schema = StructType([
    StructField("EmployeeId", StringType(), True),
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Department", StringType(), True)
])

departments_schema = StructType([
    StructField("Department", StringType(), True),
    StructField("DepartmentName", StringType(), True)
])

# Create DataFrames
employees_df = spark.createDataFrame(employees_data, schema=employees_schema)
departments_df = spark.createDataFrame(departments_data, schema=departments_schema)

# Register DataFrames as temporary tables
employees_df.createOrReplaceTempView("employees")
departments_df.createOrReplaceTempView("departments")

# Perform SQL operations
# 1. Join employees and departments on Department column
result = spark.sql("""
    SELECT e.Name, e.Age, d.DepartmentName
    FROM employees e
    JOIN departments d
    ON e.Department = d.Department
""")

# 2. Filter employees older than 30
result_filtered = spark.sql("""
    SELECT * 
    FROM employees
    WHERE Age > 30
""")

# 3. Aggregate count of employees by department
result_aggregated = spark.sql("""
    SELECT Department, COUNT(*) AS EmployeeCount
    FROM employees
    GROUP BY Department
""")

# Show results
print("Join result:")
result.show()

print("Filtered result:")
result_filtered.show()

print("Aggregated result:")
result_aggregated.show()

# Stop SparkSession
spark.stop()
