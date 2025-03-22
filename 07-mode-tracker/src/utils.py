import csv
from datetime import date
import os
import pandas as pd


MOOD_FILE = "src/mood-log.csv"

def load_mode_data() -> pd.DataFrame:
    """
    Load mood data from a CSV file if it exists, otherwise return an empty DataFrame with columns "Date" and "Mood".
    """

    if os.path.exists(MOOD_FILE):
        return pd.read_csv(MOOD_FILE)
    return pd.DataFrame(columns=["Date", "Mood"])


def save_mood_data(date: date, mood: str):
    with open(MOOD_FILE, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])


