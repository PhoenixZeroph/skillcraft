"""Tools invocadas por BeeAI para cumplir con el prompt‑flow."""
from app.wx_client import complete

def slack_tool(text: str) -> str:
    """Resumen de mensaje de Slack para clasificación rápida"""
    prompt = f"Clasifica la siguiente tarea en menos de 30 palabras:\n{text}"
    return complete(prompt, max_tokens=64)

def plan_tool(spec: str) -> str:
    prompt = (
        "Eres un experto DevOps. Genera un plan paso a paso (bullet list) para automatizar: "
        f"{spec}. Usa máximo 7 bullets."
    )
    return complete(prompt, max_tokens=256)

def upskill_tool(spec: str) -> str:
    prompt = (
        "Sugiere 3 cursos online concretos (título – plataforma – duración) "
        f"para dominar: {spec}"
    )
    return complete(prompt, max_tokens=128)
