import json
from re import sub
import pandas as pd
from fastapi import status, APIRouter

from db.base import engine

router = APIRouter(prefix="/metrics")

def string_to_camelcase(text):
    text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
    text = text.replace('.', '')
    return ''.join([text[0].lower(), text[1:]])

@router.get('/', status_code=status.HTTP_200_OK)
async def main():
    kasuria_metrics_daily = pd.read_sql_table('kasuria_metrics_daily', engine, schema='metrics')
    new_names = {}
    for column in kasuria_metrics_daily.columns:
        new_names[column] = string_to_camelcase(column)
    print(new_names)
    kasuria_metrics_daily = kasuria_metrics_daily.rename(columns=new_names)
    to_json = kasuria_metrics_daily.to_json(orient="records")

    return json.loads(to_json)
