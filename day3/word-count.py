from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("WordCount Example") \
    .getOrCreate()

# Read input text file
input_file_path = "words.txt"
text_rdd = spark.sparkContext.textFile(input_file_path)

# Split each line into words and flatten the result
words_rdd = text_rdd.flatMap(lambda line: line.split())

# Map each word to a tuple (word, 1) for counting
word_count_rdd = words_rdd.map(lambda word: (word, 1))

# Reduce by key to count occurrences of each word
word_counts = word_count_rdd.reduceByKey(lambda x, y: x + y)

# Collect results and print
results = word_counts.collect()
for word, count in results:
    print(f"{word}: {count}")

# Stop SparkSession
spark.stop()
