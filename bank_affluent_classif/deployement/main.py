import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI, File, HTTPException, UploadFile

from typing import Any
from pydantic import BaseModel
import pickle
 
class Customer(BaseModel):
    tested: int 
    fail_pct: float 
    sba_limit: float 
    hbin_qty_sum: int
    p_value: float
    bad: int
    good: int
    ratio: float 
    
def load_model(path:str) -> None:
    return pickle.load(open(path, 'rb'))

model_rev = '1.0.0'

app = FastAPI()
#Index Page
#app.mount("/", StaticFiles(directory="html",html = True), name="static")

@app.get('/')
async def index():
    #Landing Page for your model
    return FileResponse('html/index.html')

@app.get('/favicon.ico')
async def favicon():
    #Favicon for your model page
    return FileResponse('html/favicon.png')

@app.post('/predict/affluent')
async def predict_commonality(Customer: Customer):
    data = Customer.dict()
    model = load_model(f'models/affluent_model_v{model_rev}.pkl')
    prediction = model.predict(data)
    probability = model.predict_proba(data).max()

    return {
        'prediction': prediction[0],
        'probability': probability
    }

if __name__=="__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
