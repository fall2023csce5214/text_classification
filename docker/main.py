from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.responses import JSONResponse
import logging
import random
import sys
from typing import Union

from text_classification.model import SentimentAnalysis

app = FastAPI()


FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(stream=sys.stdout, format=FORMAT)
logger = logging.getLogger(__name__)


@app.post("/predict", response_model=SentimentAnalysis)
async def predict(file: UploadFile = File(...)) -> Union[SentimentAnalysis, JSONResponse]:
    try:
        text = (await file.read()).decode("utf-8")
        logger.warning(f"Uploaded text: {text} {type(text)}")
        return SentimentAnalysis(sentiment=random.getrandbits(1))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))