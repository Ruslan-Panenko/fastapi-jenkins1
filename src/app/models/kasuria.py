from db.base import engine, metadata
import sqlalchemy

# connection to  analytics.mvp_tool_metrics
KasuriaData = sqlalchemy.Table(
    'mvp_tool_metrics',
    metadata,
    schema='analytics',
    autoload=True,
    autoload_with=engine
)

# connection to  analytics.mvp_tr_graph
TrGraph = sqlalchemy.Table(
    'mvp_tr_graph',
    metadata,
    schema='analytics',
    autoload=True,
    autoload_with=engine
)

# connection to  stg.token_descriptions
TokenDescription = sqlalchemy.Table(
    'token_descriptions',
    metadata,
    schema='stg',
    autoload=True,
    autoload_with=engine
)

# connection to  stg.protocol_descriptions
ProtocolDescription = sqlalchemy.Table(
    'protocol_descriptions',
    metadata,
    schema='stg',
    autoload=True,
    autoload_with=engine
)

# connection to  stg.mvp_tokens_categorization
MvpTokensCategorization = sqlalchemy.Table(
    'mvp_tokens_categorization',
    metadata,
    schema='stg',
    autoload=True,
    autoload_with=engine
)
# connection to  stg.asset_registry
AssetRegistry = sqlalchemy.Table(
    'asset_registry',
    metadata,
    schema='stg',
    autoload=True,
    autoload_with=engine
)
