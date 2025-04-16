# app/utils/llama_client.py
import httpx
# http://host.docker.internal:11434
# OLLAMA_URL = "http://host.docker.internal:11434/api/generate"


OLLAMA_URL = "http://localhost:11434/api/generate"

async def generate_summary_with_llama(prompt: str) -> str:
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(OLLAMA_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "No summary generated")
        except Exception as e:
            return f"Error from LLaMA: {str(e)}"
