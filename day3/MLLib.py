from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("MLlib Example") \
    .getOrCreate()

# Sample data
data = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
df = spark.createDataFrame(data, ["feature1", "feature2", "label"])

# Prepare features column
vector_assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
df = vector_assembler.transform(df)

# Initialize and fit a linear regression model
lr = LinearRegression(featuresCol="features", labelCol="label")
model = lr.fit(df)

# Predict
predictions = model.transform(df)
predictions.select("features", "label", "prediction").show()

# Stop SparkSession
spark.stop()
