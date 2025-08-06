from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from git_pipeline.config.ConfigStore import *
from git_pipeline.functions import *

def filter_employee_by_id(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("Empno") == lit("7369")))
