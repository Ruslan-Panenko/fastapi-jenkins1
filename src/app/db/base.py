import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import DB_URL

engine = create_engine(DB_URL)

metadata = sqlalchemy.MetaData(engine)

Session = sessionmaker(engine)
