import sqlalchemy
from core.settings import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_URL)
metadata = sqlalchemy.MetaData(engine)

Session = sessionmaker(engine)

# 