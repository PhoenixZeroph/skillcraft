"""Helper para llamadas a Granite vía watsonx.ai"""
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
from ibm_watsonx_ai.foundation_models import Model   # noqa: E402
import pandas as pd                                   # noqa: E402

COST_FILE = Path("costing/cost_sheet.csv")
COST_FILE.parent.mkdir(parents=True, exist_ok=True)

model = Model(
    model_id="granite-3-8b-instruct",
    project_id=os.getenv("PROJECT_ID"),
    api_key=os.getenv("API_KEY"),
    url="https://us-south.ml.cloud.ibm.com",
)

def log_ru(ru: float, cuh: float = 0.0):
    row = pd.DataFrame([[pd.Timestamp.utcnow(), ru, cuh]],
                       columns=["timestamp", "ru", "cuh"])
    row.to_csv(COST_FILE, mode="a", header=not COST_FILE.exists(), index=False)


def complete(prompt: str, max_tokens: int = 512) -> str:
    resp = model.generate(prompt, max_new_tokens=max_tokens)
    ru = (resp.usage.input_tokens + resp.usage.generated_tokens) / 1000.0
    log_ru(ru)
    return resp.generated_text
