## put your custom functions here

from engine import Engine
from sql_operations import SQLOperations
import pandas as pd





def pull_data_from_postgres(engine: Engine, table: str, schema: str):

    try:
        con = SQLOperations(
        engine = engine,
        table = table,
        schema = schema)

        df = con.pull_data()
    except:
        df = None
        logging("Something happened")

    return df

def push_data_to_postgres(engine: Engine, table: str, schema: str, df: pd.DataFrame):

    try:
        con = SQLOperations(
        engine = engine,
        table = table,
        schema = schema)

        con.push_data(df = df)
        return True
    except:
        logging("Something happened")
        return False



