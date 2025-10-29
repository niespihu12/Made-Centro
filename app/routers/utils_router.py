from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Any
from num2words import num2words
import re

from app.models.utils_model import NumberWordsResponse, NumbersWords

utils_router = APIRouter()

@utils_router.post(
    "/convert-number-to-words",
    tags=["Utils"],
    status_code=200,
    response_description="Number converted to words successfully",
    response_model=NumberWordsResponse
)
async def convert_number_to_words(word: NumbersWords) -> NumberWordsResponse:
    resultado = word.word
    pattern = r"(?<!\w)(\d+)(?!\w)"  

    def reemplazar(match: re.Match) -> str:
        numero = int(match.group(1))
        palabras = num2words(numero, lang='es')
        return palabras

    resultado = re.sub(pattern, reemplazar, resultado)

    return JSONResponse(content={"result": resultado}, status_code=200)
