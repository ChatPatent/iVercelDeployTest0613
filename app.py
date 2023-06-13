from transformers import pipeline
from fastapi import FastAPI

app = FastAPI()

model = pipeline("sentiment-analysis", model="binqiangliu/iVercelDeployTest0613")

@app.post("/predict")
async def predict(text: str):
    result = model(text)[0]
    return {"label": result["label"], "score": result["score"]}