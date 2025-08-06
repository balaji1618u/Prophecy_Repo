from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from git_pipeline.config.ConfigStore import *
from git_pipeline.functions import *
from prophecy.utils import *
from git_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_aaa = aaa(spark)
    df_filter_employee_by_id = filter_employee_by_id(spark, df_aaa)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("Git_pipeline").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Git_pipeline")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Git_pipeline", config = Config)(pipeline)
    
    spark.streams.resetTerminated()
    spark.streams.awaitAnyTermination()

if __name__ == "__main__":
    main()
