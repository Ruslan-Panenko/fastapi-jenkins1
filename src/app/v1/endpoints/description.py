from models.kasuria import TokenDescription, ProtocolDescription
from fastapi import status, APIRouter, HTTPException

from db.base import Session

router = APIRouter(prefix="/description")


@router.get('/token/{token_symbol}/', status_code=status.HTTP_200_OK)
async def get_token_description(token_symbol: str):
    with Session() as session:
        token_description = session.query(TokenDescription).filter_by(
            token_symbol=token_symbol.upper()
        ).first()

        if not token_description:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='data not found')

    return {'tokenDescription': token_description.token_description}


@router.get('/protocol/{protocol_name}/', status_code=status.HTTP_200_OK)
async def get_protocol_descriptions(protocol_name: str):
    with Session() as session:
        protocol_description = session.query(ProtocolDescription).filter_by(
            protocol_name=protocol_name
        ).first()

        if not protocol_description:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='data not found')
    return {"protocolDescription": protocol_description.protocol_description}
