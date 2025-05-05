from beeai.agents.react import ReActAgent
from .tools import slack_tool, plan_tool, upskill_tool

router = ReActAgent(
    llm="granite-3-8b-instruct",
    tools=[slack_tool, plan_tool, upskill_tool],
)

def route(message: str) -> str:
    """Entrada pública para el bot"""
    return router(message)
