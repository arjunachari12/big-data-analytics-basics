from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "RDD Example")

# Create RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Perform transformations and actions
squared_rdd = rdd.map(lambda x: x * x)
result = squared_rdd.reduce(lambda x, y: x + y)

print("Squared RDD:", squared_rdd.collect())
print("Sum of Squares:", result)

# Stop SparkContext
sc.stop()
