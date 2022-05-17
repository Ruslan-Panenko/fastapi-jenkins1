from db.base import engine, metadata
import sqlalchemy

kasuria_data = sqlalchemy.Table(
    'mvp_tool_metrics',
    metadata,
    schema='analytics',
    autoload=True,
    autoload_with=engine
)

tr_graph = sqlalchemy.Table(
    'mvp_tr_graph',
    metadata,
    schema='analytics',
    autoload=True,
    autoload_with=engine
)
