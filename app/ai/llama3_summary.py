import requests

#  SET Ollama HOST IP HERE
OLLAMA_HOST = "http://host.docker.internal:11434"  # ⚠️ Replace with your actual host IP if it ever changes

def generate_summary(content: str) -> str:
    """
    Generate summary using LLaMA3 via Ollama (running on host machine).
    """
    prompt = f"Please provide a short summary for the following book:\n\n{content}"

    try:
        response = requests.post(f"{OLLAMA_HOST}/api/generate", json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        })

        if response.status_code == 200:
            summary = response.json().get("response", "").strip()
            return " ".join(summary.split())
        else:
            return f" LLaMA3 failed with status code {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f" Error connecting to LLaMA3: {str(e)}"
