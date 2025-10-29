from pydantic import BaseModel, Field, field_validator


class NumbersWords(BaseModel):
    word: str = Field( min_length=1)
    
class NumberWordsResponse(BaseModel):
    result: str