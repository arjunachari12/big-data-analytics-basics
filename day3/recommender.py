from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Personalized Recommendations Example") \
    .getOrCreate()

# Sample data: User-item interactions (user_id, item_id, rating)
data = [
    (1, 1, 5),
    (1, 2, 4),
    (2, 1, 2),
    (2, 2, 3),
    (3, 1, 4),
    (3, 2, 5)
]

# Create DataFrame for user-item interactions
interactions_df = spark.createDataFrame(data, ["user_id", "item_id", "rating"])

# Split data into training and testing sets
(training_data, test_data) = interactions_df.randomSplit([0.8, 0.2])

# Build the recommendation model using ALS on the training data
als = ALS(maxIter=5, regParam=0.01, userCol="user_id", itemCol="item_id", ratingCol="rating")
model = als.fit(training_data)

# Evaluate the model by computing the RMSE on the test data
predictions = model.transform(test_data)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root Mean Squared Error (RMSE) =", rmse)

# Generate top-N recommendations for each user
user_recommendations = model.recommendForAllUsers(5)

# Show personalized recommendations for a specific user
user_id = 1
user_recommendations.filter(col("user_id") == user_id).show(truncate=False)

# Stop SparkSession
spark.stop()
