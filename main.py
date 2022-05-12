from fastapi import FastAPI

from api_requests import BooksPredictionRequest, OneBookPredictionRequest
from book_genres_model_predict import PredictGenres

app = FastAPI()

@app.get("/health_check")
async def health_check():
	return {"message": "ok"}

@app.post("/bookgenres/one-book-predictions")
async def oneBookPredict(item: OneBookPredictionRequest):
	res = {}
	res["book_id"] = item.book_id
	genres = []
	genres = PredictGenres(item.thumbnail_link)
	# img_url = 'https://blog-cdn.reedsy.com/uploads/2019/12/stargazing-705x1024.jpg'
	# genres = PredictGenres(img_url)
	res["genres"] =  genres
	return res

@app.post("/bookgenres/books-predictions")
async def oneBookPredict(item: BooksPredictionRequest):
	return item