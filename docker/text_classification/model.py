from pydantic import BaseModel


class SentimentAnalysis(BaseModel):
    sentiment: bool
