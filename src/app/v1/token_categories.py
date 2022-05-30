from fastapi import APIRouter, status
from db.base import Session
from models.kasuria import MvpTokensCategorization

router = APIRouter(prefix='/token_categories')


@router.get('/', status_code=status.HTTP_200_OK)
async def get_token_categories():
    with Session() as session:
        token_categories = session.query(MvpTokensCategorization).all()

    response = {}
    for token_category in token_categories:
        response.setdefault(token_category.category_name, []).append(token_category.token_symbol)

    return response
