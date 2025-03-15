import random
import requests


def generate_bitcoin() -> float:
    return round(random.randint(1, 1000) * 0.01, 2)


def fetch_side_hustle() -> str | None:
    try:
        response = requests.get("https://simple-fastapi.vercel.app/side-hustles")
        
        if response.status_code == 200:
            return response.json()

        return "Freelancing - Start offering your skills online!"
    
    except Exception as e:
        print(e)
        return None
    

def fetch_money_quote() -> str | None:
    try:
        response = requests.get("https://simple-fastapi.vercel.app/money-quotes")
        
        if response.status_code == 200:
            return response.json()

        return "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn"
    
    except Exception as e:
        print(e)
        return None