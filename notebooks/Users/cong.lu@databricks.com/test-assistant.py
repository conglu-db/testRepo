# Databricks notebook source
# MAGIC %sql
# MAGIC select 1+1

# COMMAND ----------

# MAGIC %sql
# MAGIC gfd = 10
# MAGIC print(gfd)

# COMMAND ----------

import time
time.sleep(10)

# COMMAND ----------

# MAGIC %md
# MAGIC | Column 1 | Column 2 | Column 3 |
# MAGIC |----------|----------|----------|
# MAGIC | Row 1, Column 1 | Row 1, Column 2 | Row 1, Column 3 |
# MAGIC | Row 2, Column 1 | Row 2, Column 2 | Row 2, Column 3 |
# MAGIC | Row 3, Column 1 | Row 3, Column 2 | Row 3, Column 3 |
# MAGIC
# MAGIC This is the quadratic formula:
# MAGIC
# MAGIC $$
# MAGIC x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
# MAGIC $$

# COMMAND ----------

# MAGIC %md
# MAGIC | Column 1 | Column 2 | Column 3 |
# MAGIC |----------|----------|----------|
# MAGIC | Row 1, Column 1 | Row 1, Column 2 | Row 1, Column 3 |
# MAGIC | Row 2, Column 1 | Row 2, Column 2 | Row 2, Column 3 |
# MAGIC | Row 3, Column 1 | Row 3, Column 2 | Row 3, Column 3 |
# MAGIC
# MAGIC This is the quadratic formula:
# MAGIC
# MAGIC $$
# MAGIC x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
# MAGIC $$

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from airbnb

# COMMAND ----------

import time
time.sleep(50)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   DATE_TRUNC('week', tpep_pickup_datetime) AS week_start, 
# MAGIC   COUNT(*) AS total_trips 
# MAGIC FROM main.nyctaxi.trips 
# MAGIC GROUP BY DATE_TRUNC('week', tpep_pickup_datetime) 
# MAGIC ORDER BY week_start ASC

# COMMAND ----------

# MAGIC %md
# MAGIC https://www.google.com

# COMMAND ----------

display(_sqldf)

# COMMAND ----------

# MAGIC %sql
# MAGIC select 1 from sth --v
# MAGIC /*gfgjd*/

# COMMAND ----------

import time
time.sleep(10)

# COMMAND ----------

# DBTITLE 1, 
# MAGIC %sql
# MAGIC SELECT 
# MAGIC   DATE_TRUNC('week', tpep_pickup_datetime) AS week_start, 
# MAGIC   COUNT(*) AS total_trips 
# MAGIC FROM main.nyctaxi.trips 
# MAGIC GROUP BY DATE_TRUNC('week', tpep_pickup_datetime) 
# MAGIC ORDER BY week_start ASC

# COMMAND ----------

print(1)

# COMMAND ----------

for i in range(1,11):
    print(i)

# COMMAND ----------

for i in range(1,5):
    print(i)

# COMMAND ----------

gfd

# COMMAND ----------

# MAGIC %md
# MAGIC %ai
# MAGIC
# MAGIC jfiovjiodf

# COMMAND ----------

# MAGIC %md
# MAGIC generate a sql quert

# COMMAND ----------

# MAGIC %md
# MAGIC Here's an example SQL query to retrieve the average price and the maximum number of reviews per property type from the `hive_metastore.default.airbnb` table:
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   property_type,
# MAGIC   AVG(price) AS avg_price,
# MAGIC   MAX(number_of_reviews) AS max_reviews
# MAGIC FROM
# MAGIC   hive_metastore.default.airbnb
# MAGIC GROUP BY
# MAGIC   property_type
# MAGIC ORDER BY
# MAGIC   avg_price DESC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC This query groups the listings by `property_type` and calculates the average price and maximum number of reviews for each group. It then sorts the groups in descending order by average price.

# COMMAND ----------

print(1)

# COMMAND ----------

x = 5
y = 3
print(x + y)

# COMMAND ----------

print('Hello, World!')

# COMMAND ----------

print(2)

# COMMAND ----------

print('Hello, World!')

# COMMAND ----------

print(2)

# COMMAND ----------

print(3)

# COMMAND ----------

print(4)

# COMMAND ----------

print('Hello, world!')

# COMMAND ----------

print(1)

# COMMAND ----------

print(1)

# COMMAND ----------

print(2)

# COMMAND ----------

print(3)

# COMMAND ----------

print('Hello, World!')

# COMMAND ----------

print('Hello, World!')

# COMMAND ----------

(92-32)*5/9