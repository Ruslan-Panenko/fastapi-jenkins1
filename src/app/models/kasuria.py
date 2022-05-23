from db.base import engine, metadata
import sqlalchemy

# connection to  analytics.mvp_tool_metrics
kasuria_data = sqlalchemy.Table(
    'mvp_tool_metrics',
    metadata,
    schema='analytics',
    autoload=True,
    autoload_with=engine
)

# connection to  analytics.mvp_tr_graph
tr_graph = sqlalchemy.Table(
    'mvp_tr_graph',
    metadata,
    schema='analytics',
    autoload=True,
    autoload_with=engine
)

# connection to  stg.token_descriptions
token_descriptions = sqlalchemy.Table(
    'token_descriptions',
    metadata,
    schema='stg',
    autoload=True,
    autoload_with=engine
)

# connection to  stg.protocol_descriptions
protocol_descriptions = sqlalchemy.Table(
    'protocol_descriptions',
    metadata,
    schema='stg',
    autoload=True,
    autoload_with=engine
)
