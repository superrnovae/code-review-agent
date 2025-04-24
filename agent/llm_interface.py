import os
import requests
import openai

class LLMClient:
    def __init__(self, provider, model):
        self.provider = provider
        self.model = model
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    def run(self, prompt, code_snippet):
        if self.provider == "openai":
            return self._call_openai(prompt, code_snippet)
        elif self.provider == "ollama":
            return self._call_ollama(prompt, code_snippet)
        elif self.provider == "anthropic":
            return self._call_claude(prompt, code_snippet)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _call_openai(self, prompt, code_snippet):
        openai.api_key = self.openai_api_key
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": code_snippet}
            ]
        )
        return response.choices[0].message.content

    def _call_ollama(self, prompt, code_snippet):
        url = f"http://localhost:11434/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": code_snippet}
            ]
        }
        res = requests.post(url, json=payload).json()
        return res["choices"][0]["message"]["content"]

    def _call_claude(self, prompt, code_snippet):
        headers = {
            "x-api-key": self.anthropic_api_key,
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": code_snippet}
            ]
        }
        response = requests.post("https://api.anthropic.com/v1/chat/completions", json=data, headers=headers).json()
        return response["choices"][0]["message"]["content"]
