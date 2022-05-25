import json
from re import sub
import pandas as pd
from fastapi import status, APIRouter, HTTPException

from db.base import Session
from models.kasuria import KasuriaData, TrGraph

router = APIRouter(prefix="/metrics")


def string_to_camelcase(text):
    text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
    text = text.replace('.', '')
    return ''.join([text[0].lower(), text[1:]])


def dataframe_to_json(df):
    new_names = {column: string_to_camelcase(column)
                 for column in df.columns}
    df = df.rename(columns=new_names)

    to_json = df.to_json(orient="records")

    return json.loads(to_json)


@router.get('/graph/', status_code=status.HTTP_200_OK)
async def get_graph_data(
        time_frame: str = None,
        underlying_currency: str = None,
        strategy_type: str = None,
        token_name: str = None,
        protocol: str = None,
        pool: str = None,

):
    with Session() as session:
        query = session.query(TrGraph).filter_by(
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
        if df.empty:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='data not found')

    df = df[['date_of_record', 'tr_cum']].astype({'date_of_record': str})
    return dataframe_to_json(df)


@router.get('/{currency}/', status_code=status.HTTP_200_OK)
async def get_all_data_by_currency(currency: str):
    with Session() as session:
        query = session.query(KasuriaData).filter_by(
            Currency=currency.upper(),
        )
        df = pd.read_sql_query(
            sql=query.statement,
            con=session.bind
        )

        if df.empty:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f'{currency} - is not currency')

    return dataframe_to_json(df)
