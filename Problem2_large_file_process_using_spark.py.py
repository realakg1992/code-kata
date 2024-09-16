#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CSV Anonymization") \
    .getOrCreate()

# Read large CSV file
df = spark.read.csv('large_dataset.csv', header=True, inferSchema=True)

# Apply SHA-256 anonymization to required columns
df_anonymized = df.withColumn('first_name', sha2(col('first_name'), 256)) \
                  .withColumn('last_name', sha2(col('last_name'), 256)) \
                  .withColumn('address', sha2(col('address'), 256))

# Write anonymized data back to CSV
df_anonymized.write.csv('anonymized_large_dataset_spark.csv', header=True)


# In[ ]:




