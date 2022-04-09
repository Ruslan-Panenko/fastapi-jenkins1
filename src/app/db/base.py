from core.settings import DB_URL
from sqlalchemy import create_engine


engine = create_engine(DB_URL)