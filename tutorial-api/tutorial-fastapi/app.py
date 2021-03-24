import uvicorn
from fastapi import FastAPI,Query

# init app
app = FastAPI()

# Routes
@app.get('/')
async def index():
	return {"text":"Hello World"}


@app.get('/ping/')
async def index():
	return "pong"



if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)