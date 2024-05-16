from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Spark Streaming Example") \
    .getOrCreate()

# Create a local StreamingContext with two execution threads and a batch interval of 1 second
ssc = StreamingContext(spark.sparkContext, 1)

# Create a DStream that represents streaming data from a TCP source
lines = ssc.socketTextStream("localhost", 9999)

# Split each line into words
words = lines.flatMap(lambda line: line.split())

# Count each word in each batch
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)

# Print the word counts
word_counts.pprint()

# Start the streaming context
ssc.start()

# Wait for the streaming to finish
ssc.awaitTermination()
