import sys
import pandas as pd
import logging
from dotenv import load_dotenv
from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import pull_data_from_postgres, push_data_to_postgres


if __name__ == "__main__":
    ## load other vars
    load_dotenv()
    push_table = os.getenv("push_table")
    push_schema = os.getenv("push_schema")
    pull_table = os.getenv("pull_table")
    pull_schema = os.getenv("pull_schema")

    ## read in sample data from csv
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

    ## push data to postgres db
    boolean = push_data_to_postgres(table = push_table, schema = push_schema, df = df)
    logging.info(f"The {push_schema}.{push_table} was loaded {boolean}")


    ## pull data from postgres that we just pushed
    pg_data = pull_data_from_postgres(table = pull_table, schema = pull_schema)
    print(head(pg_data))
