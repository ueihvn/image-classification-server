from typing import List
from pydantic import BaseModel

class OneBookPredictionRequest(BaseModel):
	book_id: int
	thumbnail_link: str

class BooksPredictionRequest(BaseModel):
	books: List[OneBookPredictionRequest] = []