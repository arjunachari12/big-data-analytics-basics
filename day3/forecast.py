from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Supply Chain Demand Prediction") \
    .getOrCreate()

# Sample data: shipments with product demand
shipments_data = [
    (100, 50),
    (200, 100),
    (150, 80),
    (250, 120)
]

# Create DataFrame for shipments
shipments_df = spark.createDataFrame(shipments_data, ["QuantityShipped", "Demand"])

# Feature engineering: Prepare features and label for regression
assembler = VectorAssembler(inputCols=["QuantityShipped"], outputCol="features")
data = assembler.transform(shipments_df).select("features", "Demand")

# Split data into training and testing sets
(training_data, test_data) = data.randomSplit([0.8, 0.2])

# Train a linear regression model
lr = LinearRegression(featuresCol="features", labelCol="Demand")
lr_model = lr.fit(training_data)

# Make predictions on the test data
predictions = lr_model.transform(test_data)

# Show predictions
predictions.show()

# Stop SparkSession
spark.stop()
