from db.base import engine, metadata
import sqlalchemy

kasuria_data = sqlalchemy.Table(
    'kasuria_metrics_daily', 
    metadata, 
    schema='metrics', 
    autoload=True, 
    autoload_with=engine
)
