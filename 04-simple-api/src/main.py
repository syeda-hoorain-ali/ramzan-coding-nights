from fastapi import FastAPI
from src.data import money_quotes, side_hustles
import random


app = FastAPI()

@app.get("/")
def root():
    """Welcome to the Side Hustles and Money Quotes API!"""
    return "Welcome to the Side Hustles and Money Quotes API!"


@app.get("/side-hustles")
def get_side_hustles():
    """Return a random side hustle idea"""
    return random.choice(side_hustles)


@app.get("/money-quotes")
def get_money_quotes():
    """Return a random money quote"""
    return  random.choice(money_quotes)
