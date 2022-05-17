import json
from re import sub
import pandas as pd
from fastapi import status, APIRouter

from db.base import Session
from models.kasuria import kasuria_data, tr_graph

router = APIRouter(prefix="/metrics")


def string_to_camelcase(text):
    text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
    text = text.replace('.', '')
    return ''.join([text[0].lower(), text[1:]])


@router.get('/graph/', status_code=status.HTTP_200_OK)
async def get_graph_data(
        time_frame: int = None,
        underlying_currency: str = None,
        strategy_type: str = None,
        token_name: str = None,
        protocol: str = None,
        pool: str = None,

                         ):
    with Session() as session:
        query = session.query(tr_graph).filter_by(
            time_frame=time_frame,
            underlying_currency=underlying_currency,
            strategy_type=strategy_type,
            token_name=token_name,
            protocol=protocol,
            pool=pool,
        )
        df = pd.read_sql_query(
            sql=query.statement,
            con=session.bind
        )
    new_names = {column: string_to_camelcase(column)
                 for column in df.columns}
    df = df.rename(columns=new_names)
    to_json = df[['dateOfRecord', 'trCum']].to_json(orient="records")

    return json.loads(to_json)


@router.get('/{currency}/', status_code=status.HTTP_200_OK)
async def get_all_data_by_currency(currency: str):
    with Session() as session:
        query = session.query(kasuria_data).filter_by(Currency=currency.upper(),
                                                      )
        df = pd.read_sql_query(
            sql=query.statement,
            con=session.bind
        )
    new_names = {column: string_to_camelcase(column)
                 for column in df.columns}
    df = df.rename(columns=new_names)

    to_json = df.to_json(orient="records")
    return json.loads(to_json)
