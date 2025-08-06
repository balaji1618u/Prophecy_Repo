from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from git_pipeline.config.ConfigStore import *
from git_pipeline.functions import *

def aaa(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Empno", StringType(), True), StructField("Ename", StringType(), True), StructField("Job", StringType(), True), StructField("Mgr", StringType(), True), StructField("Hiredate", StringType(), True), StructField("salary", StringType(), True), StructField("comm", StringType(), True), StructField("deptno", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/prophecy/Emp (1).csv")
