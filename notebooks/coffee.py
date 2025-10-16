import pandas as pd
from dateutil import parser
from pathlib import Path

RAW = Path("data/raw/Coffe_sales.csv")
PROCESSED = Path("data/processed/coffee.csv")

df = pd.read_csv(RAW)

df.head()