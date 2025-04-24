import yaml

class CodeAnalyzer:
    def __init__(self, llm_client, prompt_mode):
        self.llm_client = llm_client
        self.prompt_mode = prompt_mode
        with open("code_review_agent/prompts/templates.yaml", "r") as f:
            self.templates = yaml.safe_load(f)

    def analyze(self, code_snippet):
        template = self.templates.get(self.prompt_mode)
        if not template:
            raise ValueError(f"Unknown prompt mode: {self.prompt_mode}")
        prompt = template["description"]
        return self.llm_client.run(prompt, code_snippet)
