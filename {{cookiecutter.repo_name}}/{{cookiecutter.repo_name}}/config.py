## this will get the env vars that are used for the data pull
import logging
from sqlalchemy import URL, create_engine
import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class DatabaseCredentials:
    db: str
    user:str 
    host:str 
    port:str 
    password:str 
    engine:str
    file_name: str = ".env"

    def __post_init__(self):
        load_dotenv(self.file_name)
        self.db = os.getenv("db")
        self.user = os.getenv("user")
        self.host = os.getenv("host")
        self.port = os.getenv("port")
        self.password = os.getenv("password")
        self.engine = os.getenv("engine")
        return self
        









