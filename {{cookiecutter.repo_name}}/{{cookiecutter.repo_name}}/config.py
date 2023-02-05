## this will get the env vars that are used for the data pull
import logging
from sqlalchemy import URL
from sqlalchemy import create_engine


class DatabaseEngine:
    def __init__(self, db, user, host, port, password, engine):
        self.db = db
        self.user = user
        self.host = host
        self.port = port
        self.password = password
        self.engine = engine

    def create_engine(self):
        if toupper(self.engine) == "POSTGRES":

            url_object = URL.create(
                "postgresql+psycopg2",
                username=self.user,
                password=self.password,  # plain (unescaped) text
                host=self.host,
                database=self.db,
            )

            engine = create_engine(url_object)
            return engine
        else if toupper(self.engine) == "MSSQL":
            url_object = URL.create(
                "mysql+pymysql",
                username=self.user,
                password=self.password,  # plain (unescaped) text
                host=self.host,
                database=self.db,
            )

            engine = create_engine(url_object)
            return engine
        else if toupper(self.engine) == "ORACLE":
            url_object = URL.create(
                "oracle",
                username=self.user,
                password=self.password,  # plain (unescaped) text
                host=self.host,
                database=self.db,
            )

            engine = create_engine(url_object)
            return engine
        else if toupper(self.engine) == "SQL SERVER":
            url_object = URL.create(
                "mssql+pymssql",
                username=self.user,
                password=self.password,  # plain (unescaped) text
                host=self.host,
                database=self.db,
            )

            engine = create_engine(url_object)
            return engine
        else:
            logging.error(f"{engine} is not supported. please consult with the db lead to get it added or make sure you spelled it right, supported dbs are POSTGRES, MSSQL, ORACLE, or SQL SERVER")


    def postgres(self):


    def engine(self):
        try:
            logging.info(f"Trying to connect to {engine} engine")
