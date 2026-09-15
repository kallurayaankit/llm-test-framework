"""Minimal client for the local Ollama HTTP API."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

DEFAULT_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2:3b"


class OllamaClient:
    """Talks to a locally-running Ollama server."""

    def __init__(self, base_url: str | None = None, model: str | None = None):
        self.base_url = base_url or os.getenv("OLLAMA_URL", DEFAULT_URL)
        self.model = model or os.getenv("OLLAMA_MODEL", DEFAULT_MODEL)

    def generate(self, prompt: str, timeout: int = 120) -> str:
        """Send a prompt, return the model's text response."""
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=timeout,
        )
        response.raise_for_status()
        return response.json()["response"]