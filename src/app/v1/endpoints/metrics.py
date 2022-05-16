import json
from re import sub
import pandas as pd
from fastapi import status, APIRouter

from db.base import Session, engine
from models.kasuria import kasuria_data

router = APIRouter(prefix="/metrics")

def string_to_camelcase(text):
    text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
    text = text.replace('.', '')
    return ''.join([text[0].lower(), text[1:]])


@router.get('/{currency}/', status_code=status.HTTP_200_OK)
async def get_all_data_by_currency(currency: str):
    with Session() as session:
        query = session.query(kasuria_data).filter_by(Currency=currency.upper())
        df = pd.read_sql_query(
            sql = query.statement,
            con = session.bind
        )
    print(df)
    new_names = {}
    for column in df.columns:
        new_names[column] = string_to_camelcase(column)
    df = df.rename(columns=new_names)
    currency_mask = df['currency'] == currency.upper()
    df = df.loc[currency_mask]
    to_json = df.to_json(orient="records")

    return json.loads(to_json)
