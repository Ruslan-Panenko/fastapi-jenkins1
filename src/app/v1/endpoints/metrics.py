import json
import pandas as pd
from fastapi import status, APIRouter

from db.base import engine

router = APIRouter(prefix="/metrics")

@router.get('/', status_code=status.HTTP_200_OK)
async def main():
    kasuria_metrics_daily = pd.read_sql_table('kasuria_metrics_daily', engine, schema='metrics')
    to_json = kasuria_metrics_daily.to_json(orient="records")

    return json.loads(to_json)
