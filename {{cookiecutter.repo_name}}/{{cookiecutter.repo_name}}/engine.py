from config import DatabaseCredentials
import logging
from sqlalchemy import URL, create_engine
from dataclasses import dataclass

@dataclass
class Engine:
    creds: DatabaseCredentials = DatabaseCredentials() ## will grab whatever is in .env file
    def create_engine(self):
        try:
            if toupper(self.creds.engine) == "POSTGRES":

                url_object = URL.create(
                    "postgresql+psycopg2",
                    username=self.creds.user,
                    password=self.creds.password,  # plain (unescaped) text
                    host=self.creds.host,
                    database=self.creds.db,
                )

                engine = create_engine(url_object)
                return engine
            else if toupper(self.creds.engine) == "MSSQL":
                url_object = URL.create(
                    "mysql+pymysql",
                    username=self.creds.user,
                    password=self.creds.password,  # plain (unescaped) text
                    host=self.creds.host,
                    database=self.creds.db,
                )

                engine = create_engine(url_object)
                return engine
            else if toupper(self.creds.engine) == "ORACLE":
                url_object = URL.create(
                    "oracle",
                    username=self.creds.user,
                    password=self.creds.password,  # plain (unescaped) text
                    host=self.creds.host,
                    database=self.creds.db,
                )

                engine = create_engine(url_object)
                return engine
            else if toupper(self.creds.engine) == "SQL SERVER":
                url_object = URL.create(
                    "mssql+pymssql",
                    username=self.creds.user,
                    password=self.creds.password,  # plain (unescaped) text
                    host=self.creds.host,
                    database=self.creds.db,
                )

                engine = create_engine(url_object)
                return engine
            else:
                logging.error(f"{engine} is not supported. please consult with the db lead to get it added or make sure you spelled it right, supported dbs are POSTGRES, MSSQL, ORACLE, or SQL SERVER")
        except:
            logging.error("Failed to create engine, make sure the env file is correct.")
