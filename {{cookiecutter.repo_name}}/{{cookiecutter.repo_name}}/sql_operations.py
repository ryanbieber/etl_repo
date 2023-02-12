from dataclasses import dataclass
from engine import Engine
import pandas as pd

@dataclass
class SQLOperations:
    engine: Engine
    schema: str
    table: str
    sql_text: str = None
    if_exists: str = "replace"  # change to append if you want to append to table otherwise will default to replace

    def pull_data(self):
        try:    
            if sql_text is not None:
                logging.info(f"Trying to load data from {self.schema}.{self.table}")
                df = pd.read_sql_table(
                    table_name = self.table,
                    con = self.engine,
                    schema = self.schema
                )
            else:
                logging.info(f"Trying to load data from {self.schema}.{self.table}")
                df = pd.read_sql_query(
                    sql = self.sql_text,
                    con = self.engine
                )
        except:
            logging.error(f"Failed to pull data from {self.schema}.{self.table}")
            

    def push_data(self, data: pd.DataFrame):

        logging.info(f"Trying to load data to {self.schema}.{self.table}")
        try:
            data.to_sql(
                name = self.name,
                schema = self.schema,
                con = self.engine,
                if_exists = self.if_exists,
            )
            logging.info(f"Table Succesfully loaded to {self.schema}.{self.table}")
        except:
            logging.error(f"Table failed to load to {self.schema}.{self.table}")






