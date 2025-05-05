import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request
from agents.task_router import route
from slack_bolt import App as SlackApp
from slack_bolt.adapter.fastapi import SlackRequestHandler

api = FastAPI(title="SkillCraft API")
slack_app = SlackApp(token=os.getenv("SLACK_BOT_TOKEN"),
                    signing_secret=os.getenv("SLACK_SIGNING_SECRET"))
handler = SlackRequestHandler(slack_app)

@slack_app.event("app_mention")
def handle_mention(body, say):
    text = body["event"]["text"]
    response = route(text)
    say(response)

@api.post("/slack/events")
async def endpoint(req: Request):
    return await handler.handle(req)

# =========================================
# FILE: costing/ru_tracker.py
# =========================================
"""CLI para consultar uso acumulado."""
import pandas as pd
from pathlib import Path
import click

COST_FILE = Path("costing/cost_sheet.csv")

@click.command()
def summary():
    df = pd.read_csv(COST_FILE)
    print(df.tail())
    print("\nTotal RU:", df["ru"].sum())
    print("Total CUH:", df["cuh"].sum())

if __name__ == "__main__":
    summary()
